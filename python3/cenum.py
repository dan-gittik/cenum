class CEnumNamespace(dict):

    def __init__(self):
        self.index = 0
    
    def __getitem__(self, key):
        if not key.startswith('__') and key not in self:
            self[key] = self.index
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if isinstance(value, int):
            self.index = value + 1


class CEnum(type):

    def __prepare__(*args):
        return CEnumNamespace()
