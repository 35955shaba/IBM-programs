# MULTILAYER PERCEPTRON USING KERAS
import tensorflow as tf 
from tensorflow import keras 
from keras.layers import Dense,Flatten
from keras.models import Sequential
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from keras.datasets import mnist
(x_train,y_train),(x_test,y_test) = mnist.load_data()
print("X_train shape:",x_train.shape)
print("X_test shape:",x_test.shape)
print("Y_train shape:",y_train.shape)
print("Y_test shape:",y_test.shape)

plt.figure(figsize=(6,6))
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(x_train[i],cmap = "gray")
    plt.title(f"digit: {y_train[i]}")
plt.tight_layout()
plt.show()

new_x_train = x_train/256.0
new_x_test = x_test/256.0

model = Sequential()
model.add(Flatten(input_shape=(28,28)))
model.add(Dense(128,activation = "relu"))
model.add(Dense(64,activation="relu"))
model.add(Dense(32,activation="relu"))
model.add(Dense(10,activation="softmax"))

model.summary()

model.compile(loss = "sparse_categorical_crossentropy",optimizer = "adam")
data = {}
for i in range(1,6):
    model.fit(new_x_train,y_train,epochs=10)
    pred = model.predict(new_x_test)
    pred[0]
    y_pred = pred.argmax(axis = 1) 
    print(y_pred)
    acc = accuracy_score(y_test,y_pred)
    data[i] = acc