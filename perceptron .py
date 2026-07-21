#import libraries
import numpy as np
import matplotlib.pyplot as plt

#loading the dataset
def generate_datasets():
    x = np.random.randn(100, 2)
    y = np.array([1 if x[0] + x[1] > 0 else 0 for x in x])
    return x, y

#step 2 make our perceptron class to make model
class Perceptron:
    def __init__(self, input_dim, learning_rate=0.01):
        self.learning_rate = learning_rate
        self.weight = np.zeros(input_dim+1)
        
    def predict(self, x):
        linear_output = np.dot(x, self.weight[1:])+self.weight[0]
        #self.weight = array[0.0,0.0,0.0] index[0] -- bias and index[1:] -- weight
        return np.where(linear_output >= 0.0, 1, 0)
    
    def train(self,x,y,epochs = 10):
        for _ in range(epochs):
            for xi, target in zip(x,y):
                update = self.learning_rate * (target - self.predict(xi))
                self.weight[1:] = self.weight[1:] + update * xi
                self.weight[0] = self.weight[0] + update

x, y = generate_datasets()
p = Perceptron(input_dim=2)
p.train(x, y, epochs=10)

#step 4:visualize the decision boundary
def plot_decision_boundary(x, y, model):
    x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', marker='o')
    plt.title('Perceptron Decision Boundary')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
plot_decision_boundary(x, y, p)