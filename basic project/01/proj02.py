import numpy as np

#sample data (e.g.,years of experience vs salary)
x = np.array([1,2,3,4,5])
y = np.array([20000,30000,40000,50000,60000])

#calculate the slop(m) and intercept(b)

mean_x = np.mean(x)
mean_y = np.mean(y)

numenator = np.sum((x - mean_x)*(y - mean_y))
denomenator = np.sum((x - mean_x)**2)

m = numenator/denomenator
b = mean_y - m * mean_x

#print cofficient

print(f"calculate slop(m):{m}")
print(f"calculate intercept :{b}")

#predict y value using model

y_pred = m * x +b

# display the predict value alongside of orginal value

print("\n original vs predict :")
for i in range(len(x)):
    print(f"input:{x[i]}, Actual : {y[i]}, Predict : {y_pred[i]:.2f}")

#calculate the mean aquard error(mse)
mse = np.mean((y - y_pred)**2)
print("\n Mean squard erroe is :{mse}")
