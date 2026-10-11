# Data clinic for VS Code.
# Run a cell: click it and press Shift+Enter. Cells start with "# %%".
# Point PATH at any CSV that has at least one numeric column.
# Edit the column names in the cells that say EDIT.
# This file does not assume a particular class session.

# %% Setup
import numpy as np
import pandas as pd

# EDIT
PATH = "data/raw/YOUR_FILE.csv"
NUMERIC = "YOUR_NUMERIC_COLUMN"
NUMERIC_2 = "YOUR_SECOND_NUMERIC_COLUMN"  # used in the last exercise; may match NUMERIC

# A sample is enough while you are still fixing paths and names.
df = pd.read_csv(PATH, nrows=10000)
print(df.shape)
print(df.head())

# %% Exercise 1 — What is in the table
print(df.dtypes)
print("missing:\n", df.isna().sum().sort_values(ascending=False).head(15))
# Write: rows, columns, and which column has the most missing values.

# %% Exercise 2 — One numeric column as an array
values = df[NUMERIC].to_numpy(dtype=float)  # EDIT NUMERIC above
print("shape:", values.shape)
print("missing in this column:", int(np.isnan(values).sum()))

# %% Exercise 3 — Summaries that skip missing numbers
print("mean:", np.nanmean(values))
print("median:", np.nanmedian(values))
print("std:", np.nanstd(values))
print("min:", np.nanmin(values), "max:", np.nanmax(values))
# Write one sentence: do these numbers look plausible for this column?

# %% Exercise 4 — Where the values sit
# Percentiles: 50 is the median. 90 means 90% of values are at or below this number.
p10, p50, p90 = np.nanpercentile(values, [10, 50, 90])
print("p10, p50, p90:", p10, p50, p90)

# %% Exercise 5 — Keep rows above a cutoff you choose
cutoff = 0  # EDIT so the cutoff means something for this column
mask = values > cutoff
print("above cutoff:", int(np.nansum(mask)))
print("share above cutoff:", float(np.nanmean(mask)))
# Write: the cutoff, the count, and whether the cutoff is meaningful.

# %% Exercise 6 — Flag rows without deleting them
# 1 means "above cutoff", 0 means "not". Missing stays missing.
flag = np.where(np.isnan(values), np.nan, np.where(values > cutoff, 1, 0))
print("flagged:", int(np.nansum(flag)))
print(flag[:10])

# %% Exercise 7 — How far from the typical value
center = np.nanmean(values)
spread = np.nanstd(values)
if spread == 0 or np.isnan(spread):
    print("No spread to measure. Every non-missing value is the same, or the column is empty.")
else:
    distance = np.abs(values - center) / spread
    far = distance > 2
    print("more than 2 standard deviations from the mean:", int(np.nansum(far)))
# This counts extreme rows. It does not remove them.

# %% Exercise 8 — The largest few values
valid = values[~np.isnan(values)]
if valid.size:
    order = np.argsort(valid)
    print("five smallest:", valid[order[:5]])
    print("five largest:", valid[order[-5:]])
# Write: are the largest values possible, or do they look like errors?

# %% Exercise 9 — Two numeric columns, one comparison
# EDIT NUMERIC_2. If you only have one numeric column, set NUMERIC_2 = NUMERIC
# and treat the result as a self-check (correlation with itself is 1).
other = df[NUMERIC_2].to_numpy(dtype=float)
paired = ~(np.isnan(values) | np.isnan(other))
if paired.sum() > 2 and NUMERIC_2 != NUMERIC:
    corr = np.corrcoef(values[paired], other[paired])[0, 1]
    print("rows used:", int(paired.sum()))
    print("correlation:", corr)
    # Write: does a higher first column tend to come with a higher second column?
else:
    print("Need two different numeric columns and at least 3 complete pairs.")

# %% Exercise 10 — A one-sentence finding
# In a comment or a print, answer:
# What is this file about, which numeric column did you use,
# and what is one number above that would change your mind?
