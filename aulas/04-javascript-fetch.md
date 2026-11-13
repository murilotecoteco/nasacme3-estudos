# 04 — JavaScript e `fetch`

`js/api-client.js` mostra o consumo da mesma API sem depender de HTML, CSS ou
DOM. Compare:

- `requests.get(...)` versus `fetch(...)`;
- `response.raise_for_status()` versus `response.ok`;
- dicionário Python versus objeto JavaScript;
- exceções síncronas e Promises/`async`.

Exercício: injete uma função `fetchImpl` falsa e teste uma resposta 500 sem
fazer uma chamada de rede real.
