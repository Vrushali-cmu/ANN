import numpy as np
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import FeedForwardNetwork, LinearLayer, TanhLayer, FullConnection
from pybrain.datasets import SupervisedDataSet

# To test, create array:
# 
# import numpy as np
# a = array([[ 1,  0,  0,  1,  1,  1,  0,  0], [ 0,  0,  1,  0,  1,  1,  0,  1], [ 0,  0,  1,  1,  1,  0,  0,  1]])
# from mlp import MLP
# net = MLP(3)
# net.train(a,3)
# ⁠⁠⁠net.test((1,0,0),8)

class MLP:
  def __init__(self, numMolecules):
    self.nm = numMolecules
    network = buildNetwork(numMolecules, numMolecules, numMolecules, hiddenclass=TanhLayer)
    self.network = network

  def train(self, input, epochs):
    nm = self.nm
    ds = SupervisedDataSet(nm, nm)
    ds.setField('input', np.transpose(np.delete(input,0,1)))
    ds.setField('target', np.transpose(np.delete(input,input.shape[1]-1,1)))
    trainer = BackpropTrainer(self.network, ds)
    for index in range(epochs):
      trainer.train()

  def test(self, input, ts):
    net = self.network
    res = np.zeros((self.nm, ts))
    res[:,0] = input
    for i in range(2,ts-1):
      res[:,i] = net.activate(res[:,i-1])
    return res
