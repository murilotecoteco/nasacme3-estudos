# Plano de implementação

## Etapa 1 — Base do ambiente

- consolidar `AGENTS.md`;
- manter os prompts do toolkit em `.github/prompts`;
- manter as quatro skills em `.github/skills`;
- criar a camada visual de acompanhamento;
- configurar testes Python e JavaScript.

## Etapa 2 — Persistência e contratos

- usar SQLite apenas para prática offline;
- manter o SQL PostgreSQL/Supabase como referência;
- testar upsert e auditoria;
- testar o contrato de RLS/GRANTs por inspeção automatizada.

## Etapa 3 — Aprendizagem adaptativa

- registrar sessão, tentativa e nível de assistência;
- selecionar tarefas pelo backlog;
- avaliar competências por evidências;
- criar desafios de transferência.

## Etapa 4 — Integração com a atividade

- mapear cada requisito do PDF para uma aula;
- criar perguntas de arguição;
- registrar decisões do endpoint NASA/CCMC;
- preparar checklist de evidências e backup.

## Validação

```bash
pytest -q
npm test
node --check js/api-client.js
python -m compileall -q src tests
```

Além dos comandos, uma sessão representativa deve provar que o agente sabe
rotear um pedido para `LEARNING MODE`, pedir hipótese e não entregar a solução
inteira antes da tentativa.
