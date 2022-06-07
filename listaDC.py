class NodoListaCir:
    def __init__(self, valor_):
        self.valor = valor_
        self.anterior = None
        self.siguiente = None

class ListaDC:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def insertar(self,valor_):
        nuevo=NodoListaCir(valor_)
        
        if (self.primero==None):
            self.primero=nuevo
        else:
            nuevo.anterior=self.ultimo
            self.ultimo.siguiente=nuevo
        self.ultimo=nuevo
        self.ultimo.siguiente=self.primero
        self.primero.anterior=self.ultimo

    def imprimir(self):
        print("Elementos de la lista  circular doblemente enlazada")
        aux=self.primero
        while(aux!=None):
            print(aux.valor)
            if (aux.siguiente==self.primero):
                return
            aux=aux.siguiente

    def buscar(self, objetivo):
        aux = self.primero
        while(aux != None):
            if(aux.valor == objetivo):
                print("anterior : ", aux.anterior.valor
                , " |actual   : ", aux.valor,
                "|siguiente: " ,aux.siguiente.valor)

#para evitar que entre en ciclo, al momente de que el siguiete sea el primero que se detenga
#y coloca el siguiente valor 
            if (aux.siguiente==self.primero):
                return
            aux=aux.siguiente