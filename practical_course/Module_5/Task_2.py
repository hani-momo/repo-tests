import json

class Models:

    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author


    def save(self, filename):
        attrs = {'title': self.title, 'text': self.text, 'author': self.author}
        with open(filename, 'w') as f: # запись
            json.dump(attrs, f)


class C1 :
    title = '1'
    text = '2'
    author = '3'

# test
model = Models("Название статьи", "Текст статьи", "Имя автора")

# метод save
model.save("data.json")

# внутри файла
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)
