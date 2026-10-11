# Data-cleaning reference for VS Code.
# Run a cell with Shift+Enter. Cells start with "# %%".
# Read from data/raw/. Write the result to data/clean/. Never overwrite the raw file.
# Skip any cell that does not apply. Do not invent a column just to run a cell.
# Develop on a sample (nrows), then run the same file on the full local data.
# Course projects still need a large source: at least 200,000 rows on one file,
# or a credible combination. The sample is only for writing the code.

# %% 0. Load, and remember the starting size
import numpy as np
import pandas as pd

# EDIT
raw_path = "data/raw/YOUR_FILE.csv"
df = pd.read_csv(raw_path, nrows=10000)  # remove nrows for the final run

rows_before = len(df)
print("rows", df.shape[0], "cols", df.shape[1])
print(df.dtypes)
print(df.head())

# %% 1. Nulls
# Count missing values before you drop or fill anything.
null_counts = df.isna().sum().sort_values(ascending=False)
null_share = (df.isna().mean() * 100).round(1)
print(pd.DataFrame({"nulls": null_counts, "percent": null_share}))

# EDIT — look at the blanks in one column you care about
col = "YOUR_COLUMN"
print(df.loc[df[col].isna()].head())

# Choices, per column: leave the nulls, drop those rows, or fill.
# Filling changes later averages. Say which you chose.
# df = df.dropna(subset=["YOUR_COLUMN"])
# df["YOUR_COLUMN"] = df["YOUR_COLUMN"].fillna("Unknown")

# %% 2. Special characters in a column that should be numeric
# $, commas, %, and words such as N/A or "-" often hide in "number" columns.
# EDIT
text_col = "YOUR_AMOUNT_COLUMN"
print(df[text_col].astype(str).head(15))

cleaned = (
    df[text_col]
    .astype(str)
    .str.strip()
    .str.replace("\u00a0", "", regex=False)
    .str.replace(r"[$%,]", "", regex=True)
    .replace(
        {
            "nan": np.nan,
            "None": np.nan,
            "N/A": np.nan,
            "n/a": np.nan,
            "-": np.nan,
            "?": np.nan,
        }
    )
)
df[text_col] = pd.to_numeric(cleaned, errors="coerce")
print(df[text_col].head())
print("became null:", int(df[text_col].isna().sum()))
# A value that becomes null is a decision. Look at a few raw strings first.

# %% 3. Data types
print(df.dtypes)

# EDIT
num_col = "YOUR_NUMERIC_COLUMN"
before_nulls = int(df[num_col].isna().sum())
df[num_col] = pd.to_numeric(df[num_col], errors="coerce")
after_nulls = int(df[num_col].isna().sum())
print("nulls before", before_nulls, "after", after_nulls)
# errors="coerce" turns non-numbers into null. Record that count.

# %% 4. Dates and datetimes
# EDIT
date_col = "YOUR_DATE_COLUMN"
raw_dates = df[date_col].copy()
df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
failed = int(df[date_col].isna().sum())
print("failed to parse:", failed)
print(raw_dates[df[date_col].isna()].head(10))
print("min", df[date_col].min(), "max", df[date_col].max())

# If many fail, rows may use different formats. Inspect them before dropping.
# df[date_col] = pd.to_datetime(raw_dates, format="%Y-%m-%d", errors="coerce")

# Calendar day only, when you do not need the clock time:
df["day"] = df[date_col].dt.date
print(df[["day"]].head())

# %% 5. Extra decimals
# 3.1000000000000001 is usually how a binary float prints.
# Rounding stores a different number. Formatting only changes the print.
# EDIT
money_col = "YOUR_NUMERIC_COLUMN"
print(df[money_col].head())

# Print two decimals without changing stored values:
shown = df[money_col].map(lambda x: f"{x:.2f}" if pd.notna(x) else x)
print(shown.head())

# Uncomment only if you have decided the stored value should change.
# df[money_col] = df[money_col].round(2)

