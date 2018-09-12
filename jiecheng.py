# coding=utf-8


def jiecheng(n):
    # 判断递归结束的条件
    if n == 0:
        return 1
    else:
        return n * jiecheng(n-1)


if __name__ == '__main__':
    result = jiecheng(5)
    print(result)