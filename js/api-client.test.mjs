import assert from "node:assert/strict";
import test from "node:test";
import { fetchCme } from "./api-client.js";

test("fetchCme envia os parâmetros e devolve uma lista", async () => {
  let receivedUrl;
  const result = await fetchCme("2026-01-01", "2026-01-02", async (url) => {
    receivedUrl = String(url);
    return { ok: true, json: async () => [{ activityID: "cme-1" }] };
  });

  assert.match(receivedUrl, /startDate=2026-01-01/);
  assert.match(receivedUrl, /endDate=2026-01-02/);
  assert.deepEqual(result, [{ activityID: "cme-1" }]);
});

test("fetchCme transforma HTTP de erro em exceção", async () => {
  await assert.rejects(
    fetchCme("2026-01-01", "2026-01-02", async () => ({ ok: false, status: 503 })),
    /Falha HTTP 503/,
  );
});

test("fetchCme rejeita payload que não é lista", async () => {
  await assert.rejects(
    fetchCme("2026-01-01", "2026-01-02", async () => ({ ok: true, json: async () => ({}) })),
    /não retornou uma lista/,
  );
});
