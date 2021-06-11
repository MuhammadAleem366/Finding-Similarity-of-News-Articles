import numpy as np
'''training_inputs = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
training_outputs = np.array([[0,1,1,0]]).T
#weights = [3.1,2.1,8.7]
#bias = 3
#output = 0.0
##   mul_num = inputs[x] * weights[x]
  #  output = output + mul_num
#print(output+bias)
def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_derivative(x):
    return x * (1-x)
np.random.seed(1)
synaptics_weights = 2 * np.random.random((3,1))-1
print('Random starting synaptic weights : ' )
print(synaptics_weights)
for iteration in range(100000):
    input_layer = training_inputs
    output = sigmoid(np.dot(input_layer,synaptics_weights))
    error = training_outputs - output
    adjustments = error * sigmoid_derivative(output)
    synaptics_weights += np.dot(input_layer.T,adjustments)
print('synaptic weights after Training')
print(synaptics_weights)
print('output after training : ')
print(output)'''
# sigmoid is an activation function and it calculates the probability
def sigmoid(x , deriv=False):
    if (deriv == True):
        return (x*(1-x))
    return 1/(1+np.exp(-x))
# training input  data ...
x = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
# y is output training data and every value is associate to the value of x
y = np.array([[0],[1],[1],[0]])
# seed
np.random.seed(1)
# synapsis or weights associated with inputs
syn1 = 2 * np.random.random((3,4))-1
syn2 = 2 * np.random.random((4,1))-1
# training th  data and creating layers
for j in range(60000):
    l0 = x
    l1 = sigmoid(np.dot(l0,syn1))
    l2 = sigmoid(np.dot(l1,syn2))
    # back propagation
    l2_error = y-l2
    if (j % 10000)==0:
        print("Error: " + str(np.mean(np.abs(l2_error))))
    l2_delta = l2_error * sigmoid(l2,deriv=True)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * sigmoid(l1,deriv=True)

    # updating the weights
    