# 03 — SQL, upsert e RLS

Leia `sql/01_schema.sql` e compare com `sql/setup.sql` do NASACME3.

Pontos para estudar:

- chave `unique` permite que um upsert seja idempotente;
- índices aceleram filtros, mas têm custo de escrita e armazenamento;
- `jsonb` conserva listas de instrumentos sem criar outra tabela neste exercício;
- RLS decide quais linhas cada papel pode ler ou alterar.

No projeto real, verifique sempre `USING` e `WITH CHECK` separadamente. Uma
policy permissiva de leitura pode neutralizar outra policy de leitura na mesma
tabela; não conclua que uma operação de escrita funcionou apenas pelo status
HTTP — conte as linhas afetadas.
