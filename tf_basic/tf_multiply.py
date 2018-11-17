import tensorflow as tf

a = tf.placeholder("float")
b = tf.placeholder("float")

y = tf.multify(a,b)

sess = tf.Session()  #생성자임..대분자로 시작...생성자-클래스 있어야 함..

print (sess.run(y, feed_dict={a:3, b: 3}))



