# Preparação para a apresentação

## Roteiro de 20 minutos

1. **API — 6 min:** o que é CME, o que a API fornece e por que os dados são relevantes.
2. **Arquitetura — 4 min:** API → Actions → Supabase → Pages.
3. **Demonstração — 8 min:** workflow, banco, endpoint REST, painel e filtro.
4. **IA — 2 min:** onde ajudou, onde errou e o que foi corrigido.

## Perguntas obrigatórias

- Qual é a chave natural do evento?
- Por que existe deduplicação antes do upsert?
- O que diferencia `anon` de `service_role`?
- Por que o secret não pode aparecer no frontend?
- O que acontece em uma falha parcial?
- O que `concurrency` evita?
- Por que o painel pode usar uma chave pública?
- Como a última execução chega à interface?
- Como o projeto evita inserir dados externos sem escape?
- Por que um HTTP 204 não prova que uma escrita alterou linhas?

## Evidências para conferir

- organização e repositório corretos;
- workflow verde;
- dados reais em `cme_events`;
- registro em `execucoes`;
- endpoint REST retornando JSON;
- painel publicado com filtro e última atualização;
- tutorial, apresentação, reflexão e registro de IA;
- backup local de prints ou gravação.
