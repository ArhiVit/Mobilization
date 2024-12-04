#!/usr/bin/env python
import PySimpleGUI as sg

def check(value):
    try:
        int(value)
        value = value.lstrip('0')
        if not value: value = 0
    except:
        try:
            float(value)
            #s = s.lstrip('0')
        except:
            value = '--> Неверный ввод!'
    return value


def keypad(min_limit=0, max_limit=1000000000000):
    
    sg.theme('Dark')

    layout = [
              [sg.Text(f'Введите число\nот {min_limit} до {max_limit}', justification='center', s=(25,2))],
              [sg.Input('',
              size=(25, 1),
              readonly=True,
              #disabled_readonly_background_color='red',
              disabled_readonly_text_color='red',
              key='input')],
              [sg.Button('1'), sg.Button('2'), sg.Button('3')],
              [sg.Button('4'), sg.Button('5'), sg.Button('6')],
              [sg.Button('7'), sg.Button('8'), sg.Button('9')],
              [sg.Button('.'), sg.Button('0'), sg.Button('\U0000232B')],
              [sg.Button(button_text='\U000023CE', expand_x=True)],
              #[sg.Text('', expand_x=True, font=('Helvetica', 14, 'italic'),text_color='red', key='out')],
              ]
    
    window = sg.Window(
                       'Keypad',
                       layout,
                       disable_close=False,#True,
                       default_button_element_size=(6, 2),
                       auto_size_buttons=False,
                       element_justification='center',
                       modal = True,
                       finalize=True,
                       )

    keys_entered = ''
    out = 0
    
    while True:
        
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '\U0000232B':
            keys_entered = ''
            window['input'].update(keys_entered)
        elif event in '1234567890.':
            keys_entered = values['input']
            keys_entered += event
            keys_entered = check(keys_entered)
            window['input'].update(keys_entered)
        elif event == '\U000023CE':
            if keys_entered in ['--> Неверный ввод!', '.', '', '--> Значение вне диапазона!']:
                keys_entered = '--> Неверный ввод!'
                window['input'].update(keys_entered)
            elif float(keys_entered) > max_limit or float(keys_entered) < min_limit:
                keys_entered = '--> Значение вне диапазона!'
                window['input'].update(keys_entered)
            else:
                out = float(keys_entered)
                break
    
    window.close()
    
    return out


if __name__ == '__main__':
    
    #min_limit = 0
    #max_limit = 1000000000
    
    res = keypad(0, 10)
    #res = keypad()
    
    print(res)
    input()
