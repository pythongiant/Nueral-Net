
import random
class Preceptron:
    weight=[]
    label=0
    weight.append(random.uniform(-1,1))
    weight.append(random.uniform(-1,1))
    def sign(self,a):
        if (a>0):
            label= 1
        elif(a<=0):
            label= -1
        return label    
    #Guess the output
    def guess(self,m1,m2):
        #initialise random weights
        for i in range(0,len(self.weight)):
        #    print(self.weight[i])
            pass
        output=m1*self.weight[0]+m2* self.weight[1]
        return self.sign(output)
    
    #gradient descent
    def train(self,train,label):
        guess = self.guess(train[0],train[1])
        error= label - guess
        weight=self.weight
        lr=0.1
        for i in range(len(weight)):
            weight[i]=error*train[i]*0.1
