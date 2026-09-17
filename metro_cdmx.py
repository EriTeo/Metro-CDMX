from collections import defaultdict, deque

class GrafoMetro:
    def __init__(self):
        # Usamos un diccionario de listas para la lista de adyacencia
        self.grafo = defaultdict(list)

    def agregar_arista(self, origen, destino):
        # Como el metro va en ambas direcciones, el grafo es no dirigido
        self.grafo[origen].append(destino)
        self.grafo[destino].append(origen)

    def agregar_linea(self, estaciones):
        # Conecta estaciones consecutivas de una línea
        for i in range(len(estaciones) - 1):
            self.agregar_arista(estaciones[i], estaciones[i+1])

    def bfs_ruta_corta(self, inicio, destino):
        """
        Búsqueda en Anchura (BFS).
        Garantiza la ruta más corta en grafos de costo unitario.
        Usa una Cola (Queue).
        """
        if inicio not in self.grafo or destino not in self.grafo:
            return None

        cola = deque([[inicio]])
        visitados = set([inicio])

        while cola:
            ruta = cola.popleft()
            nodo_actual = ruta[-1]

            if nodo_actual == destino:
                return ruta

            for vecino in self.grafo[nodo_actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(ruta + [vecino])
        return None

    def dfs_ruta_alternativa(self, inicio, destino):
        """
        Búsqueda en Profundidad (DFS).
        Encuentra una ruta, pero raramente es la más corta.
        Usa una Pila (Stack).
        """
        if inicio not in self.grafo or destino not in self.grafo:
            return None

        pila = [[inicio]]
        visitados = set([inicio])

        while pila:
            ruta = pila.pop()
            nodo_actual = ruta[-1]

            if nodo_actual == destino:
                return ruta

            for vecino in self.grafo[nodo_actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    pila.append(ruta + [vecino])
        return None

def construir_metro():
    metro = GrafoMetro()
    
    # Definimos las líneas principales necesarias para las rutas solicitadas
    # (Se incluyen las estaciones de las Líneas 1, 2, 3 y 5)
    
    linea_1 = ["Observatorio", "Tacubaya", "Juanacatlán", "Chapultepec", "Sevilla", 
               "Insurgentes", "Cuauhtémoc", "Balderas", "Salto del Agua", "Isabel la Católica", 
               "Pino Suárez", "Merced", "Candelaria", "San Lázaro", "Moctezuma", 
               "Balbuena", "Boulevard Puerto Aéreo", "Gómez Farías", "Zaragoza", "Pantitlan"]
               
    linea_2 = ["Cuatro Caminos", "Panteones", "Tacuba", "Cuitláhuac", "Popotla", 
               "Colegio Militar", "Normal", "San Cosme", "Revolución", "Hidalgo", 
               "Bellas Artes", "Allende", "Zócalo", "Pino Suárez", "San Antonio Abad", 
               "Chabacano", "Viaducto", "Xola", "Villa de Cortés", "Nativitas", 
               "Portales", "Ermita", "General Anaya", "Taxqueña"]
               
    linea_3 = ["Indios Verdes", "Deportivo 18 de Marzo", "Potrero", "La Raza", "Tlatelolco", 
               "Guerrero", "Hidalgo", "Juárez", "Balderas", "Niños Héroes", 
               "Hospital General", "Centro Médico", "Etiopía", "Eugenia", 
               "División del Norte", "Zapata", "Coyoacán", "Viveros", 
               "Miguel Ángel de Quevedo", "Copilco", "Universidad"]
               
    linea_5 = ["Politécnico", "Instituto del Petróleo", "Autobuses del Norte", "La Raza", 
               "Misterios", "Valle Gómez", "Consulado", "Eduardo Molina", "Aragón", 
               "Oceania", "Terminal Aérea", "Hangares", "Pantitlan"]

    # Agregamos las líneas al grafo
    metro.agregar_linea(linea_1)
    metro.agregar_linea(linea_2)
    metro.agregar_linea(linea_3)
    metro.agregar_linea(linea_5)

    return metro

def imprimir_resultados(metro, origen, destino):
    print(f"\n{'='*50}")
    print(f"Ruta: {origen} -> {destino}")
    print(f"{'='*50}")

    ruta_bfs = metro.bfs_ruta_corta(origen, destino)
    print("🚇 Resultado BFS (Ruta más corta / Costo Unitario):")
    if ruta_bfs:
        print(f"Total estaciones (Costo): {len(ruta_bfs) - 1}")
        print(" -> ".join(ruta_bfs))
    else:
        print("Ruta no encontrada.")

    print("\n🛤️  Resultado DFS (Ruta explorada en profundidad):")
    ruta_dfs = metro.dfs_ruta_alternativa(origen, destino)
    if ruta_dfs:
        print(f"Total estaciones (Costo): {len(ruta_dfs) - 1}")
        print(" -> ".join(ruta_dfs))
    else:
        print("Ruta no encontrada.")

if __name__ == "__main__":
    metro_cdmx = construir_metro()

    # 1. Cuatro Caminos -> Pantitlan
    imprimir_resultados(metro_cdmx, "Cuatro Caminos", "Pantitlan")

    # 2. Politécnico -> Taxqueña
    imprimir_resultados(metro_cdmx, "Politécnico", "Taxqueña")

    # 3. Zapata -> Oceania
    imprimir_resultados(metro_cdmx, "Zapata", "Oceania")  
