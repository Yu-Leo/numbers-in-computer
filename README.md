# Numbers in computer
## Описание
Приложение для получения компьютерного представления чисел.

## Функциональность:
1. Перевод числа из 10й системы счисления 2ю, прямой, обратный и дополнительный коды
2. Перевод числа из 2й системы счисления 10ю, прямой, обратный и дополнительный коды
3. Перевод числа из прямого кода в 10ю и 2ю системы счисления, обратный и дополнительный коды
4. Перевод числа из обратного кода в 10ю и 2ю системы счисления, прямой и дополнительный коды
5. Перевод числа из дополнительного кода в 10ю и 2ю системы счисления, прямой и обратный коды

## Интерфейс
### Перевод целых чисел
![int_interface](https://github.com/Yu-Leo/numbers-in-computer/blob/main/int_interface.jpg)
1. Выбор типа числа, перевод которого требуется осуществить (*доступен только режим для перевода целых чисел*).
2. Выбор поля, по которому требуется провести расчёт остальных значений.
3. Кнопки, копирующие значение из соответствующего поля в буфер обмена.
4. Кнопка "Очистить" - очищает все поля, кроме числа двоичных разрядов.
5. Кнопка "Рассчитать" - выполняет расчёт по значению, которое отмечено в п.2 (*аналогично*: нажатие **[Enter]** в 
   соответствующем отмеченному в п.2 полю).
   
## Код
### Используемые модули
* [tkinter](https://docs.python.org/3/library/tkinter.html)
* [tkinter.messagebox](https://docs.python.org/3/library/tkinter.messagebox.html)
* [Pillow (PIL)](https://pypi.org/project/Pillow/)
* [pyperclip](https://pypi.org/project/pyperclip/)

### Файлы
* [main.py](https://github.com/Yu-Leo/numbers-in-computer/blob/main/main.py) - главный код приложения
* [windowParameters.py](https://github.com/Yu-Leo/numbers-in-computer/blob/main/windowParameters.py) - параметры 
  окна приложения
* [widgets.py](https://github.com/Yu-Leo/numbers-in-computer/blob/main/widgets.py) - виджеты, используемые в 
  интерфейсе, и их параметры
* [messageboxes.py](https://github.com/Yu-Leo/numbers-in-computer/blob/main/messageboxes.py) - всплывающие сообщения
* [constants.py](https://github.com/Yu-Leo/numbers-in-computer/blob/main/constants.py) - константы
* [config.py](https://github.com/Yu-Leo/numbers-in-computer/blob/main/config.py) - настройки приложения
* [text.py](https://github.com/Yu-Leo/numbers-in-computer/blob/main/text.py) - фразы, используемые в интерфейсе
* [calculate.py](https://github.com/Yu-Leo/numbers-in-computer/blob/main/calculate.py) - функции, вызываемые для 
  расчёта
* [exceptions.py](https://github.com/Yu-Leo/numbers-in-computer/blob/main/exceptions.py) - исключения приложения
* [numbersKits.py](https://github.com/Yu-Leo/numbers-in-computer/blob/main/numbersKits.py) - "механика" расчётов 

## Использованные материалы
### Перевод целых чисел
* [Теория](https://docs.google.com/presentation/d/1YPI_snJPLiwrhdFxSkXxy7WKKs6D0mhg_8s38qkEKaw/edit#slide=id.p)
* [Практика](http://mathel.ru/int/?n=8)
