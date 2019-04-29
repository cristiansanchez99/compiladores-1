class Pila():
    def __init__(self):
        self.pila = []
        self.numero_elementos = 0

    def apilar_elemento(self,elemento):
        self.pila.append(elemento)
        self.numero_elementos += 1

    def pila_vacia(self):
        if self.numero_elementos == 0:
            return True
        return False

    def desapilar_elemento(self):
        self.numero_elementos -= 1
        return self.pila.pop()

    def vaciar_pila(self):
        while self.pila_vacia() == False:
            self.desapilar_elemento()
