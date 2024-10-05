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

    def replace(self, old_string: str, new_string: str) -> None:
        file = File(self.filename)
        file.replace_string(old_string, new_string)

    def search(self, query: str) -> bool:
        file = File(self.filename)
        return file.search(query)

metod = Metodi('output.txt')
metod.write('albbata ishladi \n ishlagan bolsa bu pastga tushishi kerak')

metod.copy_file('output_copy.txt')

metod.replace('ishlagan', 'o\'zgartirilgan')

found = metod.search('ishladi')
print(f'String found: {found}')
