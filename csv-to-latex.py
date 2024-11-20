import os
import pandas as pd

file_name = "scores.csv"
file_prefix, = file_name.split()
latex_string = ""

df = pd.read_csv(file_name)
max_cols = list(df.max()[:-1])
df.iloc[1], df.iloc[2] = df.iloc[2].copy(), df.iloc[1].copy()
for index, row in df.iterrows():
    row_data = ""
    for i, el in enumerate(row[:-1]):
        if el == max_cols[i]:
            row_data += f" & \\textbf{{{el}}}"
        else:
            row_data += f"& {el}"
    latex_string += row_data + r" \\" + "\n"

latex_string += "\\midrule" + "\n"

with open(f'{file_prefix}.txt', 'w') as file:
    file.write(latex_string)
