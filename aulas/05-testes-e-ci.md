# 05 — Testes e CI

Os testes são intencionalmente independentes de Supabase e NASA. Isso torna a
execução previsível e evita gastar rede para validar regras simples.

Exercícios:

1. Rode `pytest -q` antes de qualquer alteração.
2. Faça um teste falhar de propósito e leia a mensagem.
3. Corrija a regra e rode novamente.
4. Leia `.github/workflows/tests.yml` e identifique checkout, Python,
   dependências e comando de teste.
