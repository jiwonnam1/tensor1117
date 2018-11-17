from Person import Person
# import Person 도 가능함.. 파일명과 클래스명이 동일시에.....

def main():

    maria = Person("마리아 ",20,"서울시") 

    maria.greeting()

# public static main() 과 같은 부분...
if __name__ == "__main__" :  # __로 실행하면 프라이빗으로 외부에서 접근 못한다..파이션 에서 __main__ 을 가지고 있는 이름이 1개만 있어야한다....엔트리진입점.
    main()
