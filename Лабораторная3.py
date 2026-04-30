###Лабораторная3
import statsmodels.api as sm
import matplotlib.pyplot as plt
data = sm.datasets.interest_inflation.load_pandas().data
print("Названия колонок:", data.columns.tolist())
print("Первые 5 строк:")
print(data.head())
year_col = 'year' 
filtered = data[(data[year_col] >= 1980) & (data[year_col] <= 1990)]
print(filtered)
plt.figure(figsize=(10, 6))
for column in filtered.columns:
    if column != year_col:  
        plt.plot(filtered[year_col], filtered[column], label=column)
plt.xlabel('Год')
plt.ylabel('Значение')
plt.title('Динамика временных рядов (interest_inflation)\n1980-1990 годы')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()