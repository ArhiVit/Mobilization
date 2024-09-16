#!/usr/bin/env python
import PySimpleGUI as sg
import keypad
import logic


def main():

    sg.theme('Dark')

    k_sut = 2.11
    k_rent = 1.4
    k_staffTravel = 1.4

    layout_V_E_S = sg.Button('Объем работ\n0.0 м2(шт, м.п.)', expand_x=True, s=(0, 2)), sg.Button('Выработка\n0.0 м2(шт, м.п.)/ч.д.', expand_x=True, s=(0, 2)), sg.Button('Персонал рабочих\n0 чел.', expand_x=True, s=(0, 2))
    layout_sut = sg.Frame('Суточные',
                          [[sg.Button('Оплата чел. в сутки\n0.0 р/ч.д.', expand_x=True, s=(0, 2), key='-T_SUT-'),],
                           [sg.Text('0.0 ₽', expand_x=True,
                                    text_color='red', key='-SUT-')],
                           ],
                          title_color='pink',
                          expand_x=True,
                          )
    layout_rent = sg.Frame('Аренда жилья',
                           [[sg.Button('Оплата за чел. в сутки\n0.0 р/ч.д.', expand_x=True, s=(0, 2)),],
                            [sg.Text('0.0 ₽', expand_x=True,
                                     text_color='red', key='-RENT-')],
                            ],
                           title_color='pink',
                           expand_x=True,
                           )

    layout_staff_travel = sg.Frame('Проезд персонала (1 поездка в 2 месяца)',
                                   [[sg.Button('Оплата чел. в 1 конец\n0.0 р/ч.д.', expand_x=True, s=(0, 2)), sg.Button('Кол-во поездок\n0.0 шт', expand_x=True, s=(0, 2)),],
                                    [sg.Text('0.0 ₽', expand_x=True,
                                             text_color='red', key='-STAFFTRAVEL-')],
                                    ],
                                   title_color='pink',
                                   expand_x=True,
                                   )

    layout = [[layout_V_E_S],
              [layout_sut, layout_rent,],
              [layout_staff_travel],
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
        elif event == '-T_SUT-':
            sut = logic.Sut(keypad.keypad()).sut
            window['-T_SUT-'].update(
                f'Оплата чел. в сутки\n{round(float(sut),2)} ₽/ч.д.')
            window['-SUT-'].update(f'Всего: {round(float(sut*k_sut),2)} ₽')
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
