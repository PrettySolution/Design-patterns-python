class HtmlElement:
    indent_size = 2
    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []  # Here I am going to store inner elements

    def __str__(self):
        return self.__str(0)

    def __str(self, indent):
        lines = []  # here is going to be each line
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')  # Opening tag

        if self.text:  # Processin text if there is some
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:  # Processing inner elements if there are any
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')  # Closing tag
        return '\n'.join(lines)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)


ul = HtmlElement.create('ul')
ul.add_child('li', 'Hello')
print(ul)