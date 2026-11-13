-- Banco didático inspirado no NASACME3. Execute em PostgreSQL/Supabase.
create table if not exists cme_events (
  id bigint generated always as identity primary key,
  activity_id text not null unique,
  start_time timestamptz,
  speed numeric,
  type text,
  is_earth_directed boolean not null default false,
  source_location text,
  instruments jsonb not null default '[]'::jsonb,
  fetched_at timestamptz not null default now()
);

create index if not exists idx_cme_events_start_time on cme_events (start_time);
create index if not exists idx_cme_events_speed on cme_events (speed);

create table if not exists execucoes (
  id bigint generated always as identity primary key,
  executed_at timestamptz not null default now(),
  registros_processados integer not null default 0,
  lotes integer not null default 0,
  erros integer not null default 0,
  status text not null check (status in ('concluido', 'erro_parcial', 'erro_critico'))
);

alter table cme_events enable row level security;
alter table execucoes enable row level security;

drop policy if exists "public read cme events" on cme_events;
create policy "public read cme events" on cme_events
  for select to anon, authenticated using (true);

drop policy if exists "service role manages cme events" on cme_events;
create policy "service role manages cme events" on cme_events
  for all to service_role using (true) with check (true);

drop policy if exists "public read executions" on execucoes;
create policy "public read executions" on execucoes
  for select to anon, authenticated using (true);

drop policy if exists "service role manages executions" on execucoes;
create policy "service role manages executions" on execucoes
  for all to service_role using (true) with check (true);

grant select on cme_events to anon, authenticated;
grant all on cme_events to service_role;
grant select on execucoes to anon, authenticated;
grant all on execucoes to service_role;

-- Exercício: explique por que activity_id é chave natural e por que o índice
-- de start_time ajuda a consulta por período. Depois estude o RLS do projeto real.
