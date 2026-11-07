# Atividade 4 — Testes Automatizados do LocalEats

## 1. Identificação

- Turma ADS — 2026/2 (Noite), conforme as atividades anteriores.
- Modalidade individual.
- Integrante responsável Ivo Lucas de Lima Júnior.
- Data da última execução 07/11/2026.
- Repositório [IvoLucasLLJ/pbl-qualidade-software-2026-2](https://github.com/IvoLucasLLJ/pbl-qualidade-software-2026-2).
- Diretório de entrega [atividades/atividade-04](https://github.com/IvoLucasLLJ/pbl-qualidade-software-2026-2/tree/main/atividades/atividade-04), disponível remotamente após o envio.

Entrega organizada segundo o [modelo oficial da Atividade 4](https://github.com/lucianozanuz/pbl-qualidade-software-2026-2/blob/main/atividades/atividade-04/atividade-04-testes-automatizados.md). O escopo acordado contém uma função, três testes unitários e um teste funcional com exatamente duas assertions.

A pasta original `atividade 04 `, com espaço após `04`, foi movida para `atividade-04` depois de confirmar que o destino estava ausente. Os nove arquivos existentes, incluindo caches, foram preservados e comparados por SHA-256 imediatamente após o movimento. Os caches ficaram excluídos da seleção do Git pelo `.gitignore` local.

## 2. Integrantes e responsabilidades

Ivo Lucas de Lima Júnior é o responsável pelos quatro testes e pela revisão acadêmica da entrega. A implementação, a exploração e as execuções registradas foram realizadas com assistência do Codex.

| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
|---|---|---|---|---|
| TU01 | Ivo Lucas de Lima Júnior | Unitário | R$ 30 retorna `True` | `tests/test_regras_localeats.py::test_tu01_pedido_no_valor_minimo` |
| TU02 | Ivo Lucas de Lima Júnior | Unitário | R$ 29,99 retorna `False` | `tests/test_regras_localeats.py::test_tu02_pedido_abaixo_do_valor_minimo` |
| TU03 | Ivo Lucas de Lima Júnior | Unitário | R$ -1 gera `ValueError` | `tests/test_regras_localeats.py::test_tu03_pedido_com_valor_negativo` |
| TF01 | Ivo Lucas de Lima Júnior | Funcional | A aba Criar Conta apresenta campo de nome e botão Registrar | `tests/test_localeats.py::test_tf01_abrir_formulario_de_cadastro` |

## 3. Testes unitários

### Regra de Ivo Lucas de Lima Júnior

A regra escolhida é o valor mínimo do pedido. A função `pedido_atingiu_valor_minimo(valor_pedido)` está em [src/regras_localeats.py](src/regras_localeats.py). Ela recebe um valor numérico e primeiro rejeita negativos com `ValueError`. Para os demais valores, retorna o resultado da comparação `valor_pedido >= 30`.

| Entrada | Resultado esperado | Teste |
|---|---|---|
| `30` | `True` | TU01 |
| `29.99` | `False` | TU02 |
| `-1` | `ValueError` | TU03 |

Os três casos estão em [tests/test_regras_localeats.py](tests/test_regras_localeats.py). TU01 e TU02 conferem o booleano com `is True` e `is False`. TU03 verifica a exceção com `pytest.raises(ValueError)`. A função Python pertence ao exercício local. O teste funcional avalia separadamente a interface da aplicação hospedada.

## 4. Aplicação do TDD

### TDD de Ivo Lucas de Lima Júnior

A retomada encontrou `src/regras_localeats.py` vazio e apenas o teste de valor igual a 30. Seu nome original era `test_pedido_no_valor_minimo`. Ele recebeu o identificador TU01 no nome e no comentário, preservando a entrada e a verificação existentes.

As cinco execuções abaixo ocorreram nesta ordem, a partir de `atividades/atividade-04`, com o Python da `.venv` da raiz. A saída integral, incluindo o erro e a falha intermediária, foi mantida em [relatorio-tdd.txt](relatorio-tdd.txt).

| Execução | Estado antes da execução | Resultado real | Código de saída | Decisão seguinte |
|---|---|---|---|---|
| 1 | TU01 existente e módulo vazio | `0 items / 1 error`, `ImportError` durante a coleta | 2 | Definir a função com `return valor_pedido >= 30` |
| 2 | TU01 e implementação inicial | `1 passed` | 0 | Acrescentar TU02 antes de alterar a função |
| 3 | TU01 e TU02, mesma implementação | `2 passed` | 0 | Registrar que TU02 passou imediatamente e acrescentar TU03 |
| 4 | Três testes, ainda sem validação de negativos | `1 failed, 2 passed`, TU03 com `DID NOT RAISE ValueError` | 1 | Acrescentar a validação `valor_pedido < 0` e lançar `ValueError` |
| 5 | Três testes e validação de negativos | `3 passed` | 0 | Concluir a regra e seguir para a validação funcional |

Na primeira execução, o Python localizou o módulo, mas não encontrou a função importada. A coleta foi interrompida antes de executar a assertion do TU01. Na quarta execução, o TU03 foi coletado e executado, mas a verificação de exceção falhou porque a função retornava `False` para `-1`.

TU02 já passou ao ser acrescentado porque a comparação `>= 30` contemplava R$ 29,99. Esse caso teve aprovação imediata, sem etapa vermelha observada. O ciclo que exigiu mudança de comportamento foi TU03, com falha por ausência da exceção e aprovação após a validação. A revisão final manteve a implementação curta, sem necessidade de refatoração adicional.

Para reproduzir a execução unitária, comece na raiz do repositório e execute os comandos abaixo. O registro de TDD preserva os caminhos e as saídas originais das cinco execuções históricas.

```bash
source .venv/bin/activate
cd atividades/atividade-04
PYTHONDONTWRITEBYTECODE=1 python -m pytest -v -p no:cacheprovider tests/test_regras_localeats.py
```

## 5. Testes funcionais com Playwright

### Exploração e escolha do fluxo

O relatório da Atividade 1 documenta buscas por `italiana` e `Restaurante Sabor 0` retornando “Nenhum restaurante encontrado.” apesar da existência do restaurante na listagem. Também registra a busca por `xyzabc123` e a tentativa posterior com nome válido. Essas evidências motivaram a verificação de acesso à pesquisa antes da escolha do cenário. [Relatório da Atividade 1](../atividade-01/atividade-01-fundamentos-qualidade.md)

Na exploração de 07/11/2026, em um contexto novo do Chromium, o acesso à raiz redirecionou para `/static/login.html`. Clicar no link LocalEats, cujo destino era `index.html`, também terminou no login. A interface acessível apresentou as abas Entrar e Criar Conta. Ao clicar em Criar Conta, foram exibidos Nome Completo, o campo com placeholder `Seu nome`, E-mail, Senha e o botão Registrar. [Aplicação explorada](https://local-eats-unisenac.vercel.app/)

A pesquisa ficou condicionada à autenticação, conforme também previsto nas pré-condições da Atividade 3. Esta execução permite registrar a barreira de acesso atual. A situação dos falsos negativos históricos continua sem confirmação em uma sessão autenticada. O redirecionamento observado, isoladamente, é insuficiente para caracterizar um defeito da aplicação. [Pré-condições da Atividade 3](../atividade-03/atividade-03-estrategia-projeto-testes.md)

### TF01 de Ivo Lucas de Lima Júnior

O fluxo escolhido é abrir o formulário de cadastro pela aba Criar Conta. Ele é curto, funcionou na exploração e pode ser reproduzido em uma sessão nova. A cobertura fica restrita à apresentação do formulário após a interação. Cadastro efetivo, autenticação, persistência de dados e pesquisa exigem verificações próprias.

1. Acessar a raiz do LocalEats usando a fixture `page` do pytest-playwright.
2. Clicar no botão com papel `button` e nome exato `Criar Conta`.
3. Verificar com `expect(...).to_be_visible()` que o campo de placeholder exato `Seu nome` está visível.
4. Verificar com `expect(...).to_be_visible()` que o botão de nome exato `Registrar` está visível.

As etapas 3 e 4 são as duas assertions. Os locators foram definidos a partir dos elementos observados na interface real. A navegação aguarda `domcontentloaded`, o clique usa a espera automática de acionabilidade do Playwright e as assertions aguardam a visibilidade dos elementos. O código está em [tests/test_localeats.py](tests/test_localeats.py).

TF01 foi aprovado no Chromium. A execução depende de acesso à internet e da disponibilidade da aplicação externa. Uma falha futura deve ser examinada pela etapa e mensagem do pytest. Timeout de navegação exige verificar conectividade e disponibilidade. Falha de visibilidade exige conferir a interface e os locators antes de atribuir a causa à aplicação.

## 6. Resultado da execução

Em 07/11/2026, a execução conjunta coletou exatamente quatro testes. TU01, TU02, TU03 e TF01 foram aprovados, com zero falhas, zero erros e um aviso. O resultado final foi `4 passed, 1 warning in 2.25s`, com código de saída 0. A saída real está em [relatorio-pytest.txt](relatorio-pytest.txt).

O aviso `PytestRemovedIn10Warning` aponta para a fixture de sessão `base_url`. A inspeção do pacote instalado identificou essa fixture como método de instância em `pytest_playwright/pytest_playwright.py`. Trata-se de uma descontinuação na integração da dependência com o pytest. O aviso foi preservado no relatório e a execução terminou aprovada. A verificação `python -m pip check` retornou `No broken requirements found.`

### Ambiente e dependências

| Componente | Versão verificada |
|---|---|
| Sistema | Ubuntu 26.04.1 LTS |
| Python da `.venv` da raiz | 3.14.4 |
| pytest | 9.2.0 |
| pytest-playwright | 0.10.0 |
| playwright | 1.64.1 |
| Chromium executado pelo Playwright | 156.0.8078.4 |

As versões das três dependências diretas foram lidas do ambiente que executou os testes e fixadas em [requirements.txt](requirements.txt). A instalação do Chromium é feita separadamente pelo Playwright. A reprodução em outra máquina depende também das bibliotecas do sistema e das dependências transitivas resolvidas pelo pip.

### Comandos para Ubuntu com Bash

Comece na raiz do repositório para preparar as dependências usando a `.venv` existente.

```bash
source .venv/bin/activate
python -m pip install -r atividades/atividade-04/requirements.txt
python -m playwright install --with-deps chromium
python -m pip check
```

Em uma cópia nova do repositório, criar o ambiente com `python3 -m venv .venv` antes da ativação. O comando com `--with-deps` pode solicitar privilégios administrativos para instalar bibliotecas do Ubuntu. Na execução registrada, o ambiente e o Chromium já estavam disponíveis.

Comece novamente na raiz do repositório para executar os quatro testes desta entrega e regenerar o relatório com stdout e stderr. `pipefail` mantém a falha do pytest no status do comando mesmo com o uso de `tee`.

```bash
source .venv/bin/activate
cd atividades/atividade-04
set -o pipefail
PYTHONDONTWRITEBYTECODE=1 python -m pytest -v --tb=short -p no:cacheprovider --browser chromium tests 2>&1 | tee relatorio-pytest.txt
```

O diretório de trabalho permite importar `src.regras_localeats` e limita a coleta aos testes desta atividade. O registro de TDD mantém as saídas históricas das versões intermediárias. O relatório conjunto corresponde ao código final.

## 7. Explicações individuais

### Explicação do TU03 de Ivo Lucas de Lima Júnior

O teste `test_tu03_pedido_com_valor_negativo` verifica a rejeição de um pedido de valor negativo. A entrada é `-1`. O bloco `with pytest.raises(ValueError)` executa a chamada e exige que ela lance uma exceção desse tipo. Se a função apenas retornar `False`, o pytest informa `DID NOT RAISE ValueError`, como aconteceu na quarta execução do TDD. Uma exceção de tipo diferente também reprova o teste.

A função avalia o sinal antes de comparar com o mínimo. Assim, distingue a entrada negativa inválida de um pedido válido abaixo de R$ 30, que deve retornar `False`. TU01 cobre o limite inclusivo e TU02 cobre o valor imediatamente abaixo dele em centavos.

## 8. Uso de inteligência artificial

- ChatGPT foi utilizado no planejamento, para organizar o escopo e discutir a regra e os testes.
- Codex com GPT-6 Astra, raciocínio Extra alto, foi utilizado na execução assistida, incluindo inspeção local, organização da pasta, implementação progressiva, exploração com Playwright, execução dos testes e preparação da documentação.
- A sugestão anterior de implementar apenas `return valor_pedido >= 30` foi corrigida ao completar a regra. Essa expressão devolvia `False` para `-1` e precisava gerar `ValueError`. TU03 registrou a falha real, e a validação de negativos foi acrescentada antes da comparação.
- O código foi verificado pelas cinco execuções unitárias registradas, pela execução conjunta dos quatro testes, pela inspeção dos elementos reais da interface e pela conferência dos identificadores entre código, tabela e relatórios. As versões instaladas e a consistência das dependências também foram conferidas.

Esta entrega foi preparada para revisão de Ivo Lucas de Lima Júnior antes do envio ao GitHub. A explicação individual acima é material para essa revisão e para a demonstração de compreensão do código.

## 9. Diferenciais implementados

- [x] Terceiro teste unitário, cobrindo entrada negativa com TU03. [Código dos testes](tests/test_regras_localeats.py)
- [x] Uso de `pytest.raises` para verificar a exceção. [Código dos testes](tests/test_regras_localeats.py)
- [x] Registro de falha encontrada e corrigida, com `DID NOT RAISE ValueError` antes da validação. [Registro integral do TDD](relatorio-tdd.txt)

O terceiro teste amplia a cobertura para a classe de entrada inválida. As saídas preservadas permitem conferir a falha inicial de importação, a aprovação imediata de TU02 e a correção exigida por TU03.
