from math import sqrt

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def AreaSign (self, a, b, c):
        area2 = ( b.x - a.x ) * ( c.y - a.y ) - ( c.x - a.x ) * ( b.y - a.y )
        if (area2 > 0.5): return 1
        elif (area2 < -0.5): return -1
        else: return 0

    def leftor (self, a, b, c):
        return self.AreaSign (a, b, c) > 0 or self.AreaSign (a, b, c) == 0
    def left (self, a, b, c):
        return self.AreaSign (a, b, c) > 0

    def listaleft (self, a, b, lista):
        for i in lista:
            if(self.AreaSign (a, b, i) > 0 ):
                return self.AreaSign (a, b, i) > 0
            else: return self.AreaSign (a, b, i) > 0

    def colinear (self, a, b, c):
        return self.AreaSign (a, b, c) == 0

    def distance(self, a, b):
        return sqrt((a.x-b.x)**2+(a.y-b.y)**2)

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

class Poligono:
    def __init__(self):
        self.lista=[]

    def anadir (self,p):
        self.lista.append (p)

    def __repr__ (self):
        l=""
        for i in self.lista:
            l+=str(i)
        return l

    def izqder (self):
        izq = Point(1000,0)
        der = Point(0,0)
        for i in self.lista:
            if (i.x<izq.x):
                izq = i

            if (i.x>der.x):
                der = i
        result = [ izq, der ]
        return result

    def distPL (self,a,b,p): #siendo la linea desde a hasta b y el punto p

        return abs ((p.y - a.y) * (b.x - a.x) - (b.y - a.y) * (p.x - a.x));


    def masLejos (self,poligono, a, b, listaTotal): #linea con los puntos a,b. fin sera el string que da resultado de todos los puntos mas lejanos
        listaaux=poligono
        dist=0
        punto = Point(0,0)
        for i in listaaux.lista:
            aux=poligono.distPL(a,b,i)
            ocho = punto.colinear(a,b,i)
            if(aux>dist):
                dist = aux
                punto = i
        print("recta: ", a, b, "a punto: ", punto)
        listaTotal.append(punto)
        #borrar puntos
        for j in listaaux.lista:
            paux = Point (0,0)
            uno = paux.leftor(a, b, j) #cambie left por leftor
            dos = paux.leftor(b, punto, j)
            tres = paux.leftor(punto, a, j)
            cuatro = paux.colinear(b, punto, j) #esto puede no ser necesario
            cinco = paux.colinear(a, b, j)
            if((uno and dos and tres) or cuatro or cinco):
                listaaux.lista.remove(j)
        if(punto in listaaux.lista):
            listaaux.lista.remove(punto)

        if(len(listaaux.lista) == 0):
            return
        poligono.masLejos(listaaux, b, punto, listaTotal)
            #last = masLejos(listaaux, a, punto, fin)
            #return fin
        #return
        return listaTotal

    def total (self):
        listaTotal = []
        res = self.izqder()
        izq = res[0]
        der = res[1]
        listaTotal.append(izq)
        listaTotal.append(der)
        self.lista.remove(izq)
        self.lista.remove(der)
        convex = self.masLejos(self, izq, der, listaTotal)
        return convex

    def pintar (self, lista):
        poli = []

        base = Point (0,0)
        base = lista[0]
        poli.append(base)
        lista.remove(base)
        longi = len(lista)

        while (longi > 0):
            distancia = 100000
            aux = base
            for i in lista:
                dist = i.distance(aux, i)

                if(dist < distancia and base.listaleft(aux, i, lista) != True):
                    distancia = dist
                    base = i
            lista.remove(base)
            if(len(poli)>2):
                if (base.colinear((poli[len(poli)-2]), aux, base) != True):
                    poli.append(base)
                else:
                    poli.remove(aux)
                    poli.append(base)
            else:
                poli.append(base)
            longi = len(lista)

        return poli
