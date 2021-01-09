# Файл с классом параметров окна приложения

class WindowParameters:
    def __init__(self):
        self.__width = 550
        self.__height = 400
        self.__padx = 100  # Отступ по горизонтали от верхнего левого угра экрана
        self.__pady = 100  # Отступ по вертикали от верхнего левого угра экрана
        self.__resizable = (False, False)
        self.__ico_path = "img/program_icon64.ico"

    def get_geometry(self):
        """Геометрия окна по стандарту tkinter-a"""
        return f"{self.__width}x{self.__height}+{self.__padx}+{self.__pady}"

    def get_resizable(self):
        return self.__resizable

    def get_ico_path(self):
        return self.__ico_path

    def __repr__(self):
        return f"width: {self.__width}\nheight: {self.__height}\n" + \
               f"padding_x: {self.__padx}\npadding_y: {self.__pady}\n" + \
               f"resizable_x: {self.__resizable[0]}\nresizable_y: " + \
               f"{self.__resizable[1]}\n" + f"path_to_icon: {self.__ico_path}"


if __name__ == "__main__":
    p = WindowParameters()
    print(p)
