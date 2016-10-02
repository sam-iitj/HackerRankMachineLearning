# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import matplotlib.pyplot as plt 

inputs_ = sys.stdin.read()
inputs_ = [float(x) for x in inputs_.split()]

#data = zip(inputs_[len(inputs_)/2:], inputs_[:len(inputs_)/2])
data = zip(inputs_[:len(inputs_)/2], inputs_[len(inputs_)/2:])
data = map(lambda x:[1.0]+list(x), data)
y = map(lambda x:x[-1], data)
X = map(lambda x:x[:2], data)
theta = [0.0 for i in range(2)]

print X
print y 

def dot(x, y):
    sum_ = 0.0
    for i in range(len(x)):
        sum_ += x[i] * y[i]
    return sum_

def cost(theta, X, y):
    cost_ = 0.0
    for i in range(len(X)):
        cost_ += (dot(X[i], theta) - y[i])**2
    cost_ = cost_/(2 * len(X))
    return cost_

def gradient_descent(theta, X, y, alpha=0.1):
    previous_theta = [x for x in theta]
    for j in range(len(previous_theta)):
        total_change = 0.0
        for i in range(len(X)):
            total_change += (dot(X[i], previous_theta) - y[i])*X[i][j]
        theta[j] = theta[j] - (alpha)/(len(X))*total_change
    return theta

for i in range(10000):
    theta = gradient_descent(theta, X, y, alpha=0.01)

pred = [dot(x, theta) for x in X]
    
print theta
plt.scatter(map(lambda x:x[1], X), y)
plt.plot(map(lambda x:x[1], X), pred)
plt.show()
