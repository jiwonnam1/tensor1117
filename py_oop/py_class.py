#
#    class declare 파일이름과 클래스명이 틀려도 상관없다..
#


#object 생략가능 함. 
#class MyClass(object):
#class MyClass():

class MyClass:
    """description of class"""
    pass  #빈클래스 만듬
    
a = MyClass()  # new 클래스 생성함.

b = MyClass()
print(a)  #클래스의 주소값이 출력
print(b)




