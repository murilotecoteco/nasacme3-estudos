# NASACME3 Estudos

Ambiente de aprendizado prático para compreender e defender o projeto
NASACME3/CME Watch. O projeto inclui um painel HTML/CSS funcional, mas essa
camada é mantida pelo agente e não é o foco principal dos estudos. O foco do
estudante é Engenharia de Software aplicada ao fluxo real:

```text
API NASA/DONKI -> validação e normalização -> deduplicação -> lotes -> banco
                         \-> logs, testes e automação
```

## O que será estudado

- HTTP, JSON, query parameters, timeout e retry;
- variáveis de ambiente e proteção de secrets;
- funções puras, tipagem, tratamento de valores ausentes e normalização;
- deduplicação, idempotência, processamento em lotes e métricas;
- PostgreSQL: tabela, chave única, índices, upsert e RLS;
- JavaScript moderno para consumo de API, sem manipulação de interface;
- testes automatizados e GitHub Actions;
- segurança operacional e leitura crítica de respostas HTTP.

O painel visual existe para tornar o aprendizado observável. HTML e CSS não são
itens obrigatórios da trilha pedagógica.

## Estrutura

```text
nasacme3-estudos/
├── aulas/                         # explicações curtas e exercícios
├── docs/learning/                 # auditoria, roadmap, backlog e avaliação
├── learning/                      # memória específica deste projeto
├── fixtures/cme.json              # dados locais para estudar sem internet
├── index.html                     # painel de acompanhamento
├── style.css                      # estilo do painel, mantido pelo agente
├── js/api-client.js               # fetch + query parameters, sem DOM
├── js/dashboard.js                # comportamento do painel
├── sql/01_schema.sql              # modelo didático do banco
├── src/nasacme_estudos/
│   ├── api.py                     # HTTP, retry e JSON
│   ├── domain.py                  # regras de negócio puras
│   ├── pipeline.py                # lotes, status e métricas
│   └── storage.py                 # persistência local e upsert
├── tests/                         # testes unitários
├── AGENTS.md                      # regras para o Codex
├── CONTRIBUTING.md                # fluxo de contribuição e commits
├── requirements.txt
└── pyproject.toml
```

## Como executar

```bash
cd nasacme3-estudos
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
npm test
```

O exemplo local não precisa de Supabase nem de chave da NASA:

```bash
PYTHONPATH=src python -m nasacme_estudos.pipeline --fixture fixtures/cme.json
```

Para exercitar persistência, upsert e registro de execução local:

```bash
PYTHONPATH=src python -m nasacme_estudos.pipeline \
  --fixture fixtures/cme.json --database work/study.db
```

Para abrir o painel, use um servidor HTTP local:

```bash
python -m http.server 8000
```

Depois acesse `http://localhost:8000`.

Para consultar a API real, informe um intervalo e execute:

```bash
PYTHONPATH=src python -m nasacme_estudos.api \
  --start 2026-01-01 --end 2026-01-07
```

Não coloque `SUPABASE_SERVICE_KEY`, tokens ou arquivos `.env` no Git.

## Trilha sugerida

1. Leia [`docs/learning/ROADMAP.md`](docs/learning/ROADMAP.md).
2. Comece por [`CME-LEARN-001`](docs/learning/BACKLOG.md).
3. Use os workflows documentados em [`AGENTS.md`](AGENTS.md).
4. Registre somente evidências reais em `learning/`.
5. Use [`docs/learning/PRESENTATION_PREP.md`](docs/learning/PRESENTATION_PREP.md) para ensaiar a banca.

As aulas complementares estão em `aulas/`; elas acompanham o backlog e não
substituem a tentativa do estudante.

## Modos de trabalho

- **LEARNING MODE:** você tenta primeiro; a IA faz perguntas e oferece dicas graduais.
- **ENGINEERING MODE:** a IA pode implementar diretamente quando você pedir.

Os dois modos são explícitos e não mudam silenciosamente.

## Integração com IA

O projeto possui uma camada para Codex em `AGENTS.md` e uma camada compatível
com GitHub Copilot em `.github/`. Os prompts e skills foram adaptados ao NASA
CME, mantendo os nomes do toolkit de referência.

## Commits

Os commits seguem Conventional Commits em inglês. Consulte
[`docs/learning/COMMIT_RULES.md`](docs/learning/COMMIT_RULES.md) e
[`CONTRIBUTING.md`](CONTRIBUTING.md).

Se o diretório ainda não tiver Git inicializado, execute:

```bash
bash scripts/init_git.sh
```

O projeto original continua intacto em `/home/murilo/PROJETOS/NASACME3`.
