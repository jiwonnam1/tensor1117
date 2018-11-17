

class MyStatic(object):
    """description of class"""

    def reset(self):   #파이선에서 메소드 선언방식임. 스태틱이란 키워드가 없이 자동으로 처리함.. 클래스 밖에 있으면 스태틱 함수가 된다...클래스안에 무조건 메소드존재
        # self는 외부에서 볼때는 없는것??

        self.x = 0  # x,y는 인스턴스 변수임.
        self.y = 0



a = MyStatic()
MyStatic.reset(a)   #  ...  a는 클래스 메소드로 ㅓ리됨..

#a.reset()  로도 사용가능함, a는 인스턴스 메소드임....


print("x값:",a.x )
print("y값:", a.y)


