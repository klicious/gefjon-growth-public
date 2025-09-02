| **ID** | **Theme** | **Skill Signals** |
| --- | --- | --- |
| **I-1** | Sliding-Window *Median* VWAP | Heap / two-stack window, streaming math |
| **I-2** | Currency Tri-Arbitrage Finder | Graph search, negative-cycle detection |
| **I-3** | Mini Matching Engine | Data-structure design, event handling |
| **I-4** | TTL-Aware LRU Cache | Hash + DLL, eviction policy, edge-cases |
| **I-5** | Trade JSON Schema Validator | Parsing, rules engine, error reporting |

# **◾ Intermediate Problem Set (45 min target each)**

---

## **I-1 Sliding-Window Median VWAP**

### **Summary / Objective**

Stream trade ticks {t, p, s} (epoch s, price, size). For each tick, output the **median price** of all trades whose timestamp is within the last W seconds **and** the classic VWAP over that same window.

### **Detailed Requirements**

| **Spec** | **Detail** |
| --- | --- |
| **Window** | W positive int, rolling (inclusive). |
| **Outputs** | For every input tick emit tuple (median, vwap); if window empty (first tick) still emit. |
| **Performance** | O(log N) per event with two heaps; memory ≈ window size. |
| **Edge** | Expire old ticks on arrival; ties allowed. |

```
def rolling_median_vwap(trades: list[dict], window: int) -> list[tuple[float,float]]:
    ...
```

### **Candidate-Facing Examples**

| **trades** | **W** | **output** |
| --- | --- | --- |
| [{t:0,p:10,s:1},{t:1,p:20,s:1},{t:4,p:30,s:2}] | 3 | [(10,10.0),(15,15.0),(25,25.0)] |

### **Grader Test Matrix**

1. Sparse arrivals → old ticks expire.
2. Identical prices / sizes.
3. Window = 1 (edge).

---

## **I-2 Currency Tri-Arbitrage Finder**

### **Summary / Objective**

Given a directed graph of currency pairs with **log-rate weights** (so sum < 0 implies profit), detect whether any three-currency cycle yields arbitrage and return **one** such cycle.

### **Requirements**

| **Spec** | **Detail** |
| --- | --- |
| **Input** | rates: list[tuple[str,str,float]] where weight = -log(rate). |
| **Output** | Cycle list [A,B,C] or None. |
| **Algo** | Bellman-Ford (3 vertices enough), V ≤ 50. |
| **Edge** | Multiple cycles—return any; no cycle→None. |

```
def tri_arbitrage(rates: list[tuple[str,str,float]]) -> list[str] | None:
    ...
```

**Candidate Example**

| **rates** | **output** |
| --- | --- |
| ("USD","EUR",0.9) ("EUR","JPY",120) ("JPY","USD",0.0095) | ["USD","EUR","JPY"] |

Hidden tests include: no-cycle graph, duplicate edges, disconnected vertices.

---

## **I-3 Mini Matching Engine**

### **Summary / Objective**

Implement price-time-priority limit-order matching for one symbol. Process events:

```
NEW id side price qty
CANCEL id
```

Emit TRADE buyer seller price qty whenever match occurs.

### **Requirements**

| **Spec** | **Detail** |
| --- | --- |
| **Book** | Two ordered dicts (bid max-heap, ask min-heap) preserves FIFO for equal price. |
| **Match Rule** | Crossed book: highest bid ≥ lowest ask. |
| **Constraints** | ≤ 10 k events. |
| **Outputs** | List of strings in arrival order. |

```
def match_engine(events: list[str]) -> list[str]:
    ...
```

**Visible Example**

| **input events** | **output** |
| --- | --- |
| NEW 1 B 100 5, NEW 2 A 99 3 | TRADE 1 2 99 3 |

Hidden tests: partial fills, multiple price levels, cancel race.

---

## **I-4 TTL-Aware LRU Cache**

### **Summary / Objective**

Design class TTLLRU(capacity:int) supporting get(key)/put(key,val,ttl) with **per-entry TTL** (secs). LRU order ignores expired items.

### **Key Points**

- O(1) for both ops.
- On get, return None if missing or expired.
- Evict least-recent **unexpired** when over capacity.

Hidden tests include: expiry mid-iteration, successive puts on same key, capacity 1.

---

## **I-5 Trade JSON Schema Validator**

### **Summary / Objective**

Validate inbound trade JSON against rules:

```
{
 "id": str  (uuid4),
 "symbol": str (^[A-Z]{3,10}$),
 "side": "BUY"|"SELL",
 "price": float (>0),
 "qty": float (>0),
 "ts": int  (epoch s, ≤ now)
}
```

Return tuple (valid:bool, errors:list[str]).

Edge-cases: missing field, wrong type, price ≤ 0, future timestamp.

```
def validate_trade(obj: dict, now: int) -> tuple[bool,list[str]]:
    ...
```

Hidden tests: multiple errors, unicode symbol, large future ts.