import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._choiceDDAeroportoD = None
        self._choiceDDAeroportoP = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        self._view._txt_result.controls.clear()  # cancello ciò che ho stampato con la chiamata precedente
        min = self._view.txt_min.value
        if min is None or min == "":
            self._view.create_alert("Inserire il minimo")
            return

        try:
            minInt = int(min)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un valore numerico!", color="red"))
            self._view.update_page()
            return

        if minInt < 0:
            self._view.create_alert("Inserire un numero positivo")

        self._model.build_graph(minInt)
        self._view.dd_AeroportoP.disabled = False
        self._view.btn_connessi.disabled = False
        self._view.dd_AeroportoD.disabled = False
        self._view.btn_cerca.disabled = False

        allNodes = self._model.getAllNodes()
        self.fillDD(allNodes)

        nNodes, nEdges = self._model.getGraphDetails()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato:"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di nodi:{nNodes}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di archi:{nEdges}"))

        self._view.update_page()


    def fillDD(self, allNodes):
        self._view.dd_AeroportoP.options.clear()
        self._view.dd_AeroportoD.options.clear()

        for n in allNodes:
            self._view.dd_AeroportoP.options.append(
                ft.dropdown.Option(data=n,
                                   key=n.IATA_CODE, on_click = self.leggiDdPartenza))
            self._view.dd_AeroportoD.options.append(
                ft.dropdown.Option(key=n.IATA_CODE, data=n, on_click = self.leggiDdArrivo))



    def leggiDdPartenza(self, e):
        self._choiceDDAeroportoP = e.control.data
        print("leggiDdPartenza called: ", self._choiceDDAeroportoP)
        
    def leggiDdArrivo(self, e):
        self._choiceDDAeroportoD = e.control.data
        print("leggiDdArrivo called: ", self._choiceDDAeroportoD)

    def handle_connessi(self, e):
        nodo = self._choiceDDAeroportoP
        if nodo is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Attenzione, selezionare una voce dal menù."))
            return

        viciniTuple = self._model.getSortedNeighbors(nodo)  # tupla nodo - peso
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"nodo di partenza: {nodo}"))
        self._view._txt_result.controls.append(ft.Text(f"nodi connessi in ordine decr di num di voli:"))

        for n in viciniTuple:
            self._view._txt_result.controls.append(ft.Text(f"nodo: {n[0]} - peso: {n[1]}"))

        self._view.update_page()




