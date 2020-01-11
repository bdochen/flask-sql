class student(object):
    # 定义构造方法
    def __init__(self, n, a):  # __init__() 是类的初始化方法；它在类的实例化操作后 会自动调用，不需要手动调用；
        # 设置属性
        self.name = n
        self.age = a

    # 定义普通方法
    def tell(self):
        print("%s 说：我今年%s岁" % (self.name, self.age))

    def __str__(self):
        return "名字：%s 年龄：%d" % (self.name, self.age)
#__str__为专有用法
#https://www.cnblogs.com/an-wen/p/11582222.html
#https://blog.csdn.net/pdstar/article/details/90900944
# 类student 实例化一个对象john
john = student("约翰", 19)

# 调用类中的 speak()方法
john.tell()
print(john)


