# valo_scout

A terminal stat tracker for Valorant. It pulls a set of recent matches, ranks them by a
composite impact score using a hand-written heapsort, and renders the top five in a
`rich` table.

> **Note:** the data source is currently mocked. `analyzer/api_client.py` generates
> synthetic matches rather than calling a live endpoint, so the tool runs standalone
> with nothing to configure. The docstring on `fetch_recent_matches` shows what the real
> request looks like. Everything downstream of the fetch — scoring, sorting, rendering —
> is real and works on live data unchanged.

## How it works

* **Impact score over raw K/D.** A match is ranked by `(kills + assists) / deaths`,
  weighted by a variance factor, so a 20/18/12 game does not outrank a 16/6/9 one just
  on kill count.
* **Heapsort, written out.** `analyzer/algorithms.py` implements `heapify` and
  `heapsort_matches` directly rather than calling `sorted()`. It builds a max-heap over
  the match dicts keyed on any field, extracts in place for O(n log n) worst case with
  no extra allocation, then reverses for descending order.
* **Agent-specific columns.** The table surfaces utility usage (smokes deployed)
  alongside combat stats, since for a controller main that is the number that actually
  reflects the round.

## Run

```bash
git clone https://github.com/apollo-2006/valo_scout.git
cd valo_scout

pip install -r requirements.txt
python main.py
```

Output is a five-row table of peak-impact matches: map, K/D/A, KDA ratio, smokes
deployed, and the computed impact score.

## Layout

```
main.py                     entry point, theme, table rendering
analyzer/api_client.py      match retrieval (currently synthetic)
analyzer/algorithms.py      heapify + heapsort over match dicts
```

## Author

**Abir Deol**
