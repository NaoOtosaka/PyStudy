# 推导式 comprehensions（又称解析式），是 python 的一种独有特性。推导式是可以从一个数据序列构建另一个新的数据序列。

# 列表推导式
# 语法：
# 变量名 = [表达式 for 变量 in 列表 for 变量 in xxx]
# 变量名 = [表达式 for 变量 in 列表 if 条件]
# 语义：
# 遍历出列表中的内容给变量，表达式根据变量值进行逻辑运算。或者遍历列表中的内容给变量，然后进行判断，符合的值在给表达式。

# 例1：创建一个包含元素1-10的列表
example_one = [i for i in range(1, 11)]
print(example_one)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 例2：创建一个包含1-10之间所有偶数的列表
example_two = [i for i in range(1, 11) if i % 2 == 0]
print(example_two)  # [2, 4, 6, 8, 10]

# 例3：现在有一列表 lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] ，求出 1/4/7 和 1/5/9元素
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
example_three = [lst[i][0] for i in range(len(lst))]
example_four = [lst[i][i] for i in range(len(lst))]
print(example_three)  # [1, 4, 7]
print(example_four)  # [1, 5, 9]

# 字典推导式
# 字典推导式列表推导式思想的延续，语法差不多，只不过产生的是字典而已。

# 例4:将字典中的 key 和 value 进行对换。
dic = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

example_five = {value: key for key, value in dic.items()}
print(example_five)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 集合推导式
# 集合推导式跟列表推导式非常相似，唯一区别在于用 {} 代替 []
# 生成的集合同样具有元素唯一性

tuple_demo = (1, 1, 2, 3, 4, 5, 6, 6)

example_six = {x for x in tuple_demo}
print(example_six)  # {1, 2, 3, 4, 5, 6}

example_seven = {x for x in tuple_demo if x % 2 == 0}
print(example_seven)  # {2, 4, 6}
