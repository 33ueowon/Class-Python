# star 함수 정의
def star(x,*y):
    for i in y:
        print(x*y)
    star(",",3)
    star(".",1,2,3)

