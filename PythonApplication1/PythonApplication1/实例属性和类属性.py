class Student(object):
    def __init__(self, name):
        self.name =name

s = Student('Bob')
s.score = 90
s.hello="123456"
print("实例s的属性:",s.score,s.name,s.hello)


class Student(object):
    name = 'Student'
s = Student() # 创建实例的对象s
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name) # 打印类的name属性
s.name = 'Michael' # 给实例对象s绑定name属性
print(s.name) # 由于实例s属性优先级比类属性高
              #所以它会屏蔽掉类的name属性
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
#千万不要对实例属性和类属性使用相同的名字，
#因为相同名称的实例属性将屏蔽掉类属性，
#但是当你删除实例属性后，再使用相同的名称，
#访问到的将是类属性。