# Backlog técnico e pedagógico

## CME-LEARN-001 — Reconstruir o fluxo do pipeline

- **Objetivo técnico:** rastrear API → normalização → deduplicação → lotes → auditoria.
- **Objetivo pedagógico:** construir um modelo mental antes de editar código.
- **Pré-requisitos:** ler `scripts/fetch_nasa.py` e `src/nasacme_estudos/pipeline.py`.
- **Dificuldade:** baixa.
- **Aceitação:** explicar oito etapas do fluxo e prever o resultado de um fixture.
- **Validação:** sessão `/read` e perguntas de previsão.

## CME-LEARN-002 — Normalizar payload incompleto

- **Objetivo técnico:** tratar campos ausentes sem quebrar o pipeline.
- **Objetivo pedagógico:** praticar contratos e valores opcionais.
- **Dependência:** 001.
- **Dificuldade:** baixa.
- **Aceitação:** teste para análise ausente, instrumento vazio e coordenadas ausentes.

## CME-LEARN-003 — Deduplicar por chave natural

- **Objetivo técnico:** impedir duplicatas antes do upsert.
- **Objetivo pedagógico:** entender idempotência.
- **Dependência:** 002.
- **Dificuldade:** baixa.
- **Aceitação:** explicar por que `activity_id` é obrigatório e testar repetição.

## CME-LEARN-004 — Projetar testes de API

- **Objetivo técnico:** testar sucesso, resposta vazia, HTTP 400, HTTP 503 e JSON inválido.
- **Objetivo pedagógico:** separar falha do cliente de falha do serviço externo.
- **Dependência:** 002.
- **Dificuldade:** média.
- **Aceitação:** testes com mock, sem rede real.

## CME-LEARN-005 — Explicar retry e backoff

- **Objetivo técnico:** reconhecer erros transitórios e não repetir erro permanente.
- **Objetivo pedagógico:** justificar decisões de confiabilidade.
- **Dependência:** 004.
- **Dificuldade:** média.
- **Aceitação:** defender a estratégia em uma pergunta de banca.

## CME-LEARN-006 — Implementar upsert local

- **Objetivo técnico:** persistir eventos e atualizar registros existentes.
- **Objetivo pedagógico:** relacionar chave natural e idempotência.
- **Dependência:** 003.
- **Dificuldade:** média.
- **Aceitação:** duas execuções deixam a mesma quantidade de eventos.

## CME-LEARN-007 — Ler RLS e GRANTs

- **Objetivo técnico:** identificar operações de `anon`, `authenticated` e `service_role`.
- **Objetivo pedagógico:** raciocinar sobre autorização por operação.
- **Dependência:** 006.
- **Dificuldade:** média.
- **Aceitação:** explicar `USING`, `WITH CHECK` e o risco de policy permissiva.

## CME-LEARN-008 — Ler um workflow

- **Objetivo técnico:** entender cron, manual, permissions, concurrency e timeout.
- **Objetivo pedagógico:** relacionar automação e confiabilidade.
- **Dependência:** 005.
- **Dificuldade:** média.
- **Aceitação:** explicar o que acontece em uma execução agendada.

## CME-LEARN-009 — Revisão de segurança

- **Objetivo técnico:** localizar exposição de secret e uso incorreto de dados externos.
- **Objetivo pedagógico:** desenvolver revisão crítica.
- **Dependência:** 007, 008.
- **Dificuldade:** média.
- **Aceitação:** produzir uma revisão classificada por severidade.

## CME-LEARN-010 — Ensaio técnico

- **Objetivo técnico:** defender arquitetura, API, banco, workflow e painel.
- **Objetivo pedagógico:** transferir compreensão para comunicação oral.
- **Dependência:** 001-009.
- **Dificuldade:** alta.
- **Aceitação:** responder perguntas novas sem ler o código durante a resposta.

## CME-LEARN-011 — Explicar o workflow e os secrets

- **Objetivo técnico:** relacionar triggers, permissions, concurrency, timeout e secrets.
- **Objetivo pedagógico:** compreender automação sem decorar YAML.
- **Dependência:** 005, 008.
- **Dificuldade:** média.
- **Aceitação:** explicar uma execução manual e uma agendada.

## CME-LEARN-012 — Validar contratos de integração

- **Objetivo técnico:** testar contratos de API, SQL e persistência offline.
- **Objetivo pedagógico:** aprender a testar dependências sem depender do serviço real.
- **Dependência:** 004, 006, 007.
- **Dificuldade:** média.
- **Aceitação:** todos os testes passam sem rede ou credenciais.

## CME-LEARN-013 — Separar responsabilidades

- **Objetivo técnico:** identificar limites entre API, domínio, pipeline e storage.
- **Objetivo pedagógico:** praticar modularização e arquitetura.
- **Dependência:** 001-012.
- **Dificuldade:** alta.
- **Aceitação:** defender uma mudança de módulo e seus contratos.

## CME-LEARN-014 — Refatorar com regressão controlada

- **Objetivo técnico:** fazer uma refatoração pequena preservando comportamento.
- **Objetivo pedagógico:** distinguir melhoria real de preferência estética.
- **Dependência:** 013.
- **Dificuldade:** alta.
- **Aceitação:** testes antes/depois e explicação do trade-off.

## CME-LEARN-015 — Revisar segurança do sistema

- **Objetivo técnico:** revisar secrets, escape, RLS, GRANTs e logs.
- **Objetivo pedagógico:** priorizar risco objetivo.
- **Dependência:** 007, 011.
- **Dificuldade:** alta.
- **Aceitação:** revisão classificada com evidências e correções propostas.

## CME-LEARN-016 — Avaliação prática

- **Objetivo técnico:** resolver uma tarefa nova usando conceitos já estudados.
- **Objetivo pedagógico:** medir implementação, debugging e testes sem assistência excessiva.
- **Dependência:** 001-015.
- **Dificuldade:** alta.
- **Aceitação:** solução, testes e justificativas independentes.

## CME-LEARN-017 — Transferência para outra API

- **Objetivo técnico:** aplicar normalização, retry e idempotência em outro domínio.
- **Objetivo pedagógico:** provar compreensão generalizável.
- **Dependência:** 016.
- **Dificuldade:** alta.
- **Aceitação:** explicar analogias, limites e diferenças.

## CME-LEARN-018 — Defesa do projeto

- **Objetivo técnico:** apresentar fluxo, decisões, evidências e limitações.
- **Objetivo pedagógico:** comunicar Engenharia de Software com clareza.
- **Dependência:** 016, 017.
- **Dificuldade:** alta.
- **Aceitação:** responder perguntas novas em até 10 minutos de arguição.
