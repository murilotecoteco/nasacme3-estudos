# Roadmap técnico e pedagógico

O roadmap desenvolve conhecimento enquanto o ambiente e o NASA CME evoluem.
HTML/CSS são mantidos pelo agente; os demais tópicos são estudados por meio de
tentativas, testes e explicações.

## Fases

| Fase | Tarefas | Dependência | Resultado |
|---|---|---|---|
| 0. Orientação | `CME-LEARN-001` | nenhuma | fluxo do pipeline explicado |
| 1. Dados | `002-004` | 001 | API, JSON, normalização e deduplicação |
| 2. Confiabilidade | `005-007` | 002 | retry, timeout, erros e testes |
| 3. Persistência | `008-010` | 003 | SQL, upsert, RLS e auditoria |
| 4. Automação | `011-012` | 005, 008 | Actions, secrets e CI |
| 5. Arquitetura | `013-015` | fases 1-4 | contratos, refatoração e revisão |
| 6. Apresentação | `016-018` | todas | defesa técnica e transferência |

## Ordem de dificuldade

Comece com leitura e previsão. Depois escreva testes, implemente pequenas
funções, integre componentes e finalmente defenda decisões em cenários novos.
O nível de assistência deve cair quando houver evidência de independência.

## Critérios de conclusão

Uma tarefa só é concluída quando:

1. o comportamento esperado está escrito;
2. o estudante tentou ou explicou a solução;
3. os testes relevantes passam;
4. há uma explicação própria com exemplo e limite;
5. a evidência foi registrada na sessão.
