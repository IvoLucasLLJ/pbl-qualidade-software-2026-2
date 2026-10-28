from pathlib import Path

from playwright.sync_api import Page, expect
from pages.todo_page import TodoPage


def test_fluxo_tarefas_pom(page: Page) -> None:
    # Preparação
    todo = TodoPage(page)
    todo.abrir()

    # Criar duas tarefas
    todo.adicionar_tarefa("Estudar Playwright")
    todo.adicionar_tarefa("Revisar testes")

    expect(todo.tarefas).to_have_count(2)

    # Concluir a primeira tarefa
    todo.concluir_tarefa("Estudar Playwright")

    concluida = todo.localizar_tarefa(
        "Estudar Playwright"
    )
    expect(
        concluida.get_by_label("Toggle Todo")
    ).to_be_checked()

    # Aplicar o filtro Active
    todo.filtrar_ativas()

    # Verificar os resultados
    expect(
        todo.localizar_tarefa("Revisar testes")
    ).to_be_visible()

    expect(
        todo.localizar_tarefa("Estudar Playwright")
    ).to_have_count(0)

    expect(todo.tarefas).to_have_count(1)

    expect(todo.contador()).to_contain_text(
        "1 item left"
    )

    page.screenshot(path=str(Path(__file__).parent / "evidencias" / "resultado.png"), full_page=True)
