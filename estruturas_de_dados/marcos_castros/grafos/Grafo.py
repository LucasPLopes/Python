# Matriz de adjacência 
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*vertices for i in range(vertices)]
        # print(self.grafo) para teste de criação

    def add_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1
        self.grafo[v-1][u-1] = 1

    def mostrar_grafo(self):
        for i in self.grafo:
            for j in i:
                print(j, end=" ")
            print('')

    def ha_ligacao(self,u,v):
        if self.grafo[u -1 ][v -1] == 1:
            return True
        else:
            return False

# """
g = Grafo(5)
g.add_aresta(1,3)
g.add_aresta(3,4)
g.add_aresta(2,3)
g.add_aresta(3,5)
g.add_aresta(4,5)

g.mostrar_grafo()

# 0 0 1 0 0 
# 0 0 1 0 0 
# 1 1 0 1 1 
# 0 0 1 0 0 
# 0 0 1 0 0 
# 

print(g.ha_ligacao(3,1))