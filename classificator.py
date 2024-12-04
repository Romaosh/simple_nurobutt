import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn import tree


# Преобразование данных в DataFrame
df = pd.read_csv("battery_data.csv")

# Разделение признаков и целевой переменной
X = df[["Capacity_mAh", "Voltage_V", "Weight_g", "Energy_Density_Wh_per_kg", "Cycle_Life"]]
y = df["Chemistry"]

# Кодирование категориальной переменной (целевой)
y_encoded = y.astype('category').cat.codes

# 2. Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# 3. Обучение модели дерева решений
clf = DecisionTreeClassifier(random_state=42, max_depth=10)  # Ограничиваем глубину для наглядности
clf.fit(X_train, y_train)

# 4. Оценка модели
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 5. Визуализация дерева решений
plt.figure(figsize=(16, 10))
tree.plot_tree(
    clf,
    feature_names=X.columns,
    class_names=y.astype('category').cat.categories,
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("Decision Tree for Battery Chemistry Classification")
plt.show()