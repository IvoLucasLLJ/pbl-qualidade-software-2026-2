# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Turma:** ADS — 2026/2 (Noite)  
**Equipe:** Individual  
**Data:** 22/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Ivo Lucas de Lima Jr. | @IvoLucasLLJ |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Verificar se a pesquisa de restaurantes do LocalEats retorna resultados corretos para diferentes tipos de entrada e se diferencia adequadamente termos válidos de termos sem correspondência, priorizando o risco de falsos negativos já observado na Atividade 1.

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Ivo Lucas de Lima Jr. | Pesquisar restaurantes por culinária ou localização | Se termos válidos localizam restaurantes existentes; se nomes exatos são encontrados; se termos inexistentes não produzem falsos positivos; e se uma nova busca pode ser realizada após um resultado vazio. |

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| Fazer pedido | O escopo foi mantido na pesquisa, que já possui evidências da Atividade 1. Isso permite aprofundar riscos, técnicas e rastreabilidade sem abrir uma nova funcionalidade que exigiria outro conjunto de regras. |

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Teste de sistema | A funcionalidade é avaliada pela interface da aplicação em funcionamento, sem acesso à implementação interna. |
| Tipos de teste | Funcional | O objetivo principal é verificar a correção do resultado da pesquisa. |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta | Os casos são projetados a partir de entradas e saídas observáveis. |
| Técnicas de teste | Particionamento de equivalência e transição de estados | O particionamento separa entradas válidas e sem correspondência; a transição de estados verifica a sequência “lista disponível -> sem resultados -> nova busca”. |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Navegador atualizado, acesso ao LocalEats e conta de usuário cadastrada. |
| Responsáveis pelo planejamento | Ivo Lucas de Lima Jr. |
| Responsáveis pela especificação dos casos | Ivo Lucas de Lima Jr. |
| Responsáveis pela futura execução | Ivo Lucas de Lima Jr. |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | Aplicação acessível, usuário autenticado, lista de restaurantes carregada e ao menos um nome/categoria existente previamente confirmado. |
| Saída | Todos os casos executados e registrados; riscos de prioridade Alta cobertos; divergências entre esperado e observado documentadas. |
| Suspensão | Indisponibilidade da aplicação, falha de autenticação ou ausência de carregamento dos dados necessários para definir uma entrada válida. |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | Ivo Lucas de Lima Jr. | Pesquisa de restaurantes | Um termo válido não retorna um restaurante existente ou uma categoria compatível. | O usuário acredita que a opção desejada não existe, precisa navegar manualmente e pode abandonar a tarefa. | Alta | Alto | Alta | O comportamento foi observado na Atividade 1 com `italiana` e `Restaurante Sabor 0`, apesar de o restaurante existir na lista. |
| R02 | Ivo Lucas de Lima Jr. | Pesquisa de restaurantes | Um termo sem correspondência pode retornar item incorreto ou não fornecer feedback adequado. | O usuário recebe informação enganosa ou não entende que não existem resultados. | Média | Médio | Média | A busca precisa distinguir corretamente ausência de correspondência de um resultado válido. No teste exploratório com `xyzabc123`, o sistema apresentou “Nenhum restaurante encontrado”, comportamento adequado para essa classe. |

### 3.2 Aplicação das técnicas

#### Análise 1

**Integrante:** Ivo Lucas de Lima Jr.  
**Funcionalidade:** Pesquisa de restaurantes  
**Risco relacionado:** R01  
**Técnica escolhida:** Particionamento de equivalência

**Por que a técnica foi escolhida:**  
A entrada da pesquisa pode ser organizada em classes com comportamento esperado semelhante. Isso permite selecionar representantes de cada classe em vez de testar todos os textos possíveis.

**Aplicação da técnica:**

| Classe de equivalência | Exemplo | Resultado esperado |
|---|---|---|
| Culinária existente | `italiana` | Apresentar restaurante(s) classificados como italianos. |
| Nome exato existente | `Restaurante Sabor 0` | Apresentar o restaurante correspondente. |
| Localização existente | `Zona Sul` | Apresentar restaurantes associados à localização, caso a busca realmente suporte localização conforme indicado na interface. |
| Termo sem correspondência | `xyzabc123` | Apresentar “Nenhum restaurante encontrado” ou feedback equivalente, sem falsos positivos. |

**Casos derivados:** CT01, CT02 e CT03.

#### Análise 2

**Integrante:** Ivo Lucas de Lima Jr.  
**Funcionalidade:** Pesquisa de restaurantes  
**Risco relacionado:** R01 e continuidade da operação  
**Técnica escolhida:** Transição de estados

**Por que a técnica foi escolhida:**  
A pesquisa altera o estado visível da lista. É relevante verificar se, depois de um estado “sem resultados”, uma nova pesquisa consegue substituir esse estado e apresentar resultados quando a entrada é válida.

**Aplicação da técnica:**

