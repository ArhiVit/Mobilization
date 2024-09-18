#!/usr/bin/env python
import PySimpleGUI as sg
import keypad
import logic

exec(open('config.txt').read())

def main():

    sg.theme('Dark')

    layout_V_E_S = sg.Button('Объем работ\n0.0 м2(шт, м.п.)', expand_x=True, s=(0, 2), key='-V-'), sg.Button('Выработка\n0.0 м2(шт, м.п.)/ч.д.', expand_x=True, s=(0, 2), key='-E-'), sg.Button('Персонал рабочих\n0 чел.', expand_x=True, s=(0, 2), key='-S-')
    layout_sut = sg.Frame(f'Суточные ({k_sut})',
                          [[sg.Button(f'Оплата чел. в сутки\n0.0 ₽/ч.д.', expand_x=True, s=(0, 2), key='-SUT-'),],
                           [sg.Text('Всего: 0.0 ₽', expand_x=True,
                                    text_color='red', key='-T_SUT-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_rent = sg.Frame(f'Аренда жилья ({k_rent})',
                           [[sg.Button('Оплата за чел. в сутки\n0.0 р/ч.д.', expand_x=True, s=(0, 2)),],
                            [sg.Text('Всего: 0.0 ₽', expand_x=True,
                                     text_color='red', key='-T_RENT-')],
                            ],
                           title_color='pink',
                           expand_x=True,
                           )
    layout_staffTravel = sg.Frame(f'Проезд персонала - 1 поездка в 2 месяца ({k_staffTravel})',
                                   [[sg.Button('Оплата чел. в 1 конец\n0.0 р/ч.д.', expand_x=True, s=(0, 2)), sg.Button('Кол-во поездок\n0.0 шт', expand_x=True, s=(0, 2)),],
                                    [sg.Text('Всего: 0.0 ₽', expand_x=True,
                                             text_color='red', key='-T_STAFFTRAVEL-')],
                                    ],
                                   title_color='pink',
                                   expand_x=True,
                                   )
    layout_delivery = sg.Frame('Доставка/возврат оборудования и материалов\nдля обеспечения работ',
                                   [[sg.Button('Расстояние до объекта\n0.0 км', expand_x=True, s=(0, 2)), sg.Button('Тариф доставки в 1 конец\n0.0 р/км', expand_x=True, s=(0, 2)), sg.Button('Кол-во рейсов\n0.0 шт', expand_x=True, s=(0, 2))],
                                    [sg.Text('Всего: 0.0 ₽', expand_x=True,
                                             text_color='red', key='-T_DELIVERY-')],
                                    ],
                                   title_color='pink',
                                   expand_x=True,
                                   )
    layout_engineer = sg.Frame('ИТР на объекте\n(з/п, суточные, жилье, проезд)',
                          [[sg.Button('Зарплата на руки\n0.0 р/мес.', expand_x=True, s=(0, 2), key='-ENGINEER-'),],
                           [sg.Text('Всего: 0.0 ₽', expand_x=True,
                                    text_color='red', key='-T_ENGINEER-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_trailer = sg.Frame('Бытовка, биотуалет и т.д\nв т.ч. аренда на весь срок',
                          [[sg.Button('Общие затраты\n0.0 р', expand_x=True, s=(0, 2), key='-TRAILER-'),],
                           [sg.Text('Всего: 0.0 ₽', expand_x=True,
                                    text_color='red', key='-T_TRAILER-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_placeTravel = sg.Frame('Проезд персонала по месту работ',
                          [[sg.Button('Оплата за чел. в сутки\n0.0 р/ч.д.', expand_x=True, s=(0, 2), key='-PLACETRAVEL-'),],
                           [sg.Text('Всего: 0.0 ₽', expand_x=True,
                                    text_color='red', key='-T_PLACETRAVEL-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_otherExpences = sg.Frame('Прочие расходы',
                          [[sg.Button('Общие затраты\n0.0 р', expand_x=True, s=(0, 2), key='-OTHEREXPENCES-'),],
                           [sg.Text('Всего: 0.0 ₽', expand_x=True,
                                    text_color='red', key='-T_OTHEREXPENCES-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_mob = sg.Text('ИТОГО\nмобилизация: ', expand_x=True, text_color='red', key='-MOB-')
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
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '\U00002716'):
            break
        elif event == '-SUT-':
            sut = round(float(logic.Sut(keypad.keypad()).sut), 2)
            t_sut = round(float(sut * k_sut), 2)
            window['-SUT-'].update(
                f'Оплата чел. в сутки\n{sut} ₽/ч.д.')
            window['-T_SUT-'].update(f'Всего: {t_sut} ₽')
    window.close()


if __name__ == '__main__':
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
