import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Download and prepare the data
data_root = "https://github.com/ageron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# 2. Visualize the data
lifesat.plot(
    kind="scatter", grid=True, x="GDP per capita (USD)", y="Life satisfaction"
)
plt.axis([23_500, 62_500, 4, 9])
plt.show()

# 3. Select a linear model
model = LinearRegression()

# 4. Train the model
model.fit(X, y)

# 5. Make a prediction for Cyprus
X_new = [[37_655.2]]  # Cyprus' GDP per capita in 2020
print(model.predict(X_new))  # output: [[6.30165767]]
