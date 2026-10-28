from playwright.sync_api import Page, expect


def test_fluxo_tarefas(page: Page) -> None:

    # Abrir a aplicação
    page.goto("https://demo.playwright.dev/todomvc/#/")

    # Criar duas tarefas
    campo = page.get_by_role(
        "textbox", name="What needs to be done?"
    )

    campo.fill("Estudar Playwright")
    campo.press("Enter")

    campo.fill("Revisar testes")
    campo.press("Enter")

    # Verificar as duas tarefas
    tarefas = page.locator(".todo-list li")
    expect(tarefas).to_have_count(2)

    # Concluir a primeira tarefa
    concluida = tarefas.filter(
        has_text="Estudar Playwright"
    )

    concluida.get_by_label("Toggle Todo").check()

    expect(
        concluida.get_by_label("Toggle Todo")
    ).to_be_checked()

    # Filtrar tarefas ativas
    page.get_by_role("link", name="Active").click()

    # Verificar a tarefa pendente
    pendente = tarefas.filter(
        has_text="Revisar testes"
    )

    expect(pendente).to_be_visible()

    # A concluída não deve aparecer no filtro
    expect(concluida).to_have_count(0)

    # Apenas uma tarefa deve estar visível
    expect(tarefas).to_have_count(1)

    # Verificar o contador
    expect(
        page.locator(".todo-count")
    ).to_contain_text("1 item left")