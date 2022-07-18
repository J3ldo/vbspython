from pathlib import Path

class Variable:
    def __init__(self, name, outer):
        self.name = name
        self.outer = outer

    def reference(self):
        return self.name, True  # True is for checking if its an refrence or if you want to apply it.

    def apply(self):
        return self.name + " = ", False

    def set(self, item):
        '''
        :param item: Item to set the variable to. Must be string or int.
        '''
        if not isinstance(item, int) and not isinstance(item, str):
            raise TypeError("Item must be int or string")
        else:
            high_comma = "\""
            with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
                f.write(
                    f"{self.name} = {high_comma + item + high_comma if isinstance(item, str) else item}\n"
                )
