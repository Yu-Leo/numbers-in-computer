# Файл с классом параметров окна приложения

class WindowParameters:
    def __init__(self):
        self.title = "Numbers in computer"
        self.__width = 550
        self.__height = 320
        self.__padx = 100  # Отступ по горизонтали от верхнего левого угра экрана
        self.__pady = 100  # Отступ по вертикали от верхнего левого угра экрана
        self.resizable = (False, False)
        self.ico_path = "img/program_icon64.ico"

    def geometry(self):
        """Геометрия окна по стандарту tkinter-a"""
        return f"{self.__width}x{self.__height}+{self.__padx}+{self.__pady}"

    def __repr__(self):
        return f"width: {self.__width}\nheight: {self.__height}\n" + \
               f"padding_x: {self.__padx}\npadding_y: {self.__pady}\n" + \
               f"resizable_x: {self.resizable[0]}\nresizable_y: " + \
               f"{self.resizable[1]}\n" + f"path_to_icon: {self.ico_path}"


if __name__ == "__main__":
    p = WindowParameters()
    print(p)
