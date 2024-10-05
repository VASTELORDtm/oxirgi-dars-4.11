from file_operations import File

class Metodi:
    def __init__(self, filename: str):
        self.filename = filename

    def write(self, content: str) -> None:
        file = File(self.filename)
        file.write(content)

    def copy_file(self, new_file_name: str) -> None:
        file = File(self.filename)
        file.copy(new_file_name)

metod = Metodi('output.txt')
metod.write('tak tekshiramiz.')
metod.copy_file('output_copy.txt')

