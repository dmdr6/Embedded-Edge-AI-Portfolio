import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Simulate local embedded telemetry (clock MHz vs power mW)
rng = np.random.default_rng(42)
clock_mhz = rng.uniform(16, 240, size=(200, 1))
power_mw = 15.0 + 1.45 * clock_mhz + rng.normal(0, 12.0, size=(200, 1))
telem = pd.DataFrame({"clock_mhz": clock_mhz.ravel(), "power_mw": power_mw.ravel()})
X = telem[["clock_mhz"]].values
y = telem[["power_mw"]].values

# 2. Visualize the data
telem.plot(kind="scatter", grid=True, x="clock_mhz", y="power_mw")
plt.axis([10, 250, 0, 420])
plt.show()

# 3. Select and train a linear model
model = LinearRegression()
model.fit(X, y)

# 4. Make a prediction at a target clock speed (180 MHz)
X_new = [[180.0]]
print(model.predict(X_new))
