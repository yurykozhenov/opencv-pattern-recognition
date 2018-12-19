import tkinter
from tkinter import filedialog

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from lab9 import lab9
from lab10 import lab10
from lab11 import lab11
from lab12 import lab12
from lab13 import lab13
from lab15 import lab15


class MenuScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(
            **kwargs, orientation="vertical", padding=32, spacing=16)

        self.button1 = Button(
            text="Лабораторна робота №9.\nОзнайомлення з бібліотекою OpenCV", halign="center", on_press=self.lab9)
        self.add_widget(self.button1)

        self.button2 = Button(
            text="Лабораторна робота №10.\nГістограма зображення", halign="center", on_press=self.lab10)
        self.add_widget(self.button2)

        self.button3 = Button(
            text="Лабораторна робота №11.\nОбробка зображення", halign="center", on_press=self.lab11)
        self.add_widget(self.button3)

        self.button4 = Button(
            text="Лабораторна робота №12.\nРозпізнавання об’єктів шляхом аналізу габаритних прямокутників", halign="center", on_press=self.lab12)
        self.add_widget(self.button4)

        self.button5 = Button(
            text="Лабораторна робота №13.\nВиділення контура на зображенні", halign="center", on_press=self.lab13)
        self.add_widget(self.button5)

        self.button6 = Button(
            text="Лабораторна робота №15.\nКаскадна класифікація Хаара", halign="center", on_press=self.lab15)
        self.add_widget(self.button6)

    def lab9(self, instance):
        file_path = self.choose_file()

        if file_path != "":
            lab9(file_path)

    def lab10(self, instance):
        file_path = self.choose_file()

        if file_path != "":
            lab10(file_path)

    def lab11(self, instance):
        file_path = self.choose_file()

        if file_path != "":
            lab11(file_path)

    def lab12(self, instance):
        file_path = self.choose_file()

        if file_path != "":
            lab12(file_path)

    def lab13(self, instance):
        file_path = self.choose_file()

        if file_path != "":
            lab13(file_path)

    def lab15(self, instance):
        file_path = self.choose_file()

        if file_path != "":
            lab15(file_path)

    def choose_file(self):
        tkinter.Tk().withdraw()
        return filedialog.askopenfilename()


class MyApp(App):

    def build(self):
        return MenuScreen()


if __name__ == "__main__":
    MyApp().run()
