# 07 — Segurança, RLS e secrets

Compare `sql/01_schema.sql` com o `sql/setup.sql` do projeto original.

Exercícios:

1. Identifique o que `anon` pode ler.
2. Identifique o que `service_role` pode fazer.
3. Explique por que a chave privilegiada não pode ir para o frontend.
4. Explique a diferença entre `USING` e `WITH CHECK`.
5. Escreva um cenário em que uma policy permissiva cause exposição.
