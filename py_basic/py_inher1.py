class Pet(object):
    def __init__(self,name,specis ):  # private 이다..코드 마니 생략한다..메소드는 : 필수
        self.name = name
        self.specis = specis 

    def getName(self):   # getter 
        return self.name 
    def getSpecis(self):
        return self.specis


    def __str__(self):
        return "동물정보"



class Dog(Pet):   #상속처리됨.
    def __init__(self,bow):
        self.bow = bow

class Cat(Pet):
    def __init__(self,yam):
        self.yam = yam


    




