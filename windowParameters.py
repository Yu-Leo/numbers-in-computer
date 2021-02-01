# Файл с классом параметров окна приложения

class WindowParameters:
    def __init__(self):
        self.title = "Numbers in computer"
        self.__padx = 100  # Отступ по горизонтали от верхнего левого угра экрана
        self.__pady = 100  # Отступ по вертикали от верхнего левого угра экрана
        self.resizable = (False, False)
        self.ico_path = "img/program_icon64.ico"  # Путь к иконке приложения

    def geometry(self):
        """Геометрия окна по стандарту tkinter-a"""
        return f"+{self.__padx}+{self.__pady}"  # Размер определяется автоматически
