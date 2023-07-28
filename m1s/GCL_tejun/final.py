import numpy as np
import tensorflow as tf
import tensorflow.contrib.layers as c_layers
import matplotlib.pyplot as plt

from keras.datasets import mnist

class CRNN_Model():
    def __init__(self,hidden_size=256,batch_size=128,sequence_size=2,img_size=28,output_size=19):
        self.hidden_size=hidden_size
        self.batch_size=batch_size
        self.sequence_size=sequence_size
        self.output_size=output_size

        self.input=tf.placeholder(tf.float32,shape=[sequence_size,None,img_size,img_size,1])
        self.correct=tf.placeholder(tf.float32,shape=[None,output_size])

        self.model=self.build_model()
        self.graph = self.build_graph()
        self.test=self.test_model()

    def build_model(self):
        #cnn
        hidden_list=[]
        for i in range(self.sequence_size):
            conv1 = tf.layers.conv2d(self.input[i], filters=16, kernel_size=[3, 3]
                                     , strides=[1, 1],padding='same', activation=tf.nn.elu)
            max_pooling1 = tf.layers.max_pooling2d(conv1, pool_size=[2, 2], strides=[2, 2])
            conv2 = tf.layers.conv2d(max_pooling1, filters=16, kernel_size=[3, 3]
                                     , strides=[1, 1], padding='same', activation=tf.nn.elu)
            max_pooling2 = tf.layers.max_pooling2d(conv2, pool_size=[2, 2], strides=[2, 2])
            flatten = c_layers.flatten(max_pooling2)
            hidden=tf.layers.dense(flatten,self.hidden_size,activation=tf.nn.elu,
                                      kernel_initializer=c_layers.variance_scaling_initializer())
            hidden_list.append(hidden)

        self.hidden_list=tf.transpose(hidden_list,perm=[1,0,2])

        #rnn
        rnn_cell = tf.nn.rnn_cell.BasicRNNCell(self.hidden_size)
        self.initial_state = rnn_cell.zero_state(self.batch_size, tf.float32)
        state = self.initial_state
        outputs = []
        for t in range(self.sequence_size):
            (output, state) = rnn_cell(self.hidden_list[:,t,:], state)
            outputs.append(output)
        self.outputs = outputs

        self.prediction = tf.layers.dense(self.outputs[-1], self.output_size)
        self.pred_output = tf.nn.softmax(self.prediction)

    def build_graph(self):
        self.loss=tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(labels=self.correct,logits=self.prediction))
        optimizer=tf.train.AdamOptimizer(learning_rate=0.001,beta1=0.9,beta2=0.999)
        self.train_step=optimizer.minimize(self.loss)

    def test_model(self):
        correct_pred=tf.equal(tf.argmax(self.pred_output,1),tf.argmax(self.correct,1))
        self.accuracy=tf.reduce_mean(tf.cast(correct_pred,tf.float32))
