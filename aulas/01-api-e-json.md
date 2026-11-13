# 01 — API, HTTP e JSON

O arquivo `fixtures/cme.json` representa a resposta da NASA. A atividade é
seguir o caminho de um registro até `normalize_event`.

## Exercícios

1. Identifique método HTTP, URL, parâmetros, status e corpo da requisição.
2. Adicione um evento sem `cmeAnalyses` ao fixture e rode `pytest`.
3. Explique por que timeout é obrigatório em uma aplicação automatizada.
4. No `api.py`, observe que `raise_for_status()` transforma HTTP 4xx/5xx em erro.

Resposta esperada: o programa não deve quebrar só porque a API omitiu um
campo opcional; ele deve representar a ausência como `None`.
