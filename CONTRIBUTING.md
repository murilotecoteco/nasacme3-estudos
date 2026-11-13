# Contribuindo

## Fluxo

1. Escolha uma tarefa do [`docs/learning/BACKLOG.md`](docs/learning/BACKLOG.md).
2. Crie uma branch curta: `feat/cme-learn-001`, `fix/api-retry`,
   `docs/roadmap`, `test/storage` ou `chore/tooling`.
3. Faça uma mudança lógica por vez.
4. Rode `pytest -q`, `npm test` e as validações relevantes.
5. Verifique que nenhum secret foi incluído.
6. Registre a evidência da tarefa em `learning/` quando houver aprendizado.
7. Faça um commit seguindo `docs/learning/COMMIT_RULES.md`.
8. Revise o diff antes de abrir um pull request.

## Modos

O `LEARNING MODE` privilegia tentativa, hipótese e dicas graduais. O
`ENGINEERING MODE` permite implementação direta quando solicitada. O modo
utilizado deve aparecer na sessão ou no pedido de trabalho.

## Validação local

```bash
pytest -q
npm test
node --check js/api-client.js
python -m compileall -q src tests
```

## Origem do toolkit

Os workflows foram adaptados do Manware's AI Learning Toolkit para este
projeto, mantendo atribuição e o link de origem. A adaptação é específica para
Codex e GitHub Copilot e não substitui o código de produção do NASA CME.
