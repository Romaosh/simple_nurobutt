import pandas as pd

# Данные
# 1. Данные для единичного аккумулятора
data = {
    "Capacity_mAh": [3000, 1500, 2000, 2500, 1800, 4000, 3500, 2500],
    "Voltage_V": [3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7],
    "Weight_g": [45, 25, 35, 40, 28, 50, 48, 38],
    "Energy_Density_Wh_per_kg": [250, 160, 260, 350, 150, 240, 300, 270],
    "Cycle_Life": [1500, 3000, 2000, 5000, 3500, 1500, 4500, 2000],
    "Chemistry": [
        "Li-ion (NMC)", "Li-ion (LFP)", "Li-ion (NCA)",
        "Solid-state", "Li-ion (LFP)", "Li-ion (NMC)",
        "Solid-state", "Li-ion (NCA)"
    ]
}


# Создание DataFrame
df = pd.DataFrame(data)

# Сохранение в CSV
csv_file = "battery_data.csv"
df.to_csv(csv_file, index=False)

print(f"CSV-файл создан: {csv_file}")