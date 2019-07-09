#import numpy as np
import Neuron as n

list=[[1,1],[1,0],[0,1],[0,0]]

def andGate(w1,w2,b):
    n.feed_forward(list[0][0],list[0][1],w1,w2,b)

def main():
    w1=input("enter weight1:")
    w2=input("enter weight2:")
    b=input("enter bias")
    print(andGate(w1,w2,b))
        
class Neuron:
    def relu(z):
        return max(0,z)
    
    def feed_forward(x1,x2,w1,w2,b):
        Z=x1*w1+x2*w2+b
        return relu(Z)
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

if __name__=='__main__':
        main()
