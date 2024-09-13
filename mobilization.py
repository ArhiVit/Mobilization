#!/usr/bin/env python
import PySimpleGUI as sg
import keypad
import logic

def main():

    sg.theme('Dark')

    layout = [
              [sg.Text('Проба ввода с Keypad', expand_x=True), sg.Button('\U000026A0\U00002692', s=(1, 1), button_color='grey'), sg.Button('\U0000260F', s=(1, 1), button_color='blue'), sg.Button('\U00002716', s=(1, 1), button_color='red'), ],
              [sg.Button('Доходы (+)',
              expand_x=True,
              #s=(0, 0),
              ),
              sg.Button('Расходы (-)',
              expand_x=True,
              ),
              ],
              [sg.Frame('Суточные', 
              [[sg.Button('Оплата суток',
              expand_x=True,
              )
              ],
              [sg.Text('0.0 ₽', expand_x=True, font=('Helvetica', 8, 'italic'), text_color='red', key='-SUT-')]],
              title_color='pink',
              font=('Helvetica', 10, 'bold'),
              #expand_x=True,
              ),
              #],
              #[
              sg.Frame('Аренда жилья', 
              [[sg.Button('Оплата, р/ч.д.',
              expand_x=True,
              )
              ],
              [sg.Text('0.0 ₽', expand_x=True, font=('Helvetica', 8, 'italic'), text_color='red', key='-RENT-')]],
              title_color='pink',
              font=('Helvetica', 10, 'bold'),
              #expand_x=True,
              )],
              [sg.Frame('Остаток (=)', [[sg.Text('0.0 ₽', expand_x=True, font=('Helvetica', 14, 'italic'), text_color='red', key='-OUT-')], [sg.Multiline('Общие данные', font='Courier 7', text_color='red', background_color='lightblue',justification='center', expand_x=True, disabled=False, no_scrollbar=True, size=(0, 1)), ], ], font=('Helvetica', 14, 'bold'), expand_x=True)],
              ]
    
    window = sg.Window('MAIN_window', layout,
                       #default_button_element_size=(14, 2),
                       font=('Helvetica', 5, 'italic'),
                       auto_size_buttons=False,
                       #modal = True,
                       finalize = True,
                       )
    window.Maximize()
    
    
    while True:
        
        event, values = window.read()
        
        if event in (sg.WIN_CLOSED, '\U00002716'):
            break
    
        elif event == 'Доходы (+)':
            profit = logic.Profit(keypad.keypad()).profit
            window['Доходы (+)'].update(f'Доходы (+)\n{round(float(profit),2)} ₽')
            
        elif event == 'Расходы (-)':
            debet = logic.Debet(keypad.keypad()).debet
            window['Расходы (-)'].update(f'Расходы (-)\n{round(float(debet),2)} ₽')
            
        elif event == 'Оплата суток':
            sut = logic.Sut(keypad.keypad()).sut
            window['Оплата суток'].update(f'Оплата суток\n{round(float(sut),2)} ₽/ч.д.')
            
        result = logic.Result().result()
        window['-OUT-'].update(f'{round(float(result),2)} ₽')
    
    window.close()
    
    
if __name__ == '__main__':
    
    main()
    
    
#диаметр#\U000000F8
#череп#\U00002620
#пиш.рука#\U0000270D (Е
#конверт#\U00002709
#x#\U00002716 (2718, 2573, 2612, 2327)
#указ.палец#\U0000261A (B, C, E, F)
#внимание#\U000026A0
#настройки#\U00002692
#телефон#\U0000260F (E, 2121, 2706, )
#собачка#\U00000040
#стрелка ввода#\U000023CE (21B2
#рециклинг#\U00002672 (267B
#галочка#\U00002713 (2714, 2611
#лупа#\U00002315
#ножницы#\U00002704 (2702
#стрелки туда-сюда#\U000021C6
#очистить, удалить#\U0000232B
#обновить#\U000021BB
