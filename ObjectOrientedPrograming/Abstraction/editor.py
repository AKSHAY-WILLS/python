from abc import ABC,abstractmethod

class Editor:

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class Vscode(Editor):

    def open(self):
        print("double click")

    def write(self):
        print("type")

    def debug(self):
        print("click debuging")

    def execute(self):
        print("run")

vscode_instance=Vscode()

vscode_instance.open()

vscode_instance.write()

vscode_instance.debug()

vscode_instance.execute()