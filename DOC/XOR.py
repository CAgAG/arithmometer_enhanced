""" 异或
0异或任何数，其结果=任何数
1异或任何数，其结果=任何数取反   ---> 1->0, 0->1
任何数异或自己，等于把自己置0
"""

if __name__ == '__main__':
    a = 0
    b = 1

    a = a ^ b
    b = a ^ b
    a = a ^ b

    print(a, b)
