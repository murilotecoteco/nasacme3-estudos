/**
 * Consumo de API sem DOM: a ideia é comparar fetch/async com requests/Python.
 * Este módulo não conhece HTML, CSS ou qualquer elemento visual.
 */
export async function fetchCme(startDate, endDate, fetchImpl = fetch) {
  const url = new URL("https://ccmc.gsfc.nasa.gov/DONKI-API/get/CME");
  url.search = new URLSearchParams({ startDate, endDate });

  const response = await fetchImpl(url, { signal: AbortSignal.timeout(30_000) });
  if (!response.ok) {
    throw new Error(`Falha HTTP ${response.status}`);
  }
  const data = await response.json();
  if (!Array.isArray(data)) {
    throw new TypeError("A API não retornou uma lista");
  }
  return data;
}
