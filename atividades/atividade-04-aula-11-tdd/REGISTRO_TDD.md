# Registro de TDD — Aula 11

Disciplina: Qualidade de Software
Atividade: Sábado Acadêmico de 24/10/2026
Ferramentas: Python 3.13.13 e pytest 9.1.1
Ambiente: Android / Termux

## Objetivo

Implementar a função calcular_taxa_entrega utilizando
Test-Driven Development (TDD), seguindo o ciclo
Red → Green → Refactor.

## Ciclo 1 — Taxa básica

Cenário: 2 km, pedido de R$ 50, taxa esperada de R$ 5.

RED:
Criado o teste test_taxa_entrega_ate_tres_km.
O teste falhou com ImportError, pois a função
calcular_taxa_entrega ainda não existia.
Resultado: 4 aprovados e 1 reprovado.

GREEN:
Criada a função retornando inicialmente o valor 5.
Resultado: 5 testes aprovados.

## Ciclo 2 — Quilômetros excedentes

Cenário: 4 km, pedido de R$ 50, taxa esperada de R$ 7.

RED:
Criado o teste test_taxa_entrega_acima_de_tres_km.
A função retornou 5, mas o teste esperava 7.
Resultado: 5 aprovados e 1 reprovado.

GREEN:
Implementado o acréscimo de R$ 2 por quilômetro
acima dos primeiros 3 km.
Resultado: 6 testes aprovados.

## Ciclo 3 — Entrega gratuita

Cenário: 5 km, pedido de R$ 100, taxa esperada de R$ 0.

RED:
Criado o teste test_entrega_gratuita_pedido_cem_reais.
A função retornou 9, mas o teste esperava 0.
Resultado: 6 aprovados e 1 reprovado.

GREEN:
Implementada a condição de gratuidade para pedidos
com valor maior ou igual a R$ 100.
Resultado: 7 testes aprovados.

## Refactor — Melhoria do código

A implementação foi simplificada utilizando:

km_excedentes = max(0, distancia_km - 3)

Essa alteração eliminou uma condição desnecessária
sem modificar os resultados da função.

Após a refatoração, todos os sete testes passaram.

## Conclusão

Foram implementados os três cenários obrigatórios,
preservando os quatro testes originais do projeto.

O exercício demonstrou o desenvolvimento incremental
orientado por testes e a importância da regressão
para verificar a preservação dos comportamentos.

Resultado final: 7 testes aprovados, nenhuma falha.
