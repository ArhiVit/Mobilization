#!/usr/bin/env python
import PySimpleGUI as sg
import keypad
import logic

def main():

    sg.theme('Dark')

    layout_V_E_S = sg.Button(f'Объем работ, м2(шт, м.п.)\n{mob.volume}', expand_x=True, s=(0, 2), key='-V-'), sg.Button(f'Выработка, м2(шт, м.п.)/ч.д.\n {mob.efficiency}', expand_x=True, s=(0, 2), key='-E-'), sg.Button(f'Персонал рабочих, чел.\n{mob.staff}', expand_x=True, s=(0, 2), key='-S-')
    layout_period = sg.Text(f'Продолжительность выполнения работ: ', expand_x=True, text_color='red', key='-PERIOD-')
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
    layout_staffTravel = sg.Frame(f'Проезд персонала - 1 поездка в 2 месяца ({mob.k_staffTravel})',
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
                          [[sg.Button(f'Общие затраты, р\n{mob.trailer}', expand_x=True, s=(0, 2), key='-TRAILER-'),],
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
                          [[sg.Button(f'Общие затраты, р\n{mob.otherExpences}', expand_x=True, s=(0, 2), key='-OTHEREXPENCES-'),],
                           [sg.Text('Всего: ', expand_x=True,
                                    text_color='red', key='-T_OTHEREXPENCES-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_mob = sg.Text(f'ИТОГО\nмобилизация: ', expand_x=True, text_color='red', key='-MOB-')
    layout = [[layout_V_E_S],
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
        elif event == '-V-':
            mob.volume = round(float(keypad.keypad()), 2)
        elif event == '-E-':
            mob.efficiency = round(float(keypad.keypad()), 2)
        elif event == '-S-':
            mob.staff = round(float(keypad.keypad()), 2)
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



        #period = round(float(mob.volume / mob.efficiency / mob.staff), 2)
        #total_sut = round(float(mob.staff * mob.sut * mob.k_sut * period / 24 * 31), 2)

        total = round(float(mob.get_total_sut() * 10), 2)

        win_dict = {
            '-V-': f'Объем работ, м2(шт, м.п.)\n{mob.volume}',
            '-E-': f'Выработка, м2(шт, м.п.)/ч.д.\n{mob.efficiency}',
            '-S-': f'Персонал рабочих, чел.\n{mob.staff}',
            '-PERIOD-': f'Продолжительность выполнения работ: {mob.get_period()} раб.д. ({round(float(mob.get_period()/24), 2)} кал.мес.)',
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
            '-TRAILER-': f'Общие затраты, р\n{mob.trailer}',
            '-T_TRAILER-': f'Всего: {mob.get_total_trailer()} р',
            '-PLACETRAVEL-': f'Оплата чел. в сутки, р/ч.д.\n{mob.placeTravel}',
            '-T_PLACETRAVEL-': f'Всего: {mob.get_total_placeTravel()} р',
            '-OTHEREXPENCES-': f'Общие затраты, р\n{mob.otherExpences}',
            '-T_OTHEREXPENCES-': f'Всего: {mob.get_total_otherExpences()} р',
            '-MOB-': f'ИТОГО\nмобилизация: {total}',
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
