# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Turma:** ADS — 2026/2 (Noite)  
**Equipe:** Individual  
**Data:** 22/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Ivo Lucas de Lima Jr. | @IvoLucasLLJ |

**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Não está claramente definido quem possui a responsabilidade final de aprovar a disponibilização de uma versão. | Uma versão pode ser liberada sem aceitação explícita dos riscos ou pode atrasar porque diferentes papéis esperam que outra pessoa decida. |
| A qualidade pode ser tratada como responsabilidade exclusiva do profissional de QA. | Defeitos simples são detectados apenas no fim do processo, aumentando retrabalho e sobrecarregando o QA. |
| Defeitos identificados podem não ser registrados e acompanhados de forma padronizada. | Problemas podem ser esquecidos, reaparecer ou ser corrigidos sem que a equipe consiga rastrear prioridade, responsável e validação. |

### 2.2 Responsabilidade pela qualidade

A qualidade do LocalEats não deve ser responsabilidade exclusiva do QA. O responsável pelo produto define necessidades e critérios de aceitação; o desenvolvedor implementa e testa o próprio código; o QA planeja os testes, analisa riscos e registra defeitos; e a liderança técnica participa das revisões e da decisão de liberação. A qualidade é compartilhada porque decisões capazes de prevenir ou introduzir defeitos acontecem durante todo o desenvolvimento, e não apenas na etapa final de testes.

---

## 3. Tarefa 2: Papéis e competências

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Ivo Lucas de Lima Jr. | Responsável pelo produto (Product Owner) | Esclarecer necessidades, definir critérios de aceitação, priorizar correções e avaliar se a entrega atende ao valor esperado. | Levantamento e priorização de requisitos, critérios de aceitação, gestão de backlog e conhecimento do domínio. | Comunicação, negociação, escuta ativa, organização e capacidade de decisão. |
| Ivo Lucas de Lima Jr. | Desenvolvedor | Implementar funcionalidades, criar testes unitários, corrigir defeitos e participar da revisão de código. | Programação, depuração, testes unitários, Git, APIs e revisão de código. | Atenção a detalhes, colaboração, responsabilidade, pensamento crítico e abertura a feedback. |
| Ivo Lucas de Lima Jr. | QA / Analista de Qualidade | Planejar e executar testes do sistema, analisar riscos, elaborar casos, registrar defeitos e acompanhar correções. | Técnicas de teste, testes funcionais e exploratórios, rastreabilidade, evidências e gestão de defeitos. | Curiosidade, organização, comunicação objetiva, imparcialidade e persistência investigativa. |
| Ivo Lucas de Lima Jr. | Liderança técnica | Definir padrões técnicos, revisar código, avaliar riscos técnicos e apoiar a decisão de disponibilização. | Arquitetura, integração contínua, revisão de código, estratégia de testes e gestão de riscos técnicos. | Liderança, mediação, visão sistêmica, orientação e tomada de decisão. |

---

## 4. Tarefa 3: Matriz de responsabilidades

**Legenda:** R = responsável por executar; A = aprovador/responsável final; C = consultado; I = informado.

| Atividade de qualidade | Produto | Desenvolvedor | QA | Liderança técnica |
|---|:---:|:---:|:---:|:---:|
| Definir critérios de aceitação | R/A | C | C | I |
| Revisar requisitos | A | C | R | C |
| Implementar a funcionalidade | I | R/A | C | C |
| Revisar o código | I | R | I | A |
| Criar testes unitários | I | R/A | C | I |
| Planejar e executar testes do sistema | C | C | R/A | I |
| Registrar e acompanhar defeitos | I | C | R/A | I |
| Priorizar a correção dos defeitos | A | C | C | R |
| Aprovar a disponibilização da versão | A | I | C | R |

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**  
A aprovação da disponibilização pode ficar difusa quando Produto, QA e Liderança Técnica entendem que outro papel é o responsável final.

**Consequência:**  
A versão pode ser liberada sem que os riscos estejam explicitamente aceitos ou a entrega pode ficar bloqueada por falta de decisão.

Na matriz proposta, Produto recebe **A** na disponibilização, Liderança Técnica recebe **R**, QA é **C** e Desenvolvimento é **I**. Dessa forma existe um único aprovador final e a decisão considera evidências técnicas e necessidades de negócio.

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Definition of Done contendo critérios de aceitação, revisão de código, testes unitários, testes de sistema relevantes e situação dos defeitos conhecidos. | Falta de clareza sobre quando uma funcionalidade está realmente pronta. | Produto, Desenvolvedor, QA e Liderança Técnica. |
| Triagem periódica de defeitos em um quadro único, registrando evidência, severidade, prioridade, responsável e situação. | Defeitos esquecidos, duplicados ou sem prioridade e acompanhamento. | QA, Produto, Desenvolvedor e Liderança Técnica. |
| Pull Request com revisão obrigatória antes do merge. | Reduz a concentração da validação no próprio autor da alteração e detecta problemas antes da integração. | Desenvolvedor e Liderança Técnica. |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
ChatGPT (OpenAI).

**Como foi utilizada:**  
Foi utilizada para organizar os papéis e competências, revisar a coerência da matriz RACI e relacionar as práticas de QA aos problemas organizacionais identificados.

**Como as respostas foram verificadas:**  
Foi conferido se as responsabilidades não ficaram concentradas exclusivamente no QA, se as atividades possuem responsáveis claros e se as práticas propostas respondem diretamente aos problemas descritos na Tarefa 1.
