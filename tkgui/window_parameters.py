# File with class of parameters for main application window\

class WindowParameters:
    def __init__(self):
        self.title = "Numbers in computer"
        self.__padx = 100  # Horizontal offset from the upper left corner of the screen
        self.__pady = 100  # Vertical offset from the upper left corner of the screen
        self.resizable = (False, False)
        self.ico_path = "../img/program_icon64.ico"  # Path to application icon

    def geometry(self) -> str:
        """
        :return: window's geometry in tkinter's template
        """
        return f"+{self.__padx}+{self.__pady}"  # The size is determined automatically
