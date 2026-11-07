from playwright.sync_api import Page, expect


# TF01 — Responsável: Ivo Lucas de Lima Júnior
def test_tf01_abrir_formulario_de_cadastro(page: Page):
    page.goto("https://local-eats-unisenac.vercel.app/", wait_until="domcontentloaded")
    page.get_by_role("button", name="Criar Conta", exact=True).click()

    expect(page.get_by_placeholder("Seu nome", exact=True)).to_be_visible()
    expect(page.get_by_role("button", name="Registrar", exact=True)).to_be_visible()
