# NumPy exercise for VS Code.
# Run a cell: click it and press Shift+Enter (or Run Cell).
# Cells start with the comment "# %%".
# This file uses a tiny built-in example. It does not depend on a course week.

# %% Imports
import numpy as np
import pandas as pd

# %% 1. A column is an array
# A Python list is visited one cell at a time.
# A NumPy array is the same numbers kept as one block.
scores_list = [18, 21, 19, 30, 24]
scores = np.array(scores_list)

print(scores)
print("dtype:", scores.dtype)
print("shape:", scores.shape)
# Write one line: how many values, and what shape reports.

# %% 2. Math on the whole column
bumped = scores + 1
print("array:", bumped)

bumped_loop = []
for value in scores_list:
    bumped_loop.append(value + 1)
print("loop:", bumped_loop)
# Write one line: do the two results match, and which version states the job more directly?

# %% 3. Summaries
print("mean:", scores.mean())
print("sum:", scores.sum())
print("min:", scores.min(), "max:", scores.max())
# Write one line: what the mean tells you that the max does not.

# %% 4. A yes/no filter
above_20 = scores > 20
print(above_20)
print(scores[above_20])
print("how many:", int(above_20.sum()))
# True counts as 1, so sum() is a count of the True values.

# %% 5. From a pandas column to an array and back
df = pd.DataFrame(
    {
        "name": ["A", "B", "C", "D", "E"],
        "score": [18, 21, 19, 30, 24],
    }
)
column = df["score"].to_numpy()
print(column)
print("mean:", column.mean())
df["score_plus_1"] = column + 1
print(df.head())
# to_numpy() keeps the numbers. The name column stays on the table.
