class Magazine:
    def __init__(self, title):
        self.title = title
    


class Newspaper:
    def __init__(self, name):
        self.name = name

m2= Magazine(title="Nokta")
m3= Magazine(title="Leman")

n1= Newspaper(name="Hurriyet")
n2= Newspaper("Bir Gün")

print(m2.title)
print(m3.title)
print(n1.name)
print(n2.name)
