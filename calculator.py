# -*- coding: utf-8 -*-
import math
from tkinter import Tk, END, Entry, N, E, S, W, Button
from tkinter import font
from tkinter import Label
from functools import partial


def get_input(entry, argu):
    entry.insert(END, argu)
    # removed 2nd insert function call to fix duplicated input


def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)
    # changed to input_len - 1 to remove the last input character


def clear(entry):
    entry.delete(0, END)
    # changed to 0 to clear entire input, not leave one input char


def calc(entry):
    # get string ready for eval
    input_info = entry.get()
    input_str = str(input_info.strip())
    try:
        # use eval function to evaluate
        result = eval(input_str)
        # clear
        clear(entry)
        # display result
        entry.insert(END, result)
    # handle divide by zero
    except ZeroDivisionError:
        pop_up("Cannot divide by 0 ! \n Enter valid values")
    # handle invalid expressions
    except SyntaxError:
        pop_up("Invalid expression! \n Please enter a valid \n mathematical expression")


def square_root(entry):
    # get string ready for eval
    input_info = entry.get()
    input_str = str(input_info.strip())
    try:
        # use math func to calc sqrt
        result = math.sqrt(float(input_str))
        # clear
        clear(entry)
        # display result
        entry.insert(END, result)
    except ValueError:
        pop_up("Cannot compute square root \n of a negative number! \n Enter valid value")


def percentage(entry):
    # get string ready for eval
    input_info = entry.get()
    input_int = float(str(input_info.strip()))
    # calculate percentage
    result = input_int / 100
    # clear
    clear(entry)
    # display result
    entry.insert(END, result)


# added message parameter for different calculator errors
def pop_up(message):
    popup = Tk()
    # changed resizable params to None instead of zero to align with function definition
    popup.resizable(None, None)
    # changed sizes so error message is more visible to user
    popup.geometry("240x140")
    popup.title("Alert")
    label = Label(popup, text=message, font=font.Font(size=20))
    label.pack(side="top", fill="x", pady=10)
    b1 = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy, font=font.Font(size=15))
    b1.pack()
    # removed 2nd button because it did the same thing


def cal():
    root = Tk()
    # changes background color
    root.configure(bg="#464646")
    root.title("Calc")
    # changed resizable params to None instead of zero to align with function definition
    root.resizable(None, None)
    entry_font = font.Font(size=15)
    entry = Entry(root, justify="right", font=entry_font, bg="#464646", fg="#AFAFAF")
    entry.grid(row=0, column=0, columnspan=4,
               sticky=N + W + S + E, padx=5, pady=5)

    # changed colors to make the calculator "dark mode"
    # reorganized and resized the buttons for a more fluid layout
    cal_button_bg = '#333599'
    num_button_bg = '#5E5E5E'
    other_button_bg = '#AFAFAF'
    text_fg = '#FFFFFF'
    button_active_bg = '#C0C0C0'

    num_button = partial(Button, root, fg=text_fg, bg=num_button_bg,
                         padx=19, pady=3, activebackground=button_active_bg)
    cal_button = partial(Button, root, fg=text_fg, bg=cal_button_bg,
                         padx=19, pady=3, activebackground=button_active_bg)

    button7 = num_button(text='7', bg=num_button_bg,
                         command=lambda: get_input(entry, '7'))
    button7.grid(row=2, column=0, pady=5)

    button8 = num_button(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=2, column=1, pady=5)

    button9 = num_button(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=2, column=2, pady=5)

    button4 = num_button(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=3, column=0, pady=5)

    button5 = num_button(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=3, column=1, pady=5)

    button6 = num_button(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=3, column=2, pady=5)

    button11 = cal_button(text='-', command=lambda: get_input(entry, '-'))
    button11.grid(row=3, column=3, pady=5)

    button1 = num_button(text='1', command=lambda: get_input(entry, '1'))
    button1.grid(row=4, column=0, pady=5)

    button2 = num_button(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=4, column=1, pady=5)

    button3 = num_button(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=4, column=2, pady=5)

    button12 = cal_button(text='*', command=lambda: get_input(entry, '*'))
    button12.grid(row=2, column=3, pady=5)

    # changed to row 4, so button is visible and clickable
    button10 = cal_button(text='+', command=lambda: get_input(entry, '+'))
    button10.grid(row=4, column=3, pady=5)

    button0 = num_button(text='0', command=lambda: get_input(entry, '0'))
    button0.grid(row=5, column=0, pady=5)

    button13 = num_button(text='.', command=lambda: get_input(entry, '.'))
    button13.grid(row=5, column=1, pady=5)

    button14 = cal_button(text='/', command=lambda: get_input(entry, '/'))
    button14.grid(row=1, column=3, pady=5)

    # I removed the backspace functionality, even though I fixed it, in order to make the calculator remain symmetric
    # My logic in removing it is that Clear does almost the same thing, the basic iPhone calculator was my inspiration
    # and that doesn't have a backspace button
    # I left the code here in case the function needs to be added back
    #
    # button15 = Button(root, text='<-', bg=other_button_bg, padx=10, pady=3,
    #                 command=lambda: backspace(entry), activebackground=button_active_bg)
    # button15.grid(row=1, column=0,
    #              padx=3, pady=5, sticky=N + S + E + W)

    button16 = Button(root, text='C', bg=other_button_bg, padx=10, pady=3,
                      command=lambda: clear(entry), activebackground=button_active_bg)
    button16.grid(row=1, column=0, padx=3, pady=5, sticky=N + S + E + W)

    button17 = cal_button(text='=', command=lambda: calc(entry), activebackground=button_active_bg)
    button17.grid(row=5, column=3, pady=5)

    button18 = cal_button(text='^', command=lambda: get_input(entry, '**'))
    button18.grid(row=1, column=1, pady=5)

    button19 = cal_button(text='%', command=lambda: percentage(entry))
    button19.grid(row=5, column=2, pady=5)

    button20 = cal_button(text='√', command=lambda: square_root(entry))
    button20.grid(row=1, column=2, pady=5)

    root.mainloop()

    def quit():
        exit['command'] = root.destroy()

    exit = Button(root, text='Quit', fg='white', bg='black', command=quit, height=1, width=7)
    exit.grid(row=6, column=3)

    label = Label(root, text="Calculator")
    label.grid(row=6, column=2)


if __name__ == '__main__':
    cal()
