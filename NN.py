#!/usr/bin/python3
from preceptron import Preceptron
import matplotlib.pyplot as plt
import random 

brain=Preceptron()

for point in range(0,50):
    X=random.randint(1,50)
    Y=random.randint(1,50)
    if(X>Y):
        plt.scatter(X,Y,marker=".")
        answer=1
    else:
        plt.scatter(X,Y,marker="o")    
        answer = -1
    train_set= [X,Y]
    brain.train(train_set,brain.label)
    guess = brain.guess(X,Y)
    print(guess)
    print("actual="+str(answer))
for i in range(0,60):
    plt.scatter(i,i,marker="D")    


    

plt.show()
