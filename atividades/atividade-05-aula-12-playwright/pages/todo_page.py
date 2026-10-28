
from playwright.sync_api import Page


class TodoPage:
    URL = "https://demo.playwright.dev/todomvc/#/"

    def __init__(self, page: Page):
        self.page = page
        self.campo = page.get_by_role(
            "textbox", name="What needs to be done?"
        )
        self.tarefas = page.locator(".todo-list li")

    def abrir(self):
        self.page.goto(self.URL)

    def adicionar_tarefa(self, descricao):
        self.campo.fill(descricao)
        self.campo.press("Enter")

    def concluir_tarefa(self, descricao):
        tarefa = self.tarefas.filter(has_text=descricao)
        tarefa.get_by_label("Toggle Todo").check()

    def filtrar_ativas(self):
        self.page.get_by_role("link", name="Active").click()

    def localizar_tarefa(self, descricao):
        return self.tarefas.filter(has_text=descricao)

    def contador(self):
        return self.page.locator(".todo-count")
