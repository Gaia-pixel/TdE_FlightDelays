import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self.airports = DAO.getAllAirports()  # oggetti Aeroporto
        self.idmapAirports = {}
        for a in self.airports:
            self.idmapAirports[a.ID] = a  # chiave ID valore oggetto Aeroporto
    
    def build_graph(self, min):
        self._graph.clear()

        # aggiungo i nodi
        nodes = DAO.getAllNodes(min, self.idmapAirports)
        self._graph.add_nodes_from(nodes)

        # aggiungo gli archi
        self.getAllArchi()

    def getAllArchi(self):
        allArchi = DAO.getAllEdges(self.idmapAirports)
        for e in allArchi:
            if e.aeroportoP in self._graph and e.aeroportoD in self._graph:
                if self._graph.has_edge(e.aeroportoP, e.aeroportoD):
                    self._graph[e.aeroportoP][e.aeroportoD]["weight"] += e.peso
                else:
                    self._graph.add_edge(e.aeroportoP, e.aeroportoD, weight=e.peso)


    def getAllNodes(self):
        nodes = list(self._graph.nodes)
        nodes.sort(key=lambda x: x.IATA_CODE)
        return nodes

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getSortedNeighbors(self, nodo):
        # restituisco una lista di tuple con nodo - peso arco
        viciniNodo = self._graph.neighbors(nodo)
        tupleVicini = []
        for v in viciniNodo:
            tupleVicini.append((v, self._graph[nodo][v]["weight"]))
        tupleVicini.sort(key=lambda x: x[1], reverse=True)
        return tupleVicini




