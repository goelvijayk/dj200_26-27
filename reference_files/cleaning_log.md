# Class 4 homework log — due 18 Oct 2026

Copy this file to your project repo as **`cleaning_log.md`**. Fill in every section below.  
Your code file is **`03_understand_and_clean.py`**, adapted from `guides/data_cleaning_reference.py`.

**Rules**

- Read from `data/raw/`. Write the cleaned table to `data/clean/`. Do not overwrite the raw file.
- If a cleaning section does not apply to your file, write **Skipped —** and one short reason. Do not invent a column just to run a cell.
- The script can show a problem. You decide whether to change the data. Write the decisions in your own words.

---

## 1. What you are trying to accomplish

Write **one paragraph** (about 5–8 sentences): the question you are investigating, who or what the rows represent, and what you hope to show by the end of the project. This should match your Class 3 proposal unless a teacher approved a change.

---

## 2. Datasets

List every file you are using. For each row, name the file, where it lives on your machine, and roughly how many rows it has (sample or full file).

| File name | Path (e.g. `data/raw/...`) | Rows (approx.) | Role in the project |
| --- | --- | --- | --- |
| | | | |
| | | | |

---

## 3. Link to the full data dictionary

Paste the **repository or web link** where the **full** data dictionary lives (course site, government portal, Kaggle page, README in the download, etc.).

**Link:**

If there is no single dictionary page, say where you read column definitions (PDF name, “Data Dictionary” tab URL, etc.).

---

## 4. Fields you chose for analysis

For **each column you plan to use** in the project, fill one block. Repeat the block for as many fields as you need (at minimum: your target to predict and two or three predictors from Class 3).

### Field: `COLUMN_NAME` — dataset: `FILE_NAME`

| Item | Your answer |
| --- | --- |
| **Why this field matters** | One sentence tied to your project question. |
| **Meaning (your words)** | Plain-language definition, as you understand it from the dictionary or source site. |
| **Type in the raw file** | What `df.dtypes` shows before you change anything (e.g. `object`, `float64`). |
| **Main finding from cleaning (if any)** | One or two sentences: nulls, special characters, sentinels, impossible values, outliers, duplicates, etc. If you have not run that cell yet, write **Not checked yet.** |

*(Copy the block above for each chosen field.)*

---

## 5. Data cleaning findings

Answer using the same **numbered cells** as in `03_understand_and_clean.py` (the comments that start with `# %%`). Run a cell with **Shift+Enter** in VS Code, then write what you saw and what you decided.

**Always answer:** Cell **0** (load), Cell **13** (save — include the three “least sure” items and one deliberate non-change below).

**Skip** any other cell if that issue is not in your file. Write **Skipped —** and why.

---

### Cell 0 — Load, and remember the starting size

After `pd.read_csv` (with or without `nrows`):

- How many **rows** and **columns**?
- What do **`df.dtypes`** and **`df.head()`** show?
- Which columns does your project question **need**?

---

### Cell 1 — Nulls

After `null_counts` / `null_share` and looking at blanks in one column:

- Which columns that you care about have missing values? How many (and roughly what **percent**)?
- For each important column: did you **leave** the nulls, **drop** those rows (`dropna`), or **fill** (`fillna`)? Why?

**Skipped —** *(only if no column you will use has missing values)*:

---

### Cell 2 — Special characters in a column that should be numeric

After stripping `$`, commas, `%`, and words like `N/A`, and using `pd.to_numeric(..., errors="coerce")`:

- Which column did you clean?
- What symbols or placeholder words did you remove?
- How many values **became null** after cleaning (`became null:` in the printout)?

**Skipped —**:

---

### Cell 3 — Data types

After `pd.to_numeric` (or similar) on a numeric column:

- Which column’s type did you change?
- **`nulls before`** and **`nulls after`** — how many values failed to convert?

**Skipped —**:

---

### Cell 4 — Dates and datetimes

After `pd.to_datetime(..., errors="coerce")`:

- Which date column?
- How many values **failed to parse** (`failed to parse:`)?
- What do a few **failed raw strings** look like?
- **Earliest** and **latest** parsed date (`min` / `max`)?
- Did you keep, drop, or fix failed rows?

**Skipped —** *(no date or time column)*:

---

### Cell 5 — Extra decimals

After comparing stored values to **print-only** formatting (`f"{x:.2f}"`) vs **`round`**:

- Which column?
- Did you only change how numbers **print**, or did you change **stored** values with `round`? Why?

