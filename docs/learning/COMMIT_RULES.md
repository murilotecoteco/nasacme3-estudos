# Regras de commits

## Formato

Use Conventional Commits, em inglês, no modo imperativo:

```text
<type>(<scope>): <short imperative description>
```

Tipos permitidos: `feat`, `fix`, `docs`, `test`, `refactor`, `ci`, `build`,
`chore`, `perf` e `style`.

Exemplos:

```text
feat(pipeline): add local execution audit
test(api): cover retryable HTTP failures
docs(learning): define the study roadmap
ci(workflow): run Python and JavaScript tests
```

## Regras

- Uma mudança lógica por commit.
- Não misturar refatoração cosmética com mudança de comportamento.
- Não incluir secrets, tokens, `.env`, bancos locais ou artefatos de build.
- Rodar testes antes do commit.
- Usar escopo curto e reconhecível.
- Não reescrever commits publicados sem autorização.
- Commits de aprendizagem podem alterar apenas exercícios, testes e registros
  correspondentes.
- Commits de implementação devem registrar a validação executada.
- Push exige autorização explícita.

## Validação automática

O hook `.githooks/commit-msg` valida o formato. Ative-o uma vez:

```bash
git config core.hooksPath .githooks
```
