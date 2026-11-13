const phases = [
  ["01", "Orientação", "Ler o fluxo real antes de alterar código."],
  ["02", "Dados", "API, JSON, normalização e deduplicação."],
  ["03", "Confiabilidade", "Retry, timeout, erros e testes."],
  ["04", "Persistência", "SQL, upsert, RLS e auditoria."],
  ["05", "Automação", "Actions, secrets e CI/CD."],
  ["06", "Apresentação", "Arquitetura, evidências e transferência."],
];

const checks = [
  "Codex instruído por AGENTS.md",
  "Copilot instruído por .github/",
  "Testes Python e JavaScript",
  "Memória de aprendizagem",
  "Backlog com critérios de aceitação",
  "Regras de commit",
];

const roadmap = document.querySelector("#roadmap");
for (const [number, title, description] of phases) {
  const article = document.createElement("article");
  article.className = "phase";
  const index = document.createElement("span");
  index.className = "phase-index";
  index.textContent = number;
  const body = document.createElement("div");
  const heading = document.createElement("h3");
  heading.textContent = title;
  const copy = document.createElement("p");
  copy.textContent = description;
  body.append(heading, copy);
  const status = document.createElement("span");
  status.className = "phase-status";
  status.textContent = "PLANEJADA";
  article.append(index, body, status);
  roadmap.append(article);
}

const checklist = document.querySelector("#checklist");
for (const item of checks) {
  const line = document.createElement("div");
  line.className = "check";
  const mark = document.createElement("span");
  mark.className = "check-mark";
  mark.setAttribute("aria-hidden", "true");
  const label = document.createElement("span");
  label.textContent = item;
  line.append(mark, label);
  checklist.append(line);
}
