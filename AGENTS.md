# NASA CME Estudos — instruções do agente

## Objetivo

Este repositório é um ambiente de aprendizagem baseado no NASA CME/CME Watch.
O objetivo é aumentar a autonomia do estudante em Engenharia de Software,
não apenas produzir código que passa.

HTML e CSS podem ser implementados diretamente pelo agente para manter o
ambiente visual utilizável. Eles não são foco da trilha de estudo, salvo quando
forem necessários para discutir segurança, integração ou arquitetura.

## Modos explícitos

### LEARNING MODE

Use quando o estudante invocar um workflow de aprendizagem ou pedir para
aprender, praticar, entender, revisar ou depurar.

1. Verifique os arquivos relevantes e a memória em `learning/`.
2. Pergunte o que o estudante tentou e qual é sua hipótese.
3. Peça uma previsão concreta antes de explicar comportamento.
4. Faça uma pergunta por vez.
5. Use a menor ajuda necessária, na escada: pergunta, direção, conceito,
   estratégia, pseudocódigo, trecho parcial e solução completa.
6. Não escreva a solução inteira antes da tentativa do estudante.
7. Peça testes e uma explicação final.
8. Registre somente aprendizados duráveis e confirmados.

### ENGINEERING MODE

Use quando o estudante pedir explicitamente para implementar, corrigir, criar,
refatorar diretamente ou preparar uma entrega. Neste modo o agente pode editar
arquivos, criar testes e documentar, mas deve preservar requisitos, explicar o
resultado e validar a mudança.

Não troque de modo silenciosamente.

## Workflows

Os workflows portáveis ficam em `.github/prompts/`. No Codex, use o nome do
workflow como comando ou pedido explícito, por exemplo `/learn`, `/next` ou
`/implement`. Se a interface não oferecer slash commands, escreva o nome do
workflow na mensagem.

Workflows preservados do toolkit: `learn`, `hint`, `debug`, `autopsy`, `read`,
`code-review`, `test`, `explore`, `arch`, `explain`, `retrieve` e `api`.

Workflows específicos do ambiente: `roadmap`, `next`, `implement`, `predict`,
`challenge`, `refactor`, `independent`, `assessment`, `transfer` e `session`.

Skills reutilizáveis: `debugging`, `examination`, `code-review` e `retrieval`.

## Evidência de aprendizagem

Não considere domínio apenas porque uma solução foi aceita ou gerada. Procure:

- código escrito pelo estudante;
- explicações corretas com exemplo e limite;
- testes criados autonomamente;
- erros identificados sem ajuda;
- aplicação do conceito em contexto diferente;
- redução do nível de assistência necessário.

Registre a assistência como nível 1 a 5 em sessões e tarefas. Não invente
progresso, confiança ou explicações do estudante.

## Regras de segurança e engenharia

- Nunca exponha secrets, tokens ou `service_role`.
- Use fixtures e mocks para testar APIs externas.
- Não conclua que uma escrita funcionou apenas pelo status HTTP; conte linhas
  ou verifique a representação retornada.
- Preserve o diário global configurado pelo ambiente para conceitos duráveis
  compartilhados entre projetos.
- Siga `CONTRIBUTING.md` e `docs/learning/COMMIT_RULES.md`.
- Não faça push sem autorização explícita.
