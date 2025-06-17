import numpy as np
import matplotlib.pyplot as plt

# 1. Sample Data (Years of Experience vs Salary)
x = np.array([1, 2, 3, 4, 5])       # Input (Years)
y = np.array([20000, 25000, 30000, 35000, 40000])  # Output (Salary)

# 2. Calculate the coefficients (m = slope, b = intercept)
n = len(x)
mean_x = np.mean(x)
mean_y = np.mean(y)

# Using the formula for slope and intercept
numerator = np.sum((x - mean_x) * (y - mean_y))
denominator = np.sum((x - mean_x)**2)
m = numerator / denominator
b = mean_y - m * mean_x

print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# 3. Make predictions
y_pred = m * x + b

# 4. Plot the data and regression line
plt.scatter(x, y, color='blue', label='Actual')
plt.plot(x, y_pred, color='red', label='Predicted Line')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.title("Linear Regression using NumPy")
plt.show()

# 5. Evaluate the model (Mean Squared Error)
mse = np.mean((y - y_pred)**2)
print(f"Mean Squared Error: {mse}")
