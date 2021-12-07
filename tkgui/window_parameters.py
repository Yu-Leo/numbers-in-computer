from typing import Tuple


class WindowParameters:
    """
    Class with parameters for main application window (tkinter's window object)
    """

    def __init__(self):
        self.title: str = "Numbers in computer"
        self.__padx: int = 100  # Horizontal offset from the upper left corner of the screen
        self.__pady: int = 100  # Vertical offset from the upper left corner of the screen
        self.resizable: Tuple[bool, bool] = (False, False)
        self.ico_path: str = "../img/program_icon64.ico"  # Path to application icon

    def geometry(self) -> str:
        """
        :return: window's geometry in tkinter's template
        """
        return f"+{self.__padx}+{self.__pady}"  # The size is determined automatically
