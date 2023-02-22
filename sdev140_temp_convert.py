# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 08:39:54 2022

@author: JenSc
"""


###############################################################################

# =============================================================================
# *-- CELSIUS to FAHRENHEIT --*
# *************************************
# GUI program containing two butttons
# that converts Celsius to Fahrenheit
# or alternatively, F to C
# when a button is clicked
# based on user input.
# formula: f = (9/5)C + 32
# *************************************
# naming convention = PascalCase
# *************************************
# =============================================================================


# *-- imports --*
# *************************************
import tkinter
import tkinter.ttk
import tkinter.font
# import dynamic_txt as txt

# *************************************

# =============================================================================
# code

# *************************************

class ConvertTempGui:
    def __init__(self):
        # *-- initalize and setup window --*
        # *************************************
        self.MainWindow = tkinter.Tk()
        self.MainWindow.title('Temperature Converter')
        self.MainWindow.geometry('800x700+350+50')
        # self.MainWindow.maxsize(800, 600)
        self.MainWindow.configure(bg='#bac3f1')
        # dynamic resizing
        # for x in range(1):
        #     self.MainWindow.columnconfigure(x, weight=1, minsize=100)
        #     self.MainWindow.rowconfigure(x, weight=1, minsize=75)
        #     for y in range(1):
        #         self.WindowFrame = tkinter.Frame(self.MainWindow, relief='ridge', borderwidth=1, bg='#bac3f1')
        #     self.WindowFrame.grid(row=x, column=y, padx=10, pady=10)
        # string var
        self.ConversionValue = tkinter.StringVar()
        # *************************************

        # *-- change icon image for window *--
        # *************************************
        # create object of photoimage class
        IconImage = tkinter.PhotoImage(file='temp_icon.png')
        # set icon for window
        # self.MainWindow.iconbitmap('temp_icon.ico')
        self.MainWindow.iconphoto(False, IconImage)

        # *-- frames --*
        # *************************************
        self.TopFrame = tkinter.Frame(self.MainWindow, bg='#bac3f1')
        self.MiddleFrame = tkinter.Frame(self.MainWindow, bg='#bac3f1')
        self.BottomFrame = tkinter.Frame(self.MainWindow, bg='#bac3f1')
        # frame placement
        self.TopFrame.pack(side='top', expand=True)
        self.MiddleFrame.pack(side='top', expand=True)
        self.BottomFrame.pack(side='bottom', expand=True)

        # *-- labels --*
        # *************************************
        # self.TitleLabel = txt.DynamicLabel(self.TopFrame, text='Temperature Converter',  font=('Silkscreen Regular', 40), bg='#bac3f1', fg='white', justify='center')
        # self.HeadingLabel = txt.DynamicLabel(self.TopFrame, text='Enter a temperature below', font=('Silkscreen regular', 20), bg='#bac3f1', fg='white', justify='center')
        # self.FahrLabel = txt.DynamicLabel(self.MiddleFrame, text='Convert to Fahrenheit', font=('Silkscreen Regular', 16), bg='#bac3f1', fg='white', wraplength=200, justify='center')
        # self.CelsLabel = txt.DynamicLabel(self.MiddleFrame, text='Convert to Celsius', font=('Silkscreen Regular', 16), bg='#bac3f1', fg='white', wraplength=200, justify='center')
        # self.DisplayTemp = txt.DynamicLabel(self.BottomFrame, textvariable=self.ConversionValue, font=('VT323', 80),
        
        self.TitleLabel = tkinter.Label(self.TopFrame, text='Temperature Converter',  font=('Silkscreen Regular', 40), bg='#bac3f1', fg='white', justify='center')
        self.HeadingLabel = tkinter.Label(self.TopFrame, text='Enter a temperature below', font=('Silkscreen regular', 20), bg='#bac3f1', fg='white', justify='center')
        self.FahrLabel = tkinter.Label(self.MiddleFrame, text='Convert to Fahrenheit', font=('Silkscreen Regular', 16), bg='#bac3f1', fg='white', wraplength=200, justify='center')
        self.CelsLabel = tkinter.Label(self.MiddleFrame, text='Convert to Celsius', font=('Silkscreen Regular', 16), bg='#bac3f1', fg='white', wraplength=200, justify='center')
        self.DisplayTemp = tkinter.Label(self.BottomFrame, textvariable=self.ConversionValue, font=('VT323', 80), bg='#bac3f1', fg='white')

        # label placement
        self.TitleLabel.grid(row=0, column=0, pady=50)
        self.HeadingLabel.grid(row=1, column=0)
        self.FahrLabel.grid(row=1, column=0, padx=10, pady=2)
        self.CelsLabel.grid(row=1, column=1, padx=20, pady=2)
        self.DisplayTemp.grid(row=0, column=0)
        # alternate:
        # self.HeadingLabel.pack(side='top', fill='both', expand=True)
        # self.TitleLabel.pack(side='top', fill='both', expand=True)
        # self.FahrLabel.pack(anchor='nw',expand=True,  side='right')
        # self.CelsLabel.pack(anchor='ne', expand=True, side='left')
        # self.DisplayTemp.pack(side='bottom', expand=True, fill='both')
        # self.EntryBoxLabel.grid(row=2, column=1)
        # *************************************

        # *-- text entry --*
        # *************************************
        self.TempEntry = tkinter.ttk.Entry(self.TopFrame, font=('VT323 20'), width=4, justify='center')
        # entry placement
        self.TempEntry.grid(row=2, column=0, pady=20)
        # alternate:
        # self.TempEntry.pack(side='top', expand=True)
        # *************************************

        # *-- buttons --*
        # *************************************
        # loading/resizing button pics
        self.FahrImage = tkinter.PhotoImage(file='f_btn2.png')
        self.CelsImage = tkinter.PhotoImage(file='c_btn1.png')
        self.ResizeFahrImage = self.FahrImage.subsample(2, 2)
        self.ResizeCelsImage = self.CelsImage.subsample(2, 2)

        # create buttons
        self.ConvertFahr = tkinter.Button(self.MiddleFrame, image=self.FahrImage, bg='#bac3f1', border=0)
        self.ConvertCels = tkinter.Button(self.MiddleFrame, image=self.CelsImage, bg='#bac3f1', border=0)
        # button placement
        self.ConvertFahr.grid(row=2, column=0)
        self.ConvertCels.grid(row=2, column=1)
        # alternate:
        # self.ConvertFahr.pack(side='left', expand=True, fill='both')
        # self.ConvertCels.pack(side='right', expand=True, fill='both')
        # *************************************

        # *-- event binding --*
        # *************************************
        self.ConvertFahr.bind('<Button-1>', self.ConvertToFahrenheit)
        self.ConvertFahr.focus()
        self.ConvertCels.bind('<Button-1>', self.ConvertToCelsius)
        self.ConvertCels.focus()
        # self.MainWindow.bind('<Configure>', self.DynamicLabel)

        # *************************************

        tkinter.mainloop()

# =============================================================================
# *-- function(s) --*

    # convert from celsius to fahrenheit
    # *************************************
    def ConvertToFahrenheit(self, event):
        # get input
        self.UserTempEntry = float(self.TempEntry.get())
        # convert
        self.FahrenheitTemp = self.UserTempEntry * 1.8 + 32
        # store new temp in string var and format
        self.ConversionValue.set(f'{self.FahrenheitTemp:.1f}' + u'F\N{DEGREE SIGN}')
    # *************************************

    # convert from fahrenheit to celsius
    # *************************************
    def ConvertToCelsius(self, event):
        # get input
        self.UserTempEntry = float(self.TempEntry.get())
        # convert
        self.CelsiusTemp = (self.UserTempEntry - 32) * .5556
        # store new temp in string var and format
        self.ConversionValue.set(f'{self.CelsiusTemp:.1f}' + u'C\N{DEGREE SIGN}')
    # *************************************

    # # wrap txt in label dynamically
    # def DynamicLabel(self, event):
    #     if self.HeadingLabel.winfo_width() > self.MainWindow.winfo_width():
    #         self.HeadlingLabel.configure(wraplength=self.MainWindow.winfo_width())
    #     self.MainWindow.update_idletasks()

# =============================================================================


# =============================================================================


# *************************************
if __name__ == "__main__":
    ConvertTempGui()

# *************************************

###############################################################################
