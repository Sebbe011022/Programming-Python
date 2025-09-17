"""
Programmering med Python - Laboration 3
Sebastian
"""

import matplotlib.pyplot as plt
import numpy as np
from itertools import zip_longest

# Filnamn
input_file = "unlabelled_data.csv"
output_file = "labelled_data.csv"

# Funktion: läser in csv och returnerar lista med tuples (x, y)
def read_file_data(path):
    xy = []
    with open(path) as f:
        for line in f:
            x_str, y_str = line.strip().split(",")
            xy.append((float(x_str), float(y_str)))
    return xy

# Läs in data
xy_data = read_file_data(input_file)

# Separera x och y till numpy-arrayer
x_vals = np.array([x for x, _ in xy_data])
y_vals = np.array([y for _, y in xy_data])

# Passa en rak linje (första gradens polynom)
k, m = np.polyfit(x_vals, y_vals, 1)

# Funktion: bestämmer om en punkt är ovanför eller under linjen
def position_1st_deg(x, y, k, m):
    line_y = k * x + m
    return "above" if y > line_y else "below"

# Funktion: skapar listor med punkter ovanför respektive under linjen
def classify_points(xy, k, m):
    above = []
    below = []
    for x, y in xy:
        if position_1st_deg(x, y, k, m) == "above":
            above.append((x, y))
        else:
            below.append((x, y))
    return above, below

# Klassificera punkterna
above_list, below_list = classify_points(xy_data, k, m)

# Skriv till CSV-fil
with open(output_file, "w") as f:
    f.write("X-axis; Y-axis; Class\n")
    for above, below in zip_longest(above_list, below_list, fillvalue=None):
        if above:
            f.write(f"{above[0]}; {above[1]}; above\n")
        if below:
            f.write(f"{below[0]}; {below[1]}; below\n")

# För scatter-plot, separera koordinater
above_x = [x for x, _ in above_list]
above_y = [y for _, y in above_list]
below_x = [x for x, _ in below_list]
below_y = [y for _, y in below_list]

# Skapa plot
plt.figure(figsize=(10, 6))
plt.scatter(above_x, above_y, color="blue", label="Class above")
plt.scatter(below_x, below_y, color="red", label="Class below")
plt.plot(x_vals, k * x_vals + m, color="green", lw=1, label="Fitted line")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Labelled data")
plt.legend(loc='upper left')

# Ställ in ticks och grid
plt.xticks(range(round(min(x_vals)), round(max(x_vals)) + 1))
plt.yticks(range(round(min(y_vals)), round(max(y_vals)) + 1))
plt.grid(True)
plt.axhline(0, color="black", lw=0.5)
plt.axvline(0, color="black", lw=0.5)

# Visa plot
plt.show() 


"""
Källor:
1. NumPy dokumentation: https://numpy.org/doc/stable/
   - Används för array-hantering och beräkning av polynom (np.polyfit)
2. Matplotlib dokumentation: https://matplotlib.org/stable/contents.html
   - Används för att plotta scatter plots och linjer
3. Python itertools.zip_longest: https://docs.python.org/3/library/itertools.html#itertools.zip_longest
   - Används för att hantera listor av olika längd vid CSV-skrivning
4. Linear regression koncept:
   - https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares
   - Grundläggande formel för rak linje: y = k*x + m
"""