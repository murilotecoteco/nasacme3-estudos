# 02 — Normalização, deduplicação e idempotência

`domain.py` separa regras puras da rede e do banco. Isso reduz o custo dos
testes e permite repetir o processamento com a mesma entrada.

## Exercícios

1. Troque a regra de `is_earth_directed` e escreva um teste para a nova regra.
2. Explique por que `activity_id` é usado para remover duplicatas.
3. Prove que rodar `prepare_fixture` duas vezes produz os mesmos dois eventos.
4. Simule uma análise sem latitude e longitude; o resultado deve ser `False`.
