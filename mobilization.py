#!/usr/bin/env python
import PySimpleGUI as sg
import keypad
import logic

def main():

    sg.theme('Dark')

    layout_V_E_S = sg.Button('Объем работ, м2(шт, м.п.)\n', expand_x=True, s=(0, 2), key='-V-'), sg.Button('Выработка, м2(шт, м.п.)/ч.д.\n', expand_x=True, s=(0, 2), key='-E-'), sg.Button('Персонал рабочих, чел.\n', expand_x=True, s=(0, 2), key='-S-')
    layout_sut = sg.Frame(f'Суточные ({k_sut})',
                          [[sg.Button(f'Оплата за чел. в сутки, р/ч.д.\n', expand_x=True, s=(0, 2), key='-SUT-'),],
                           [sg.Text('Всего: ', expand_x=True,
                                    text_color='red', key='-T_SUT-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_rent = sg.Frame(f'Аренда жилья ({k_rent})',
                           [[sg.Button('Оплата за чел. в сутки, р/ч.д.\n', expand_x=True, s=(0, 2), key='-RENT-'),],
                            [sg.Text('Всего: ', expand_x=True,
                                     text_color='red', key='-T_RENT-')],
                            ],
                           title_color='pink',
                           expand_x=True,
                           )
    layout_staffTravel = sg.Frame(f'Проезд персонала - 1 поездка в 2 месяца ({k_staffTravel})',
                                   [[sg.Button('Оплата чел. в 1 конец, р\n', expand_x=True, s=(0, 2), key='-STAFFTRAVEL-'), sg.Button('Кол-во поездок, шт\n', expand_x=True, s=(0, 2), key='-NUMSTAFFTRAVEL-'),],
                                    [sg.Text('Всего: ', expand_x=True,
                                             text_color='red', key='-T_STAFFTRAVEL-')],
                                    ],
                                   title_color='pink',
                                   expand_x=True,
                                   )
    layout_delivery = sg.Frame(f'Доставка/возврат оборудования и материалов\nдля обеспечения работ ({k_delivery})',
                                   [[sg.Button('Расстояние до объекта, км\n', expand_x=True, s=(0, 2), key='-DISTANCE-'), sg.Button('Тариф доставки в 1 конец, р/км\n', expand_x=True, s=(0, 2), key='-DELIVERY-'), sg.Button('Кол-во рейсов, шт\n', expand_x=True, s=(0, 2), key='-NUMDELIVERY-')],
                                    [sg.Text('Всего: ', expand_x=True,
                                             text_color='red', key='-T_DELIVERY-')],
                                    ],
                                   title_color='pink',
                                   expand_x=True,
                                   )
    layout_engineer = sg.Frame(f'ИТР на объекте\n(з/п, суточные, жилье, проезд) ({k_engineer})',
                          [[sg.Button('Зарплата на руки, р/мес.\n', expand_x=True, s=(0, 2), key='-ENGINEER-'),],
                           [sg.Text('Всего: ', expand_x=True,
                                    text_color='red', key='-T_ENGINEER-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_trailer = sg.Frame(f'Бытовка, биотуалет и т.д\nв т.ч. аренда на весь срок ({k_trailer})',
                          [[sg.Button('Общие затраты, р\n', expand_x=True, s=(0, 2), key='-TRAILER-'),],
                           [sg.Text('Всего: ', expand_x=True,
                                    text_color='red', key='-T_TRAILER-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_placeTravel = sg.Frame(f'Проезд персонала по месту работ ({k_placeTravel})',
                          [[sg.Button('Оплата за чел. в сутки, р/ч.д.\n', expand_x=True, s=(0, 2), key='-PLACETRAVEL-'),],
                           [sg.Text('Всего: ', expand_x=True,
                                    text_color='red', key='-T_PLACETRAVEL-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_otherExpences = sg.Frame(f'Прочие расходы ({k_otherExpences})',
                          [[sg.Button('Общие затраты, р\n', expand_x=True, s=(0, 2), key='-OTHEREXPENCES-'),],
                           [sg.Text('Всего: ', expand_x=True,
                                    text_color='red', key='-T_OTHEREXPENCES-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_mob = sg.Text(f'ИТОГО\nмобилизация: ', expand_x=True, text_color='red', key='-MOB-')
    layout = [[layout_V_E_S],
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
        volume = default_volume
        efficiency = default_efficiency
        staff = default_staff
        sut = default_sut
        rent = default_rent
        staffTravel = default_staffTravel
        numberTravel = default_numberTravel
        delivery = default_delivery
        distance = default_distance
        numberDelivery = default_numberDelivery
        engineer = default_engineer
        trailer = default_trailer
        placeTravel = default_placeTravel
        otherExpences = default_otherExpences

        event, values = window()
        if event in (sg.WIN_CLOSED, '\U00002716'):
            break
        elif event == '-SUT-':
            sut = round(float(keypad.keypad()), 2)
    
        total_sut = round(float(sut * k_sut), 2)
        m = total_sut * 10

        window['-SUT-'].update(f'Оплата чел. в сутки, р/ч.д.\n{sut}')
        window['-T_SUT-'].update(f'Всего: {total_sut} ₽')
        window['-MOB-'].update(f'ИТОГО\nмобилизация: {m}')
    window.close()


if __name__ == '__main__':

    exec(open('config.txt').read())

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
