class Grafo:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(vertices)]
    
    def add_arestas(self,u,v):
        self.grafo[u-1].append(v-1)
    
    def mostra_grafo(self):
        for i in range(self.vertices):
            print("%d: "%(i+1),end=' ')
            for j in self.grafo[i]:
                print("%d -> "% (j+1), end=' ')
            print('')


grafo = Grafo(5)
grafo.add_arestas(1,2)
grafo.add_arestas(2,3)
grafo.add_arestas(5,3)
grafo.add_arestas(2,5)
grafo.add_arestas(4,1)

grafo.mostra_grafo()