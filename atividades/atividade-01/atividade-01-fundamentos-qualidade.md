# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Turma:** ADS — 2026/2 (Noite)  
**Equipe:** Individual  
**Data:** 22/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Ivo Lucas de Lima Jr. | @IvoLucasLLJ |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | Permitir que o usuário pesquise restaurantes por culinária ou localização, conforme indicado no campo de busca da aplicação. | Usuário. | O usuário precisa percorrer manualmente a lista e pode não encontrar uma opção adequada. |
| Explícita | Permitir que o usuário acesse os restaurantes disponíveis e consulte suas informações. | Usuário e restaurante. | O usuário não consegue escolher onde realizar sua interação/pedido e o restaurante perde visibilidade. |
| Implícita | A pesquisa deve retornar resultados coerentes com os restaurantes que realmente estão disponíveis na aplicação. | Usuário e restaurante. | A aplicação pode informar que não há resultados mesmo quando existem restaurantes compatíveis, reduzindo a confiança e dificultando a tarefa. |
| Implícita | Quando não existir correspondência, o sistema deve informar a ausência de resultados de forma compreensível, sem apresentar itens incorretos. | Usuário. | O usuário pode interpretar a resposta de forma errada ou não saber se a pesquisa foi executada corretamente. |

### 2.2 Questão sobre os fundamentos da qualidade

Sim. Um sistema pode implementar todas as funcionalidades solicitadas e ainda apresentar baixa qualidade se o resultado produzido não atender às necessidades do usuário. No LocalEats, o campo de pesquisa existe e pode ser acionado, porém um restaurante italiano visível na listagem não foi localizado pela pesquisa `italiana` nem pelo próprio nome. Assim, a função existe, mas não atende à necessidade implícita de retornar resultados corretos e coerentes.

---

## 3. Tarefa 2: Exploração da aplicação

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Ivo Lucas de Lima Jr. | Pesquisar restaurantes por culinária ou localização. | **Uso esperado:** após recarregar a página, confirmei que o `Restaurante Sabor 0` estava disponível e identificado como `Italiana` e `Zona Sul`. Pesquisei `italiana` e depois o nome exato `Restaurante Sabor 0`. **Uso alternativo:** pesquisei o termo inexistente `xyzabc123` e, sem recarregar, substituí pelo nome válido `Restaurante Sabor 0`. | A lista carregada comprovou a existência do `Restaurante Sabor 0` na categoria `Italiana`. Mesmo assim, tanto `italiana` quanto `Restaurante Sabor 0` retornaram **“Nenhum restaurante encontrado.”**. O termo inexistente também retornou a mesma mensagem, o que é adequado para uma entrada sem correspondência. Depois dessa busca, o nome válido continuou sem retornar resultado. A evidência permite afirmar que a busca textual apresenta falsos negativos; não permite afirmar a causa interna do defeito. | [Lista carregada](evidencias/e00-lista-carregada-restaurante-sabor-0-italiana.png); [busca `italiana`](evidencias/e01-busca-italiana-sem-resultado.png); [busca por nome exato](evidencias/e02-busca-restaurante-sabor-0-sem-resultado.png); [termo inexistente](evidencias/e03-busca-termo-inexistente.png); [nome válido após termo inexistente](evidencias/e04-busca-valida-apos-termo-inexistente.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Ivo Lucas de Lima Jr. | A pesquisa do LocalEats deve localizar os restaurantes existentes que correspondam ao nome, culinária ou localização informados e não deve retornar itens não relacionados. | Adequação funcional — **correção funcional**. | O problema observado não é a inexistência da função, e sim o resultado incorreto. O `Restaurante Sabor 0`, comprovadamente disponível e classificado como `Italiana`, não foi encontrado nem pelo nome exato nem pela culinária. | Definir um conjunto de buscas com nomes, culinárias e localizações previamente confirmados na listagem e comparar resultado esperado x observado. Contar falsos negativos e falsos positivos. Critério proposto: todos os restaurantes existentes usados no teste devem ser localizados por ao menos um dos atributos suportados pela busca, e nenhum termo inexistente deve retornar restaurante não relacionado. |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
ChatGPT (OpenAI).

**Como foi utilizada:**  
Foi utilizada para organizar o trabalho no template oficial, diferenciar necessidade explícita e implícita, formular o requisito de qualidade, relacionar o comportamento observado à correção funcional e estruturar a documentação das evidências.

**Como as respostas foram verificadas:**  
As afirmações sobre o comportamento do LocalEats foram verificadas manualmente no navegador. Primeiro foi confirmada a existência do `Restaurante Sabor 0`, identificado como `Italiana`; depois foram executadas as pesquisas `italiana`, `Restaurante Sabor 0` e `xyzabc123`. As capturas incluídas no repositório correspondem às execuções realizadas. Não foi inferida a causa interna da falha, pois não houve inspeção do código-fonte ou do banco de dados.
