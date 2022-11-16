#import libraries and dataset functions
from keras import Model
import keras.layers as layers
import keras.utils as utils
import keras.optimizers as optimizers
from keras.regularizers import l2
import numpy as np


#initialize model
class ChessModel(Model):
    def __init__(self):
        super(ChessModel, self).__init__()
        self.cd1 = layers.Conv2D(filters=256, kernel_size=5, activation="relu", padding="same",
        use_bias=False, kernel_regularizer=l2(1e-4))
        self.bn = layers.BatchNormalization()
        self.cd2 = layers.Conv2D(filters=256, kernel_size=3, padding="same",
        use_bias=False, kernel_regularizer=l2(1e-4))
        self.bn1 = layers.BatchNormalization(axis=1, name="policy_batchnorm")
        self.cd3 = layers.Conv2D(filters=2, kernel_size=1, 
        use_bias=False, kernel_regularizer=l2(1e-4))
        self.bn2 = layers.BatchNormalization(axis=1, name="policy_batch")
        self.a = layers.Activation("relu")
        self.f = layers.Flatten()
        self.p = layers.Dense(1, kernel_regularizer=l2(1e-4), activation="softmax")

    def call(self, inputs):
        x = self.cd1(inputs)
        x = self.bn(x)
        x = self.cd2(x)
        x = self.bn1(x)
        x = self.cd3(x)
        x = self.bn2(x)
        x = self.a(x)
        x = self.f(x)
        return self.p(x)
    
    def build_graph(self):
        x = layers.Input((18, 8, 8))
        return Model(inputs=[x], outputs=self.call(x))

model = ChessModel()
model.compile(
     loss = 'mse',
     metrics = ['mse'],
     optimizer = optimizers.Adam(learning_rate=0.001))
# raw_input = (1000, 18, 8, 8)
# model(np.zeros(shape=(raw_input)))   
# print("weights:", len(model.weights))
# print("trainable weights:", len(model.trainable_weights))
# model.build_graph().summary()

class Agent(object):
    def __init__(self):
        pass
    
    def train(self):
        pass

    def evaluate(self):
        pass