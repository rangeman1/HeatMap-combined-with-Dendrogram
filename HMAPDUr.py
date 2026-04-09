import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import linkage

n = int(input("Podaj liczbę elementów: "))

# Etykiety
labels = []
print("Podaj etykiety:")
for i in range(n):
    labels.append(input(f"Etykieta {i+1}: "))

# Wprowadzanie górnego trójkąta
print("\nPodawaj odległości dla par (i < j):")

matrix = np.zeros((n, n))

for i in range(n):
    for j in range(i+1, n):
        while True:
            try:
                val = float(input(f"Odległość {labels[i]} - {labels[j]}: "))
                matrix[i][j] = val
                matrix[j][i] = val  # symetria
                break
            except:
                print("Podaj poprawną liczbę!")

# przekątna = 0 (już jest, ale dla pewności)
np.fill_diagonal(matrix, 0)

print("\nMacierz odległości:")
print(matrix)

# konwersja
condensed = squareform(matrix)

# klastrowanie
linkage_matrix = linkage(condensed, method='average')

sns.clustermap(
    matrix,
    row_linkage=linkage_matrix,
    col_linkage=linkage_matrix,
    xticklabels=labels,
    yticklabels=labels,
    cmap="viridis",
    figsize=(10, 10),
    linewidths=0.5
)

plt.show()