**Skipped —**:

---

### Cell 6 — Outliers — surface them, do not delete them here

After the **fence** (`low`, `high`) and **`outlier rows:`** count:

- Which numeric column?
- Fence values and **how many rows** are outside the fence?
- Did you **leave** them in the table for now, or **remove** them (`df.loc[~outlier_mask]`)? If you removed any, what might that hide?

**Skipped —**:

---

### Cell 7 — Duplicates

After **`duplicate rows:`** (and optional duplicate ids):

- How many duplicate rows?
- Could a repeat be a **double entry** or a **real repeated event**?
- Did you drop duplicates? Why or why not?

**Skipped —** *(e.g. zero duplicates — one line is enough)*:

---

### Cell 8 — Stray whitespace and inconsistent categories

After **strip**, lowercasing, and `value_counts`:

- Which text column?
- What did you change (spaces, capitals, merged labels like `y` / `yes`)?
- Anything still inconsistent that you left for later?

**Skipped —**:

---

### Cell 9 — Sentinel codes that mean "missing"

After `replace(sentinels, np.nan)`:

- Which column and which **codes** (-1, 99, 999, …) mean missing in **your** file?
- **`nulls before`** and **`nulls after treating sentinels`**?

**Skipped —** *(no sentinel codes)*:

---

### Cell 10 — Impossible values

After counting rows **outside the possible range** (`low_ok`, `high_ok`):

- Which column and what range did you treat as possible?
- How many rows fall outside? What did you do with them?

**Skipped —**:

---

### Cell 11 — Column names

After `df.columns.str.strip().str.lower()...`:

- Did you rename columns? Give **one old name → new name** example.
- Or did you leave names as they were? Why?

**Skipped —** *(names already usable)*:

---

### Cell 12 — Ids that loaded as floats, and empty or constant columns

After printing **`entirely empty:`** and **`only one distinct value:`**:

- Any id columns fixed with **`Int64`**?
- Any **empty** or **constant** columns? Will you drop them or keep them?

**Skipped —**:

---

### Cell 13 — Save, and compare before and after

- **`rows before`** and **`rows after`**?
- Exact path to the **clean file** (`data/clean/...`)?
- Confirm the **raw file** under `data/raw/` was **not** edited.

**Three choices you are least sure about** (required):

1.
2.
3.

**One problem you found and deliberately did not change** (required):

---

## 6. Hypotheses and early checks (at least 10)

List **at least 10** hypotheses you want to test. They can be about **cleaning**, **validation** (“does this column behave the way the dictionary says?”), or **substance** — they do not all have to be your final project outcome. The goal is to show you have read about the topic and looked at the data.

For each hypothesis, use this format:

| # | Hypothesis | Quick check you ran (or will run) | Answer or finding so far | Surprising? |
| --- | --- | --- | --- | --- |
| 1 | | | | yes / no |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |

Add rows 11+ if you have more. Put **surprising findings** in the “Answer or finding” column and mark **Surprising?** as **yes**.

---

## 7. Plan for data imperfections

Summarize how you will handle problems **going forward** (this week and later in the project). Mention concrete tools you used or plan to use from your script: **leave nulls**, **drop rows** (`dropna`), **fill** (`fillna`), **treat sentinels as null**, **cap** or **leave outliers**, **exclude impossible values**, **merge categories**, etc.

| Issue (column or row type) | What you saw | Planned handling | How that changes who or what your results describe |
| --- | --- | --- | --- |
| | | | |
| | | | |

---

## 8. Prior similar work

Summarize **at least one** published or student-journal style paper (high school or similar) on a related topic. Include a **link** and 3–5 sentences: what they asked, what data they used, and how your project is similar or different.

**Paper title / source:**

**Link:**

**Summary:**

---

## 9. Links to scripts and working files

| Item | Link or path |
| --- | --- |
| `03_understand_and_clean.py` | GitHub link or repo path |
| This log (`cleaning_log.md`) | |
| Raw file location | `data/raw/...` (do not commit huge files unless your teacher said to) |
| Clean file location | `data/clean/...` |
| Other notebooks or scripts | |

---

## 10. Confusing or hard parts

What was difficult, unclear, or frustrating about the data, the dictionary, the code cells, or the project direction? List at least **two** bullets. These help teachers support you next week.

-
-

---

**Submit for teacher approval on GitHub:** `03_understand_and_clean.py`, this `cleaning_log.md`, and your cleaned file under `data/clean/` on your machine.
