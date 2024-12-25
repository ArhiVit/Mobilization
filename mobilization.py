#!/usr/bin/env python
import PySimpleGUI as sg
import keypad
import logic
#251224

def main():

    sg.theme('Dark')

    layout_KT = sg.Frame('Коэффициенты: ',
                          [[sg.Button(f'Суточные,\n{mob.k_sut}', expand_x=True, s=(0, 2), button_color='grey', key='-KSUT-'), 
                            sg.Button(f'Аренда,\n{mob.k_rent}', expand_x=True, s=(0, 2), button_color='grey', key='-KRENT-'),
                            sg.Button(f'Перебазировка,\n{mob.k_staffTravel}', expand_x=True, s=(0, 2), button_color='grey', key='-KSTAFFTRAVEL-'),
                            sg.Button(f'Доставка МАТ,\n{mob.k_delivery}', expand_x=True, s=(0, 2), button_color='grey', key='-KDELIVERY-'),
                           ],
                           [sg.Button(f'ИТР,\n{mob.k_engineer}', expand_x=True, s=(0, 2), button_color='grey', key='-KENGINEER-'), 
                            sg.Button(f'Бытовка,\n{mob.k_trailer}', expand_x=True, s=(0, 2), button_color='grey', key='-KTRAILER-'),
                            sg.Button(f'Проезд,\n{mob.k_placeTravel}', expand_x=True, s=(0, 2), button_color='grey', key='-KPLACETRAVEL-'),
                            sg.Button(f'Прочее,\n{mob.k_otherExpences}', expand_x=True, s=(0, 2), button_color='grey', key='-KOTHEREXPENCES-'),
                           ],],
                          border_width=3,
                          title_location='s',
                          title_color='blue',
                          background_color='gray',
                          expand_x=True,
                          )
    layout_V_E_S = sg.Frame('Общие данные: ',
                          [[sg.Button(f'Объем работ, м2(шт, м.п.)\n{mob.volume}', expand_x=True, s=(0, 2), key='-V-'),
                            sg.Button(f'Выработка, м2(шт, м.п.)/ч.д.\n {mob.efficiency}', expand_x=True, s=(0, 2), key='-E-'),
                            sg.Button(f'Персонал рабочих, чел.\n{mob.staff}', expand_x=True, s=(0, 2), key='-S-'),
                          ]],
                          title_location='n',
                          title_color='gold',
                          expand_x=True,
                          )
    layout_trudoemkost = sg.Text(f'Общая трудоемкость работ: ', expand_x=True, text_color='gold', key='-T-')
    layout_period = sg.Text(f'Срок выполнения работ: ', expand_x=True, text_color='gold', key='-PERIOD-')
    layout_sut = sg.Frame(f'Суточные ({mob.k_sut})',
                          [[sg.Button(f'Оплата чел. в сутки, р/ч.д.\n{mob.sut}', expand_x=True, s=(0, 2), key='-SUT-'),],
                           [sg.Text('Всего: ', expand_x=True,
                                    text_color='red', key='-T_SUT-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_rent = sg.Frame(f'Аренда жилья ({mob.k_rent})',
                           [[sg.Button(f'Оплата за чел. в сутки, р/ч.д.\n{mob.rent}', expand_x=True, s=(0, 2), key='-RENT-'),],
                            [sg.Text('Всего: ', expand_x=True,
                                     text_color='red', key='-T_RENT-')],
                            ],
                           title_color='pink',
                           expand_x=True,
                           )
    layout_staffTravel = sg.Frame(f'Перебазировка персонала на объект\n- 1 поездка в 2 месяца ({mob.k_staffTravel})',
                                   [[sg.Button(f'Оплата чел. в 1 конец, р\n{mob.staffTravel}', expand_x=True, s=(0, 2), key='-STAFFTRAVEL-'), sg.Button(f'Кол-во поездок, шт\n{mob.number_staffTravel}', expand_x=True, s=(0, 2), key='-NUMSTAFFTRAVEL-'),],
                                    [sg.Text('Всего: ', expand_x=True,
                                             text_color='red', key='-T_STAFFTRAVEL-')],
                                    ],
                                   title_color='pink',
                                   expand_x=True,
                                   )
    layout_delivery = sg.Frame(f'Доставка/возврат оборудования и материалов\nдля обеспечения работ ({mob.k_delivery})',
                                   [[sg.Button(f'Расстояние до объекта, км\n{mob.distance}', expand_x=True, s=(0, 2), key='-DISTANCE-'), sg.Button(f'Тариф доставки в 1 конец, р/км\n{mob.delivery}', expand_x=True, s=(0, 2), key='-DELIVERY-'), sg.Button(f'Кол-во рейсов, шт\n{mob.number_delivery}', expand_x=True, s=(0, 2), key='-NUMDELIVERY-')],
                                    [sg.Text('Всего: ', expand_x=True,
                                             text_color='red', key='-T_DELIVERY-')],
                                    ],
                                   title_color='pink',
                                   expand_x=True,
                                   )
    layout_engineer = sg.Frame(f'ИТР на объекте\n(з/п, суточные, жилье, проезд) ({mob.k_engineer})',
                          [[sg.Button(f'Зарплата на руки, р/мес.\n{mob.engineer}', expand_x=True, s=(0, 2), key='-ENGINEER-'),],
                           [sg.Text('Всего: ', expand_x=True,
                                    text_color='red', key='-T_ENGINEER-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_trailer = sg.Frame(f'Бытовка, биотуалет и т.д\nв т.ч. аренда на весь срок ({mob.k_trailer})',
                          [[sg.Button(f'Затраты, р\n{mob.trailer}', expand_x=True, s=(0, 2), key='-TRAILER-'),],
                           [sg.Text('Всего: ', expand_x=True,
                                    text_color='red', key='-T_TRAILER-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_placeTravel = sg.Frame(f'Проезд персонала по месту работ ({mob.k_placeTravel})',
                          [[sg.Button(f'Оплата за чел. в сутки, р/ч.д.\n{mob.placeTravel}', expand_x=True, s=(0, 2), key='-PLACETRAVEL-'),],
                           [sg.Text('Всего: ', expand_x=True,
                                    text_color='red', key='-T_PLACETRAVEL-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_otherExpences = sg.Frame(f'Прочие расходы ({mob.k_otherExpences})',
                          [[sg.Button(f'Затраты, р\n{mob.otherExpences}', expand_x=True, s=(0, 2), key='-OTHEREXPENCES-'),],
                           [sg.Text('Всего: ', expand_x=True,
                                    text_color='red', key='-T_OTHEREXPENCES-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_mob = sg.Text(f'ИТОГО\nМОБИЛИЗАЦИЯ: ', expand_x=True, text_color='red', background_color='yellow', key='-MOB-')
    layout = [[layout_KT],
              [layout_V_E_S],
              [layout_trudoemkost],
              [layout_period],
              [layout_sut, layout_rent,],
              [layout_staffTravel],
              [layout_delivery],
              [layout_engineer, layout_trailer],
              [layout_placeTravel, layout_otherExpences],
              [layout_mob]
              ]

    window = sg.Window('Мобилизационные расходы',
                       layout,
                       auto_size_buttons=True,
                       modal = True,
                       finalize=True,
                       )
    # window.Maximize()

    while True:
        event, values = window()
        if event in (sg.WIN_CLOSED, '\U00002716'):
            break
        elif event == '-KSUT-':
            mob.k_sut = round(float(keypad.keypad()), 2)
        elif event == '-KRENT-':
            mob.k_rent = round(float(keypad.keypad()), 2)
        elif event == '-KSTAFFTRAVEL-':
            mob.k_staffTravel = round(float(keypad.keypad()), 2)
        elif event == '-KDELIVERY-':
            mob.k_delivery = round(float(keypad.keypad()), 2)
        elif event == '-KENGINEER-':
            mob.k_engineer = round(float(keypad.keypad()), 2)
        elif event == '-KTRAILER-':
            mob.k_trailer = round(float(keypad.keypad()), 2)
        elif event == '-KPLACETRAVEL-':
            mob.k_placeTravel = round(float(keypad.keypad()), 2)
        elif event == '-KOTHEREXPENCES-':
            mob.k_otherExpences = round(float(keypad.keypad()), 2)
        elif event == '-V-':
            mob.volume = round(float(keypad.keypad(0.1, 100000)), 2)
        elif event == '-E-':
            mob.efficiency = round(float(keypad.keypad(0.1, 1000)), 2)
        elif event == '-S-':
            mob.staff = round(float(keypad.keypad(1, 1000)), 2)
        elif event == '-SUT-':
            mob.sut = round(float(keypad.keypad()), 2)
        elif event == '-RENT-':
            mob.rent = round(float(keypad.keypad()), 2)   
        elif event == '-STAFFTRAVEL-':
            mob.staffTravel = round(float(keypad.keypad()), 2)
        elif event == '-NUMSTAFFTRAVEL-':
            mob.number_staffTravel = round(float(keypad.keypad()), 2)
        elif event == '-DISTANCE-':
            mob.distance = round(float(keypad.keypad()), 2)
        elif event == '-DELIVERY-':
            mob.delivery = round(float(keypad.keypad()), 2)
        elif event == '-NUMDELIVERY-':
            mob.number_delivery = round(float(keypad.keypad()), 2)
        elif event == '-ENGINEER-':
            mob.engineer = round(float(keypad.keypad()), 2)
        elif event == '-TRAILER-':
            mob.trailer = round(float(keypad.keypad()), 2)
        elif event == '-PLACETRAVEL-':
            mob.placeTravel = round(float(keypad.keypad()), 2)
        elif event == '-OTHEREXPENCES-':
            mob.otherExpences = round(float(keypad.keypad()), 2)

        
        if not mob.volume or not mob.efficiency or not mob.staff:
            sg.popup_error('АХТУНГ!!!', 'Критическая ошибка!', 'Объем работ, Выработка или Персонал рабочих не может быть 0!', 'Скорректируй ввод!', line_width=50, no_titlebar=True, background_color='grey')
        else:
            win_dict = {
                '-KSUT-': f'Суточные,\n{mob.k_sut}',
                '-KRENT-': f'Аренда,\n{mob.k_rent}',
                '-KSTAFFTRAVEL-': f'Перебазировка,\n{mob.k_staffTravel}',
                '-KDELIVERY-': f'Доставка МАТ,\n{mob.k_delivery}',
                '-KENGINEER-': f'ИТР,\n{mob.k_engineer}',
                '-KTRAILER-': f'Бытовка,\n{mob.k_trailer}',
                '-KPLACETRAVEL-': f'Проезд,\n{mob.k_placeTravel}',
                '-KOTHEREXPENCES-': f'Прочее,\n{mob.k_otherExpences}',
                '-V-': f'Объем работ, м2(шт, м.п.)\n{mob.volume}',
                '-E-': f'Выработка, м2(шт, м.п.)/ч.д.\n{mob.efficiency}',
                '-S-': f'Персонал рабочих, чел.\n{mob.staff}',
                '-T-': f'Общая трудоемкость работ: {mob.get_trudoemkost()} ч.д.',
                '-PERIOD-': f'Срок выполнения работ бригадой: {mob.get_period()} раб.д. ({round(float(mob.get_period()/24), 2)} кал.мес.)',
                '-SUT-': f'Оплата чел. в сутки, р/ч.д.\n{mob.sut}',
                '-T_SUT-': f'Всего: {mob.get_total_sut()} р',
                '-RENT-': f'Оплата за чел. в сутки, р/ч.д.\n{mob.rent}',
                '-T_RENT-': f'Всего: {mob.get_total_rent()} р',
                '-STAFFTRAVEL-': f'Оплата чел. в 1 конец, р\n{mob.staffTravel}',
                '-NUMSTAFFTRAVEL-': f'Кол-во поездок, шт\n{mob.number_staffTravel}',
                '-T_STAFFTRAVEL-': f'Всего: {mob.get_total_staffTravel()} р',
                '-DISTANCE-': f'Расстояние до объекта, км\n{mob.distance}',
                '-DELIVERY-': f'Тариф доставки в 1 конец, р/км\n{mob.delivery}',
                '-NUMDELIVERY-': f'Кол-во рейсов, шт\n{mob.number_delivery}',
                '-T_DELIVERY-': f'Всего: {mob.get_total_delivery()} р',
                '-ENGINEER-': f'Зарплата на руки, р/мес.\n{mob.engineer}',
                '-T_ENGINEER-': f'Всего: {mob.get_total_engineer()} р',
                '-TRAILER-': f'Затраты, р\n{mob.trailer}',
                '-T_TRAILER-': f'Всего: {mob.get_total_trailer()} р',
                '-PLACETRAVEL-': f'Оплата чел. в сутки, р/ч.д.\n{mob.placeTravel}',
                '-T_PLACETRAVEL-': f'Всего: {mob.get_total_placeTravel()} р',
                '-OTHEREXPENCES-': f'Затраты, р\n{mob.otherExpences}',
                '-T_OTHEREXPENCES-': f'Всего: {mob.get_total_otherExpences()} р',
                '-MOB-': f'ИТОГО\nМОБИЛИЗАЦИЯ: {mob.get_total()} р ({round(float(mob.get_total() / mob.volume), 2)} р/м2(шт, м.п.) или {round(float(mob.get_total() / mob.get_period() / mob.staff), 2)} р/ч.д.)',
            }
            window.fill(win_dict)
    window.close()

if __name__ == '__main__':

    exec(open('config.txt').read())
    param = [volume, efficiency, staff, sut, rent, staffTravel, number_staffTravel, delivery, distance, number_delivery, engineer, trailer, placeTravel, otherExpences]
    k_param = [k_sut, k_rent, k_staffTravel, k_delivery, k_engineer, k_trailer, k_placeTravel, k_otherExpences]
    mob = logic.Mobilization(*param, *k_param)

    main()


# диаметр#\U000000F8
# череп#\U00002620
# пиш.рука#\U0000270D (Е
# конверт#\U00002709
# x#\U00002716 (2718, 2573, 2612, 2327)
# указ.палец#\U0000261A (B, C, E, F)
# внимание#\U000026A0
# настройки#\U00002692
# телефон#\U0000260F (E, 2121, 2706, )
# собачка#\U00000040
# стрелка ввода#\U000023CE (21B2
# рециклинг#\U00002672 (267B
# галочка#\U00002713 (2714, 2611
# лупа#\U00002315
# ножницы#\U00002704 (2702
# стрелки туда-сюда#\U000021C6
# очистить, удалить#\U0000232B
# обновить#\U000021BB
