# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

inputs_ = sys.stdin.read()
inputs_ = [float(x) for x in inputs_.split()]

N = int(inputs_[0])
M = int(inputs_[1])

data = []
temp = []
for i in range(2, (N+1)*M+2):
    temp.append(inputs_[i])
    if len(temp) == N + 1:
        data += [temp]
        temp = []


data = map(lambda x:[1.0]+x, data)
y = map(lambda x:x[-1], data)
X = map(lambda x:x[:N+1], data)
theta = [0.0 for i in range(N+1)]

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

def gradient_descent(theta, X, y, alpha=0.01, lambda_=0.01):
    previous_theta = [x for x in theta]
    for j in range(len(previous_theta)):
        total_change = 0.0
        for i in range(len(X)):
            total_change += (dot(X[i], previous_theta) - y[i])*X[i][j]
        theta[j] = theta[j] - (alpha)/(len(X))*total_change + (lambda_/len(X))*theta[j]
    return theta

#for i in range(10000):
#    theta = gradient_descent(theta, X, y)

import numpy
X_ = numpy.array(X)
y_ = numpy.array(y)
L  = numpy.identity(X_.shape[1])
L[0][0] = 0
theta = numpy.dot(numpy.linalg.inv(numpy.dot(X_.T, X_) + 0.01 * L), numpy.dot(X_.T, y_))
#theta = numpy.polyfit(X_, y_)
    
new_samples = inputs_[(N+1)*M+2]
temp = []
new = []

for i in range((N+1)*M+3, len(inputs_)):
    temp.append(inputs_[i])
    if len(temp) == N:
        new += [temp]
        temp = []


new = map(lambda x:[1] + x, new)
for elem in new:
    print dot(elem, theta)