- **S0:** lista de restaurantes carregada.
- **S1:** pesquisa sem correspondência executada; mensagem “Nenhum restaurante encontrado”.
- **S2:** nova pesquisa válida executada; resultados correspondentes deveriam ser exibidos.

Transição projetada: `S0 -> termo inexistente -> S1 -> termo válido -> S2`.

**Observação:** na exploração da Atividade 1, o termo válido já falhou mesmo partindo de S0. Portanto, a repetição da falha após S1 não permite concluir, isoladamente, que exista um segundo defeito de transição de estado; o defeito de busca válido bloqueia essa interpretação.

**Caso derivado:** CT04.

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### CT01: Busca por culinária existente

**Integrante responsável:** Ivo Lucas de Lima Jr.  
**Funcionalidade:** Pesquisa de restaurantes  
**Risco ou requisito relacionado:** R01  
**Técnica utilizada:** Particionamento de equivalência

**Pré-condição:**  
Lista carregada e existência confirmada de pelo menos um restaurante classificado como `Italiana`.

**Dados de entrada:**  
`italiana`

**Passos:**
1. Abrir o LocalEats e autenticar-se.
2. Confirmar a existência de restaurante italiano na listagem.
3. Informar `italiana` no campo de pesquisa.
4. Clicar em `Buscar`.

**Resultado esperado:**  
Exibir ao menos o restaurante italiano previamente confirmado e não apresentar itens incompatíveis.

---

### CT02: Busca por nome exato de restaurante existente

**Integrante responsável:** Ivo Lucas de Lima Jr.  
**Funcionalidade:** Pesquisa de restaurantes  
**Risco ou requisito relacionado:** R01  
**Técnica utilizada:** Particionamento de equivalência

**Pré-condição:**  
O `Restaurante Sabor 0` está visível na listagem inicial.

**Dados de entrada:**  
`Restaurante Sabor 0`

**Passos:**
1. Confirmar o restaurante na lista.
2. Informar o nome exato no campo de pesquisa.
3. Clicar em `Buscar`.

**Resultado esperado:**  
Exibir o `Restaurante Sabor 0`.

---

### CT03: Busca por termo sem correspondência

**Integrante responsável:** Ivo Lucas de Lima Jr.  
**Funcionalidade:** Pesquisa de restaurantes  
**Risco ou requisito relacionado:** R02  
**Técnica utilizada:** Particionamento de equivalência

**Pré-condição:**  
Aplicação carregada na tela de pesquisa.

**Dados de entrada:**  
`xyzabc123`

**Passos:**
1. Informar `xyzabc123`.
2. Clicar em `Buscar`.
3. Observar a lista e a mensagem apresentada.

**Resultado esperado:**  
Não exibir restaurante não relacionado e informar que nenhum restaurante foi encontrado.

---

### CT04: Nova busca após um resultado sem correspondência

**Integrante responsável:** Ivo Lucas de Lima Jr.  
**Funcionalidade:** Pesquisa de restaurantes  
**Risco ou requisito relacionado:** R01 / continuidade da operação  
**Técnica utilizada:** Transição de estados

**Pré-condição:**  
Lista carregada; um termo válido previamente confirmado; aplicação no estado inicial S0.

**Dados de entrada:**  
Primeiro `xyzabc123`; depois `Restaurante Sabor 0`.

**Passos:**
1. Executar a busca por `xyzabc123` e chegar a S1.
2. Sem recarregar a página, substituir o termo por `Restaurante Sabor 0`.
3. Executar a nova busca.

**Resultado esperado:**  
Sair do estado “sem resultados” e exibir o restaurante correspondente ao termo válido.

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Ivo Lucas de Lima Jr. | Pesquisa de restaurantes | R01 — falso negativo para entrada válida | Particionamento de equivalência | CT01 e CT02 |
| Ivo Lucas de Lima Jr. | Pesquisa de restaurantes | R02 — tratamento de termo sem correspondência | Particionamento de equivalência | CT03 |
| Ivo Lucas de Lima Jr. | Pesquisa de restaurantes | Continuidade após resultado vazio / R01 | Transição de estados | CT04 |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
ChatGPT (OpenAI).

**Como foi utilizada:**  
Foi utilizada para estruturar o plano, relacionar os riscos às evidências da Atividade 1, selecionar técnicas de teste e organizar os casos e a matriz de rastreabilidade.

**Uma sugestão que precisou ser alterada ou rejeitada:**  
Foi considerada inicialmente a hipótese de classificar a falha após uma busca sem resultados como um defeito independente de transição de estados. Essa conclusão foi rejeitada porque o mesmo termo válido (`Restaurante Sabor 0`) já falha quando testado isoladamente. Assim, a evidência não permite separar um defeito de recuperação de estado do defeito geral da busca textual.

**Como as respostas foram verificadas:**  
Foi conferida a rastreabilidade `funcionalidade -> risco -> técnica -> caso de teste`, e os riscos foram comparados com as evidências reais coletadas na Atividade 1.
