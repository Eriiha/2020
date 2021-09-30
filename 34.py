# 일반 함수
def square(x):
    return x * x

print(square(5))

# 퍼스트클래스 함수
f = square # 별명
print(f is square)
print(square, f)
print(id(square), id(f))

print(f(5))
#2. 인자로써 다른 함수에 전달
def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result
num_list = [1,2,3,4,5]
squares = my_map(square_1, num_list)
print(type(squares))
#
def square_2(x):
    return x * x
num_list_1 = num_list
def simple_square(arg_list):
    result = []
    for i in arg_list:
        result.append(i * i)
    return result
simple_squares = simple_square(num_list_1)
print(simple_squares)
#
def square(x):
    return x * x
def cube(x):
    return x * x * x
def quad(x):
    return x * x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
        return result

num_list = [1,2,3,4,5]

squares = my_map(square, num_list)
cubes = my_map(cube, num_list)
quads = my_map(quad, num_list)
print(squares)
print(cubes)
print(quads)
#
def logger(msg):
    
    def log_message():
        print('Log: ' + msg)
    return None #msg + " rara!"

print(logger("joono"))