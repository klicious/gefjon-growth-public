## **P1 — OHLC Candlestick Generator**

### **Summary / Objective**

Given an unsorted stream of trade ticks — each with timestamp *t* (epoch s), price *p*, and size *s* — aggregate them into **fixed-width candles** (Open, High, Low, Close, Volume) for a user-supplied interval.

### **Detailed Requirements**

| **Spec** | **Detail** |
| --- | --- |
| **Interval** | Positive integer seconds, e.g. 60 s for 1-min candles. |
| **Bucket Rule** | Tick belongs to bucket floor(t / interval) |
| **Outputs** | List **sorted by bucket**: { "start": epoch, "o":…, "h":…, "l":…, "c":…, "v":… } |
| **Edge-Cases** | Empty input → empty list. Single trade bucket. Sparse buckets (skip gaps). Duplicate timestamps allowed. |
| **Complexities** | O(N) time, O(K) space (K = #buckets). |

**Starter signature (Python):**

```
def generate_candles(trades: list[dict], interval: int) -> list[dict]:
    ...
```

### **Candidate-Facing Examples**

| **Input** | **Interval** | **Output** |
| --- | --- | --- |
| [{t:0,p:10,s:2},{t:5,p:12,s:1},{t:61,p:11,s:1}] | 60 | [{start:0,o:10,h:12,l:10,c:12,v:3},{start:60,o:11,h:11,l:11,c:11,v:1}] |
| [] | 15 | [] |

### **Grader Test Matrix**

| **Case** | **Input (trades, interval)** | **Expected Output** |
| --- | --- | --- |
| **Basic** | [{t:30,p:1,s:1}], 60 | [{"start":0,"o":1,"h":1,"l":1,"c":1,"v":1}] |
| **Multi-bucket gap** | [{t:0,p:5,s:1},{t:180,p:6,s:1}], 60 | two candles, middle bucket skipped |
| **Same-timestamp** | [{t:10,p:9,s:2},{t:10,p:7,s:1}], 30 | o=9,h=9,l=7,c=7,v=3 |

---

## **P2 — Rolling Sharpe Ratio**

### **Summary / Objective**

Compute an **N-day rolling Sharpe ratio** for a series of daily PnL numbers (vector of floats). Daily returns are assumed to be PnL divided by prior day equity (simplify: equity = 1). Risk-free rate = 0.

### **Detailed Requirements**

| **Spec** | **Detail** |
| --- | --- |
| **Window** | Input integer n (≥2). |
| **Sharpe** | mean(window) / std(window) (population σ). |
| **Output** | List same length as input; positions < n-1 are None. |
| **Edge-Cases** | σ = 0 → Sharpe is None. |

**Starter signature**

```
def rolling_sharpe(pnl: list[float], n: int) -> list[float | None]:
    ...
```

### **Candidate-Facing Examples**

| **PnL** | **n** | **Output** |
| --- | --- | --- |
| [1,-1,2,2] | 3 | [None,None,~0.0,~?] (walk through with candidate) |
| [0,0,0] | 2 | [None,None,None] |

### **Grader Test Matrix**

| **Case** | **Input** | **Expected** |
| --- | --- | --- |
| **Exact σ=0** | [1,1,1], 3 | all None |
| **Normal** | [1,-1,2,1], 2 | [None,0,~?,~?] |
| **Short vector** | [5], 4 | [None] |

---

## **P3 — Exchange Funding-Time Calculator**

### **Summary / Objective**

For perpetual futures, many venues settle funding every 8 h at **00:00, 08:00, 16:00 UTC**. Implement a function that, given a UTC timestamp, returns the epoch of the **next** funding time.

### **Detailed Requirements**

| **Spec** | **Detail** |
| --- | --- |
| **Inputs** | ts (epoch s, int). |
| **Outputs** | int epoch (exact boundary). |
| **Edge-Cases** | If ts is exactly on boundary → return same boundary. |
| **Time** | Use datetime but must be **timezone-safe** (assume UTC only). |

**Starter signature**

```
def next_funding_time(ts: int) -> int:
    ...
```

### **Candidate-Facing Examples**

| **ts (UTC)** | **Output (UTC)** |
| --- | --- |
| 2025-07-14 06:00 | 2025-07-14 08:00 |
| 2025-07-14 08:00 | 2025-07-14 08:00 |

### **Grader Test Matrix**

| **Case** | **Input** | **Expected UTC** |
| --- | --- | --- |
| **Late night** | 2025-07-14 23:59:59 | 2025-07-15 00:00 |
| **Exactly 15:59:59** | …15:59:59 | 16:00 |
| **Far past** | 1609459200 (2021-01-01 00:00) | same (boundary) |

---

## **P4 — Order-Book Imbalance Indicator**

### **Summary / Objective**

Given two lists of (price, size) **bids** and **asks** (top *k* levels), compute the **Imbalance Ratio**

IR = (Σ_bid_size − Σ_ask_size) / (Σ_bid_size + Σ_ask_size), rounded to 4 dp.

### **Detailed Requirements**

| **Spec** | **Detail** |
| --- | --- |
| **Inputs** | bids, asks as list[tuple[price:float,size:float]]. |
| **Validate** | Empty side → treat sum = 0 (return ±1). |
| **Output** | float in [-1,1]. |

**Starter signature**

```
def orderbook_imbalance(bids: list[tuple[float,float]],
                        asks: list[tuple[float,float]]) -> float:
    ...
```

### **Candidate-Facing Examples**

| **Bids** | **Asks** | **Output** |
| --- | --- | --- |
| [(100,2),(99,1)] | [(101,1)] | (3-1)/4 = 0.5 |
| [] | [(101,1)] | -1.0 |

### **Grader Test Matrix**

| **Case** | **Input** | **Expected** |
| --- | --- | --- |
| **Symmetric** | bid 3, ask 3 | 0.0 |
| **Only bids** | ask empty | 1.0 |
| **Zero sum** | all sizes 0 | handle div-by-zero → return 0.0 |

---

## **P5 — API Burst Scheduler**

### **Summary / Objective**

Design a generator that yields **earliest permissible send-times** for a queue of *M* API calls under **burst rule**: at most rate calls per rolling window seconds.

### **Detailed Requirements**

| **Spec** | **Detail** |
| --- | --- |
| **Inputs** | timestamps (list[int]) arrival times, rate, window. |
| **Logic** | If a call would exceed rate within the last window, delay it to earliest allowed. |
| **Output** | List[int] of send times, non-decreasing. |
| **Constraints** | O(M) with deque. |

**Starter signature**

```
def schedule_burst(timestamps: list[int], rate: int, window: int) -> list[int]:
    ...
```

### **Candidate-Facing Examples**

| **arrivals** | **rate / window** | **output** |
| --- | --- | --- |
| [0,1,2], 2/2 | [0,1,2] |  |
| [0,0,0], 2/2 | [0,0,2] |  |

### **Grader Test Matrix**

| **Case** | **Input** | **Expected** |
| --- | --- | --- |
| **Long queue** | [0,1,2,3], 2/3 | [0,1,3,4] |
| **Exact window** | [0,1,3], 2/3 | [0,1,3] |
| **Burst gap** | [0,10,10,10], 3/5 | [0,10,10,10] (no delay) |

---

### **How to Use These Problems**

1. **Share only** the Summary, Requirements, Starter Signature, and Candidate-Facing Examples.
2. Keep the Grader Test Matrix inside your Autograder or copy-paste after the interview ends.
3. Map each rubric criterion (“Problem Solving”, “Code Quality”, etc.) to concrete behaviors you observe while they tackle these tasks.

These domain-flavored problems, plus robust test sets, will give you a high-signal look at raw coding ability, reasoning, and collaboration under real interview time constraints.