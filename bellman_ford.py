import math


class Graphe():

    def __init__(self, noeuds):
        self.matriceAdj = noeuds.copy()

    def Afficher(self, src, dist):
        print("les chemins les plus courts allant de ", src, " est : ")
        for noeud in range(len(self.matriceAdj)):
            print((noeud + 1), "\t", dist[noeud])

    def bellmanFord(self, src, ordre):

        dist = [math.inf] * len(self.matriceAdj)
        precedence = [-1] * len(self.matriceAdj)
        dist[src - 1] = 0
        precedence[src - 1] = src - 1
        relax = True

        iteration = 0

        while (iteration < len(self.matriceAdj) - 1) and relax == True:
            relax = False
            # relaxation des sommets
            for elm in ordre:
                # chaque element elm est un tuple (u,v)
                if (dist[elm[1] - 1] > dist[elm[0] - 1] + self.matriceAdj[elm[0] - 1][elm[1] - 1]):
                    dist[elm[1] - 1] = dist[elm[0] - 1] + self.matriceAdj[elm[0] - 1][elm[1] - 1]
                    precedence[elm[1] - 1] = elm[0] - 1
                    relax = True
            iteration += 1

        self.Afficher(src, dist)


# Test
# les sommets sont numérotés à partir de 1
matriceAdj = [[0, 6, 5, 5, 0, 0, 0],
              [0, 0, 0, 0, -1, 0, 0],
              [0, -2, 0, 0, 1, 0, 0],
              [0, 0, -2, 0, 0, -1, 0],
              [0, 0, 0, 0, 0, 0, 3],
              [0, 0, 0, 0, 0, 0, 3],
              [0, 0, 0, 0, 0, 0, 0]
              ]
ordre = [(1, 2), (1, 3), (1, 4), (3, 2), (2, 5),
         (3, 5), (4, 3), (4, 6), (6, 7), (5, 7)]
g = Graphe(matriceAdj)
g.bellmanFord(1, ordre)