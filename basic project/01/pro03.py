import numpy as np

# 1. Sample Data (e.g., Years of Experience vs Salary)
x = np.array([1, 2, 3, 4, 5])       # Independent variable
y = np.array([20000, 25000, 30000, 35000, 40000])  # Dependent variable

# 2. Calculate the slope (m) and intercept (b)
mean_x = np.mean(x)
mean_y = np.mean(y)

numerator = np.sum((x - mean_x) * (y - mean_y))
denominator = np.sum((x - mean_x)**2)

m = numerator / denominator
b = mean_y - m * mean_x

# Print coefficients
print(f"Calculated Slope (m): {m}")
print(f"Calculated Intercept (b): {b}")

# 3. Predict y values using the model
y_pred = m * x + b

# 4. Display predictions alongside original values
print("\nOriginal vs Predicted:")
for i in range(len(x)):
    print(f"Input: {x[i]}, Actual: {y[i]}, Predicted: {y_pred[i]:.2f}")

# 5. Calculate Mean Squared Error (MSE)
mse = np.mean((y - y_pred) ** 2)
print(f"\nMean Squared Error (MSE): {mse}")
