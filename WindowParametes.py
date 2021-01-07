class WindowParameters:
    def __init__(self):
        self.__width = 500
        self.__height = 500
        self.__padx = 100
        self.__pady = 100
        self.__resizable = (False, False)
        self.__ico_path = "img/icon64.ico"

    def get_geometry(self):
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