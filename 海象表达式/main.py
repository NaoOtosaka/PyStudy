# 语法说明
# := 将给变量赋值, 这个变量是更大的表达式的一部分

a = "This is a test case"

# 海象表达式本身作为一个更大的表达式，可以赋值给某一变量，例如
expression = (n := len(a))
print(expression)  # 19

# ===================================================================================================================

# 将 n := len(a) 作为一个表达式，进行条件判断
# 一般写法
if len(a) > 10:
    print(f"({a})长度为{len(a)} => 字符长度大于10")  # (This is a test case)长度为19 = > 字符长度大于10

# 使用海象表达式
if (a_len := len(a)) > 10:
    print(f"({a})长度为{a_len} => 字符长度大于10")  # (This is a test case)长度为19 = > 字符长度大于10

# 相比一般写法，使用海象表达式可以避免使用两次len()

# ===================================================================================================================

# 循环读取文件时，可以使用海象表达式作为While迭代读取文件的判断条件
file = open("demo.txt", "r", encoding='UTF-8')

# 一般写法
while True:
    line = file.readline()
    if not line:
        break
    print(line.strip())

# 使用海象表达式
while line := file.readline():
    print(line.strip())

# ===================================================================================================================

# 使用while实现命令行交互输入时，可以使用海象表达式进行判断
password = "test"

# 一般写法
while True:
    pw = input("输入密码：")
    if pw == password:
        break

# 使用海象表达式
while (pw := input("输入密码：")) != password:
    continue

# ===================================================================================================================

# 推导式中使用海象表达式
# 查出所有会员中过于肥胖的人的 bmi 指数，给出bmi计算函数get_bmi()
members = [
    {"name": "小五", "age": 23, "height": 1.75, "weight": 72},
    {"name": "小李", "age": 17, "height": 1.72, "weight": 63},
    {"name": "小陈", "age": 20, "height": 1.78, "weight": 82},
]


def get_bmi(info: dict) -> tuple[str, int]:
    """
    计算bmi指数
    :param info:
    :return:
    """
    height = info["height"]
    weight = info["weight"]
    return info['name'], weight / (height ** 2)


fat_bmi = [bmi for i in members if (bmi := get_bmi(i))[1] > 24]
print(fat_bmi)  # [('小陈', 25.88057063502083)]
