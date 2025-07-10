import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._txt_result = None
        self.btn_cerca = None
        self.txt_maxTratte = None
        self.dd_AeroportoD = None
        self.btn_connessi = None
        self.dd_AeroportoP = None
        self.btn_analizza = None
        self.txt_min = None
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame Flight Delays", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW1
        # text field
        self.txt_min = ft.TextField(label="# compagnie minimo", width=300, hint_text="Inserire numero minimo di compagnie")

        # button analizza
        self.btn_analizza = ft.ElevatedButton(text="Analizza aeroporti", on_click=self._controller.handleCreaGrafo)

        # metto nella riga
        row1 = ft.Row([self.txt_min, self.btn_analizza], alignment=ft.MainAxisAlignment.CENTER)
        # aggiungo riga
        self._page.controls.append(row1)

        # ROW2
        # dropdown
        self.dd_AeroportoP = ft.Dropdown(label = "Aeroporto partenza", width=300, disabled = True)
        # button analizza
        self.btn_connessi = ft.ElevatedButton(text="Aeroporti connessi", disabled= True, on_click=self._controller.handle_connessi)

        # metto nella riga
        row2 = ft.Row([self.dd_AeroportoP, self.btn_connessi], alignment=ft.MainAxisAlignment.CENTER)
        # aggiungo riga
        self._page.controls.append(row2)

        # ROW3
        # dropdown
        self.dd_AeroportoD = ft.Dropdown(label="Aeroporto destinazione", width=300, disabled=True)
        # metto nella riga
        row3 = ft.Row([self.dd_AeroportoD], alignment=ft.MainAxisAlignment.CENTER)
        # aggiungo riga
        self._page.controls.append(row3)

        # ROW4
        # text field
        self.txt_maxTratte = ft.TextField(label="# tratte massimo", width=300, hint_text="Inserire numero massimo di tratte")

        # button analizza
        self.btn_cerca = ft.ElevatedButton(text="Cerca itinerario", on_click=self._controller.handleCreaGrafo, disabled=True)

        # metto nella riga
        row4 = ft.Row([self.txt_maxTratte, self.btn_cerca], alignment=ft.MainAxisAlignment.CENTER)
        # aggiungo riga
        self._page.controls.append(row4)


        # List View where the reply is printed
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self._txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
