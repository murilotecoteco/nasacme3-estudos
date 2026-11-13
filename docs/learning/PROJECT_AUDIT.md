# Auditoria do ambiente de aprendizagem

Data da linha de base: 2026-11-12.

## Escopo

Esta auditoria compara o projeto original NASA CME com o ambiente
`nasacme3-estudos`. O HTML e o
CSS pertencem à camada visual do ambiente, mas não são foco da trilha.

## Projeto original

### Estrutura observada

- `index.html` e `style.css`: painel estático publicado no GitHub Pages;
- `script.js`: consulta REST do Supabase, normalização visual, filtros,
  estatísticas, gráfico Canvas e modal;
- `scripts/fetch_nasa.py`: coleta, retry, normalização, deduplicação, upsert,
  lotes, auditoria e códigos de saída;
- `sql/setup.sql` e `supabase/migrations/001_create_tables.sql`: tabelas,
  índices, trigger, RLS, policies e GRANTs;
- `.github/workflows/update-data.yml`: cron, execução manual, permissions,
  concurrency e timeout;
- `docs/`: tutorial, apresentação, diagnóstico, interação com IA e reflexão.

### Pontos fortes

- Fluxo de dados completo entre API, Actions, Supabase e Pages;
- chave natural `activity_id` e upsert idempotente;
- separação entre chave pública e `service_role`;
- escape de valores externos antes de usar `innerHTML`;
- registro de métricas e estados `concluido`, `erro_parcial` e `erro_critico`;
- documentação operacional e histórico real de decisões.

### Limitações educacionais

- não há suíte de testes automatizados no projeto original;
- o frontend concentra responsabilidades em um arquivo grande;
- o pipeline mistura orquestração, rede e persistência;
- o retry não é demonstrado com backoff e testes isolados;
- o schema externo da API não possui validação formal;
- o funcionamento real depende de NASA, Supabase, GitHub e Pages;
- `docs/reflexao.md` ainda precisa receber reflexão real do grupo.

## Ambiente de estudos

O ambiente adiciona:

- fixture offline;
- funções puras para normalização e deduplicação;
- cliente HTTP testável;
- persistência SQLite local com upsert;
- registro de execuções;
- testes Python, JavaScript e contrato SQL;
- painel de acompanhamento;
- workflows de aprendizagem, sessões e avaliações;
- regras de commit e CI.

## Limitações conhecidas

- SQLite simula a persistência local; a integração real continua sendo
  Supabase/PostgreSQL no projeto original;
- os prompts não criam uma nova capacidade de slash command no Codex quando a
  interface não oferece esse recurso; nesse caso o nome do workflow deve ser
  escrito na mensagem;
- a medição de competência depende de evidências registradas, não de uma
  pontuação automática;
- nenhuma experiência anterior é considerada concluída sem evidência.

## Critério de sucesso da integração

O ambiente será considerado pronto quando os testes passarem, os dois agentes
forem instruídos, os workflows forem localizáveis, o backlog tiver tarefas
executáveis, a memória puder ser recuperada e a atividade do PDF estiver
mapeada para exercícios e perguntas de apresentação.
