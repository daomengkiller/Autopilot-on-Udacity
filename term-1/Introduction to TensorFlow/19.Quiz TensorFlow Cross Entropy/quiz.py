# Solution is available in the other solution.py tab
import tensorflow as tf

softmax_data = [0.7, 0.2, 0.1]
one_hot_data = [1.0, 0.0, 0.0]

softmax = tf.placeholder(tf.float32)
one_hot = tf.placeholder(tf.float32)

# TODO Print cross entropy from session
cross_entropy=tf.reduce_sum(-tf.multiply(one_hot,tf.log(softmax)))
with tf.Session() as sees
    print(sees.run(cross_entropy,feed_dict={softmaxsoftmax_data,one_hotone_hot_data}))
    