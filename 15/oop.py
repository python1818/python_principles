


class Daire:
    pi = 3.14
    
    def __init__(self, yaricap):
        self.yaricap = yaricap
    
    
    def cevre(self):
        return (2* self.pi *self.yaricap)
    
    
    def alan(self):
        return self.pi* (self.yaricap**2)

daire1 = Daire(5)
daire2 = Daire(10)

print(daire1.alan())
print(daire1.cevre())
print(daire2.alan())
print(daire2.cevre())