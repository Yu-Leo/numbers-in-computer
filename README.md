# Numbers in computer

![GitHub](https://img.shields.io/github/license/Yu-Leo/numbers-in-computer)
![GitHub issues](https://img.shields.io/github/issues-raw/Yu-Leo/numbers-in-computer)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/Yu-Leo/numbers-in-computer)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Yu-Leo/numbers-in-computer)

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Yu-Leo/numbers-in-computer)
![GitHub last commit](https://img.shields.io/github/last-commit/Yu-Leo/numbers-in-computer)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Yu-Leo/numbers-in-computer)

## Описание

Приложение для получения компьютерного представления чисел.

## Перевод целых чисел

### Функциональность:

1. Перевод числа из 10й системы счисления 2-ю, прямой, обратный и дополнительный коды
2. Перевод числа из 2й системы счисления 10ю, прямой, обратный и дополнительный коды
3. Перевод числа из прямого кода в 10ю и 2ю системы счисления, обратный и дополнительный коды
4. Перевод числа из обратного кода в 10ю и 2ю системы счисления, прямой и дополнительный коды
5. Перевод числа из дополнительного кода в 10ю и 2ю системы счисления, прямой и обратный коды

### Интерфейс

![int_interface](https://github.com/Yu-Leo/numbers-in-computer/blob/main/docs/int_interface.jpg)

1. Выбор типа числа, перевод которого требуется осуществить.
2. Кнопки, осуществляющие расчёт по значению соответствующего поля (*аналогично*: нажатие **[Enter]** в поле).
3. Кнопки, копирующие значение из соответствующего поля в буфер обмена (*аналогично*: нажатие **[Ctrl]** + **[C]** в
   поле).
4. Кнопки, очищающие все поля, кроме числа двоичных разрядов (*аналогично*: нажатие **[Delete]** в любом поле).


### Демонстрация 

![int_demo](https://github.com/Yu-Leo/numbers-in-computer/blob/main/docs/int_demo.gif)

## Перевод вещественных чисел

### Функциональность:

1. Перевод числа из 10й системы счисления в формат с плавающей запятой с промежуточными результатами
2. Перевод числа из формата с плавающей запятой в 10ю систему счисления с промежуточными результатами

### Интерфейс

![float_interface](https://github.com/Yu-Leo/numbers-in-computer/blob/main/docs/float_interface.jpg)

1. Выбор типа числа, перевод которого требуется осуществить.
2. Кнопки, осуществляющие расчёт по значению соответствующего поля (*аналогично*: нажатие **[Enter]** в поле).
3. Кнопки, копирующие значение из соответствующего поля в буфер обмена (*аналогично*: нажатие **[Ctrl]** + **[C]** в
   поле).
4. Кнопки, очищающие все поля, кроме числа двоичных разрядов (*аналогично*: нажатие **[Delete]** в любом поле).

### Демонстрация 

![float_demo](https://github.com/Yu-Leo/numbers-in-computer/blob/main/docs/float_demo.gif)

## Код

### Используемые библиотеки

* [tkinter](https://docs.python.org/3/library/tkinter.html) - графический интерфейс приложения
* [tkinter.messagebox](https://docs.python.org/3/library/tkinter.messagebox.html) - диалоговые окна
* [Pillow (PIL)](https://pypi.org/project/Pillow/) - работа с изображениями (для отображения иконок на кнопках)
* [pyperclip](https://pypi.org/project/pyperclip/) - работа с буфером обмена

### Установка библиотек

[Инструкция по установке библиотек с помощью PIP](https://pythonru.com/baza-znanij/ustanovka-pip-dlja-python-i-bazovye-komandy)

* tkinter - дополнительная установка не требуется (стандартная библиотека Python)
* tkinter.messagebox - дополнительная установка не требуется (стандартная библиотека Python)
* Pillow (PIL) - `pip install Pillow`
* pyperclip - `pip install pyperclip`

## Использованные материалы

### Перевод целых чисел

* [Теория](https://docs.google.com/presentation/d/1YPI_snJPLiwrhdFxSkXxy7WKKs6D0mhg_8s38qkEKaw/edit#slide=id.p)
* [Практика](http://mathel.ru/int/?n=8)

### Перевод целых чисел

* [Теория](https://docs.google.com/presentation/d/1WugONp8HIJIyVRwtoeOGCsO63haGS3GbfWQums9-0lA/edit#slide=id.p)
* [Практика](http://mathel.ru/real/?m=10&p=5&sr=s_1)