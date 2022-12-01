def func1(a, b):
    print(f'{a} 곱하기 {b} = {a * b}')

func1(10, 30)

def dong1():
    c = "안녕하세요"
    return c

a = dong1()
print(a)

def dong2(num):
    for i in range(1, 10):
        print(f'{num}곱하기{i}={num*i}')

dong2(3)