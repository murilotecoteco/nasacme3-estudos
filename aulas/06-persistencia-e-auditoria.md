# 06 — Persistência, upsert e auditoria

Execute o pipeline com `--database work/study.db` e observe:

1. `cme_events` recebe eventos por `activity_id`;
2. uma segunda execução atualiza, em vez de duplicar;
3. `execucoes` registra lotes, erros e status.

Explique por que a chave natural torna a operação idempotente e como o banco
ajuda a observar uma execução que falhou.
