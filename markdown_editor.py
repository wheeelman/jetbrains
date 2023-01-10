class MarkdownEditor:
    FORMATTING_LST = ['plain', 'bold', 'italic', 'header',
                      'link', 'inline-code', 'new-line', 'unordered-list', 'ordered-list']

    formatter = "Available formatters: plain bold italic header link inline-code new-line"
    special = "Special commands: !help !done"

    def heading(self, text_line):
        while True:
            level = int(input('Level: '))
            if not 0 < level < 6:
                print("The level should be within the range of 1 to 6")
                continue
            heading_text = input('Text: ')

            level = '#' * level
            if text_line:
                return f'\n{level} {heading_text}\n'
            return f'{level} {heading_text}\n'

    def bold(self):
        bold_text = input('Text: ')
        return f'**{bold_text}**'

    def italic(self):
        italic_text = input('Text: ')
        return f'*{italic_text}*'

    def plain_text(self):
        plain_text = input('Text: ')
        return plain_text

    def inline_code(self):
        inline_code = input('Text: ')
        return f'`{inline_code}`'

    def new_line(self):
        return f'\n'

    def link(self):
        label = input('Label: ')
        url = input('URL: ')
        return f'[{label}]({url})'

    def lists(self, type):
        while True:
            n_rows = int(input('Number of rows: '))
            if n_rows < 1:
                print('The number of rows should be greater than zero')
                continue
            rows = list(map(lambda i: input(f'Row number #{i + 1}: ') + '\n', range(n_rows)))
            types = list(map(lambda i: f'{i + 1}. ' if type == 'ordered-list' else f'* ', range(n_rows)))

            # rows = [input(f"Row number #{i + 1}: ") + '\n' for i in range(n_rows)]
            # types = [f'{i + 1}. '
            #          if type == 'ordered-list' else f'* '
            #          for i in range(n_rows)]

            return ''.join(list(map(lambda x, y: x + y, types, rows)))

    def main(self):
        text = ''

        while True:
            if text != '':
                print(text)
            usr_inp = input('Chose a formatter: ')

            if usr_inp not in self.FORMATTING_LST and usr_inp not in ['!help', '!done']:
                print('Unknown formatting type or command')
                continue

            if usr_inp == '!done':
                output = open('output.md', 'w', encoding='utf-8')
                output.write(text)
                output.close()
                break

            if usr_inp == '!help':
                print(self.formatter)
                print(self.special)
            if usr_inp == 'header':
                text += self.heading(text)
            elif usr_inp == 'plain':
                text += self.plain_text()
            elif usr_inp == 'inline-code':
                text += self.inline_code()
            elif usr_inp == 'new-line':
                text += self.new_line()
            elif usr_inp == 'bold':
                text += self.bold()
            elif usr_inp == 'link':
                text += self.link()
            elif usr_inp == 'italic':
                text += self.italic()
            elif usr_inp in ['ordered-list', 'unordered-list']:
                text += self.lists(usr_inp)


if __name__ == '__main__':
    MarkdownEditor().main()
