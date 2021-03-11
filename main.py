import queue

class Node:
    
    id = -1
    pai = None
    
    def __init__(self,id):
        self.id = id

class Grafo:
    
    matriz = []
    n = 0
    direcionado = False
    
    def __init__(self,n): 
        self.n = n
        for i in range(n):
            self.matriz.append([0]*n)            
    
    def addAresta(self,s,t):
        self.matriz[s][t]=1
        
    def printMatriz(self):
        print()
        print('-------------------')
        for i in range(self.n):
            # print("i",i)
            for j in range(self.n):
                # print("j",j)
                print(self.matriz[i][j],end = ' ')
            print()
        print('-------------------')
        print()

if __name__ == "__main__":

    g = Grafo(27)

    g.addAresta(0, 1)
    g.addAresta(1, 2)
    g.addAresta(1, 3)
    g.addAresta(1, 4)
    g.addAresta(2, 3)
    g.addAresta(3, 4)
    g.addAresta(4, 5)
    g.addAresta(5, 6)
    g.addAresta(6, 7)
    g.addAresta(5, 7)
    g.addAresta(4, 7)
    g.addAresta(7, 8)
    g.addAresta(8, 9)
    g.addAresta(7, 16)
    g.addAresta(8, 16)
    g.addAresta(9, 10)
    g.addAresta(9, 16)
    g.addAresta(16, 10)
    g.addAresta(10, 11)
    g.addAresta(11, 12)
    g.addAresta(12, 13)
    g.addAresta(11, 14)
    g.addAresta(10, 14)
    g.addAresta(16, 14)
    g.addAresta(16, 15)
    g.addAresta(15, 14)
    g.addAresta(15, 7)
    g.addAresta(18, 7)
    g.addAresta(18, 4)
    g.addAresta(17, 7)
    g.addAresta(18, 17)
    g.addAresta(18, 1)
    g.addAresta(15, 17)
    g.addAresta(18, 19)
    g.addAresta(19, 17)
    g.addAresta(19, 20)
    g.addAresta(17, 20)
    g.addAresta(20, 21)
    g.addAresta(20, 26)
    g.addAresta(20, 23)
    g.addAresta(20, 22)
    g.addAresta(23, 22)
    g.addAresta(22, 26)
    g.addAresta(22, 25)
    g.addAresta(22, 24)
    g.addAresta(24, 25)
    g.addAresta(25, 26)
    g.addAresta(26, 14)
    g.addAresta(26, 15)


    g.printMatriz()