# %% 6. Outliers — surface them, do not delete them here
# EDIT
x = "YOUR_NUMERIC_COLUMN"
s = df[x].dropna()
q1 = s.quantile(0.25)
q3 = s.quantile(0.75)
iqr = q3 - q1
low = q1 - 1.5 * iqr
high = q3 + 1.5 * iqr
outlier_mask = (df[x] < low) | (df[x] > high)
print("fence", round(float(low), 3), round(float(high), 3))
print("outlier rows:", int(outlier_mask.sum()))
print(df.loc[outlier_mask, [x]].head(10))

arr = df[x].to_numpy(dtype=float)
valid = arr[~np.isnan(arr)]
q1_np, q3_np = np.percentile(valid, [25, 75])
iqr_np = q3_np - q1_np
print("numpy fence:", q1_np - 1.5 * iqr_np, q3_np + 1.5 * iqr_np)

# Uncomment only after you have written why.
# df = df.loc[~outlier_mask].copy()

# %% 7. Duplicates
print("duplicate rows:", int(df.duplicated().sum()))
# print("duplicate ids:", int(df.duplicated(subset=["YOUR_ID"]).sum()))
# A repeated row can be a double entry or a real repeated event.
# df = df.drop_duplicates()

# %% 8. Stray whitespace and inconsistent categories
# EDIT
label = "YOUR_TEXT_COLUMN"
text = df[label]
keep = text.notna()
df.loc[keep, label] = (
    text[keep].astype(str).str.strip().str.replace(r"\s+", " ", regex=True)
)
# Same word, different capitals, is still two categories until you merge them.
df.loc[keep, label] = df.loc[keep, label].str.lower()
print(df[label].value_counts(dropna=False).head(15))

# Synonyms are a decision. Example only:
# df[label] = df[label].replace({"y": "yes", "n": "no"})

# %% 9. Sentinel codes that mean "missing"
# Some files use -1, 0, 99, or 999 instead of a blank.
# EDIT the column and the codes that mean missing in this file.
sentinel_col = "YOUR_COLUMN"
sentinels = [-1, 99, 999, 9999]
before = int(df[sentinel_col].isna().sum())
df[sentinel_col] = df[sentinel_col].replace(sentinels, np.nan)
after = int(df[sentinel_col].isna().sum())
print("nulls before", before, "after treating sentinels", after)
# Only list codes you have checked. 0 is a real measurement in many columns.

# %% 10. Impossible values
# EDIT the rule so it matches this column (age, percent, count, ...).
range_col = "YOUR_NUMERIC_COLUMN"
low_ok, high_ok = 0, 120  # EDIT
impossible = (df[range_col] < low_ok) | (df[range_col] > high_ok)
print("outside the possible range:", int(impossible.sum()))
print(df.loc[impossible, [range_col]].head(10))
# Count them and decide. Do not drop them in this cell by default.

# %% 11. Column names
# Run this after the column checks above. It changes the names those cells use.
# Spaces and capitals make later code brittle. Renaming is a decision: record it.
print(list(df.columns))
df.columns = (
    df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
)
print(list(df.columns))

# %% 12. Ids that loaded as floats, and empty or constant columns
# 1001.0 is often an id that was read as a float. Nullable Int64 keeps real blanks.
# EDIT
# df["YOUR_ID"] = df["YOUR_ID"].round().astype("Int64")

empty_cols = [c for c in df.columns if df[c].isna().all()]
constant_cols = [c for c in df.columns if df[c].nunique(dropna=False) <= 1]
print("entirely empty:", empty_cols)
print("only one distinct value:", constant_cols)
# An empty column cannot answer a question. A constant column cannot explain differences.

# %% 13. Save, and compare before and after
rows_after = len(df)
print("rows before", rows_before, "rows after", rows_after)

# EDIT the output name. Create data/clean/ first if it does not exist.
df.to_csv("data/clean/YOUR_FILE_clean.csv", index=False)
# Do not commit a huge CSV. Do commit this script and the cleaning log.
