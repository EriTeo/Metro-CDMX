from collections import defaultdict, deque

class GrafoMetro:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_arista(self, origen, destino):
        self.grafo[origen].append(destino)
        self.grafo[destino].append(origen)

    def agregar_linea(self, estaciones):
        for i in range(len(estaciones) - 1):
            self.agregar_arista(estaciones[i], estaciones[i+1])

    def bfs_ruta_corta(self, inicio, destino):
        """Búsqueda en Anchura (Ruta más corta)"""
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
        """Búsqueda en Profundidad (Ruta profunda, no óptima)"""
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
    
    # 🚇 LAS 12 LÍNEAS DEL METRO DE LA CDMX
    
    linea_1 = ["Observatorio", "Tacubaya", "Juanacatlán", "Chapultepec", "Sevilla", 
               "Insurgentes", "Cuauhtémoc", "Balderas", "Salto del Agua", "Isabel la Católica", 
               "Pino Suárez", "Merced", "Candelaria", "San Lázaro", "Moctezuma", 
               "Balbuena", "Boulevard Puerto Aéreo", "Gómez Farías", "Zaragoza", "Pantitlán"]
               
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
               
    linea_4 = ["Martín Carrera", "Talismán", "Bondojito", "Consulado", "Canal del Norte", 
               "Morelos", "Candelaria", "Fray Servando", "Jamaica", "Santa Anita"]
               
    linea_5 = ["Politécnico", "Instituto del Petróleo", "Autobuses del Norte", "La Raza", 
               "Misterios", "Valle Gómez", "Consulado", "Eduardo Molina", "Aragón", 
               "Oceanía", "Terminal Aérea", "Hangares", "Pantitlán"]
               
    linea_6 = ["El Rosario", "Tezozómoc", "UAM-Azcapotzalco", "Ferrería", "Norte 45", 
               "Vallejo", "Instituto del Petróleo", "Lindavista", "Deportivo 18 de Marzo", 
               "La Villa-Basílica", "Martín Carrera"]
               
    linea_7 = ["El Rosario", "Aquiles Serdán", "Camarones", "Refinería", "Tacuba", 
               "San Joaquín", "Polanco", "Auditorio", "Constituyentes", "Tacubaya", 
               "San Pedro de los Pinos", "San Antonio", "Mixcoac", "Barranca del Muerto"]
               
    linea_8 = ["Garibaldi", "Bellas Artes", "San Juan de Letrán", "Salto del Agua", 
               "Doctores", "Obrera", "Chabacano", "La Viga", "Santa Anita", "Coyuya", 
               "Iztacalco", "Apatlaco", "Aculco", "Escuadrón 201", "Atlalilco", 
               "Iztapalapa", "Cerro de la Estrella", "UAM-I", "Constitución de 1917"]
               
    linea_9 = ["Tacubaya", "Patriotismo", "Chilpancingo", "Centro Médico", "Lázaro Cárdenas", 
               "Chabacano", "Jamaica", "Mixiuhca", "Velódromo", "Ciudad Deportiva", 
               "Puebla", "Pantitlán"]
               
    linea_A = ["Pantitlán", "Agrícola Oriental", "Canal de San Juan", "Tepalcates", 
               "Guelatao", "Peñón Viejo", "Acatitla", "Santa Marta", "Los Reyes", "La Paz"]
               
    linea_B = ["Buenavista", "Guerrero", "Garibaldi", "Lagunilla", "Tepito", "Morelos", 
               "San Lázaro", "Ricardo Flores Magón", "Romero Rubio", "Oceanía", 
               "Deportivo Oceanía", "Bosque de Aragón", "Villa de Aragón", "Nezahualcóyotl", 
               "Impulsora", "Río de los Remedios", "Múzquiz", "Ecatepec", "Olímpica", 
               "Plaza Aragón", "Ciudad Azteca"]
               
    linea_12 = ["Mixcoac", "Insurgentes Sur", "Hospital 20 de Noviembre", "Zapata", 
                "Parque de los Venados", "Eje Central", "Ermita", "Mexicaltzingo", 
                "Atlalilco", "Culhuacán", "San Andrés Tomatlán", "Lomas Estrella", 
                "Calle 11", "Periférico Oriente", "Tezonco", "Olivos", "Nopalera", 
                "Zapotitlán", "Tlaltenco", "Tláhuac"]

    # Agregamos todas las líneas al grafo
    for linea in [linea_1, linea_2, linea_3, linea_4, linea_5, linea_6, 
                  linea_7, linea_8, linea_9, linea_A, linea_B, linea_12]:
        metro.agregar_linea(linea)

    return metro

def imprimir_resultados(metro, origen, destino):
    print(f"\n{'='*60}")
    print(f"Ruta: {origen} -> {destino}")
    print(f"{'='*60}")

    ruta_bfs = metro.bfs_ruta_corta(origen, destino)
    print("🚇 Resultado BFS (Ruta más corta / Costo Unitario):")
    if ruta_bfs:
        print(f"Total estaciones (Costo): {len(ruta_bfs) - 1}")
        print(" -> ".join(ruta_bfs))
    else:
        print("Ruta no encontrada. (Verifica la ortografía de las estaciones)")

    print("\n🛤️  Resultado DFS (Ruta explorada en profundidad):")
    ruta_dfs = metro.dfs_ruta_alternativa(origen, destino)
    if ruta_dfs:
        print(f"Total estaciones (Costo): {len(ruta_dfs) - 1}")
        print(" -> ".join(ruta_dfs))
    else:
        print("Ruta no encontrada.")

if __name__ == "__main__":
    metro_cdmx = construir_metro()

    # 1. Cuatro Caminos -> Pantitlán
    imprimir_resultados(metro_cdmx, "Cuatro Caminos", "Pantitlán")

    # 2. Politécnico -> Taxqueña
    imprimir_resultados(metro_cdmx, "Politécnico", "Taxqueña")

    # 3. Zapata -> Oceanía
    imprimir_resultados(metro_cdmx, "Zapata", "Oceanía")
