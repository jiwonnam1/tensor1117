import tensorflow as tf

a = tf.placeholder("float")
b = tf.placeholder("float")

y = tf.multify(a,b)

sess = tf.Session()  #생성자임..대분자로 시작...생성자-클래스 있어야 함..

print (sess.run(y, feed_dict={a:3, b: 3}))

# tf는 tf.로 시작... 클래스로 무조건 만들어서 처리...
# 
# 
#
# 은닉화 class화
# 상속
# 추상화(자바) -> 인터페이스 - > 함수 형태, 클래스로 이용안함....
# 다형성(자바) -> 다중 상속
# 
# 
#  
#
#


