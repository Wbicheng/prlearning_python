"""
python教程：
https://www.w3school.com.cn/python/index.asp
"""


x="lokk";#函数外为全局变量
def my_func():
    global a; #函数内定义全局变量的方法 不能在此赋值
    a="me";
    print(a);


"""
This is a comment
"""
my_func();

#数据类型
s=str("hero");#指定数据类型
#数字
x = 10    # int
y = 6.3  # float
z = 2j   # complex
print(type(x));
import random  #生成随机数的模块
print(random.randrange(1,10))

#字符串
c , d = 'hello',"world";  # ' and " all right
print("c="+c,d);
a="""ahda,hfhsh  #多行字符串赋值方法  ' "均可
das
hd"""
#Python无字符类型，字符即长度为1的字符串
print(a[0:3]);#包括右区间
print(a[-3:-1]);
print(a.split(','));#通过‘，’分割字符串
c='aha' in a;#a中是否有aha
print(c);
#输出组合字符串与数字
num1=10;num2=11;
text="num1={0},num2={1}";
print(text.format(num1,num2));

#bool 布尔类
print(bool("10101"));
"""
bool()可以评估内容，有内容为Ture，反之为Fals 除0外任何数字为True
除了空列表，其他的列表，元祖，集合和字典都为True
"""

#运算符
#算术运算符
print(5/2);#2.5
print(5%2);#取模  1
print(5//2);#整除 2
print(5**2);#取幂 25
#位运算符  &   |    ^     ~(not)  >>  <<
print(5^3);#异或6
#赋值运算符
x=5;
x+=5;
#比较运算符
print(x!=10);
#逻辑运算符 and or not
print(not(x!=10));
#身份运算符 比较对象是否是同一对象，即占相同内存空间
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z);#True
print(x is y);#False
print(x != y);#False  != 比较内容是否一致

#四种集合数据类型 List 列表  Tuple 元组  Set 集合 Dictionary 字典
#列表：有序可更改 允许重复，用[]编写
thislist=["ada","asda","asd"];
thislist1=list(("ada","asda","asd"));#也可以使用list()创建
print(thislist[0]);#通过引用索引号访问列表项  -1表示最后一项
print(thislist[-2:-1]);#b不包括右区间
for x in thislist: #使用for遍历
    print(x);
if("ada" in thislist): #某项是否存在
    print("Yes");
print(len(thislist));#列表长度
thislist.append("aaa");#追加项目到列表末尾
thislist.insert(1,"insert");#在指定索引插入项目
thislist.remove("ada");#删除某项
thislist.pop(1);#删除指定索引
thislist.clear();#列表清空
thislist=thislist+thislist1;#连接
del thislist[0];#删除指定索引
del thislist;#删除整个列表

#元组 有序 不允许更改 可以重复 用()编写
thistuple=("121","aad","s1");
thistuple1 = tuple(("apple", "banana", "cherry")) #注意双括号
print(thistuple[1]);#访问第二项
print(thistuple[-2:-1]);#不包括右区间
y=list(thistuple);y[1]="112";thistuple=tuple(y);#元组不允许更改，但是可以通过先转换为列表，再转换回来进行修改
for x in thistuple: #使用for遍历
    print(x);
if ("ada" in thistuple):  # 某项是否存在
    print("Yes");
print(len(thistuple));#元组长度
thistuple=thistuple+thistuple1;#连接
#无法向元组添加项目
#无法删除元组中项目
del thistuple; #删除元组

#集合 无序 无索引 不可重复 使用{}编写
thisset={"as","123","asd"};
thisset1=set(("1","12"));
#set无序，无索引，可以通过in判断是否存在，或者for遍历
for x in thisset:
    print();
#无索引无法更改，可以添加
thisset.add("12");
thisset.update(["as","21312"]);#update增加多项 必须加[]!否则为单个字符
print(len(thisset));
thisset.remove("as");#删除项目 也可用discard
x=thisset.pop();#只能删除最后一项，并返回
thisset.clear();#清空集合
thisset=thisset.union(thisset1);#连接 会排除重复项
del thisset;#删除集合

#字典 无序 有索引 不允许重复 用{} 编写 key-value
thisdict={"asa":"qwe","sdas":"asdsa"};
thisdict1=dict(brand="Porsche", model="911", year=1963);
#嵌套
child1 = {
  "name" : "Phoebe Adele",
  "year" : 2002
}
child2 = {
  "name" : "Jennifer Katharine",
  "year" : 1996
}
myfamily = {
  "child1" : child1,
  "child2" : child2
}
print( myfamily["child1"]["name"]);
x=thisdict["asa"];#访问项目
x=thisdict.get("asa");#同上
thisdict["asa"]="ass";#更改
for x in thisdict:#遍历字典，返回键
    print(x);
for x in thisdict:#遍历字典，返回值
    print(thisdict[x]);
for x in thisdict.values():#作用同上
    print(x);
for x,y in thisdict.items():#遍历键和值
    print(x,y);
print("asa" in thisdict);#字典中是否存在指定键
print(len(thisdict));#字典中键值对数
thisdict["c"]="b";#添加项目
thisdict.pop("c");#输出具有指定键名的项
del thisdict["sdas"];#同上
thisdict.clear();#清空字典
del thisdict;#删除整个字典

#if
a=1;b=2;
if a>1:
    print("a>b");
elif a==b:
    print("a==b");
else:
    pass;#无意义

#while
i=1;
while(i<7):
    i+=1;
    print(i);
    if(i==3):
        continue;
    if(i>3):
        break;
else: #可选，表示条件不成立
    print("i不再小于7");

#for
#可以迭代序列（列表，元组，集合，字典，字符串）
fruits=["a","b","c"];
for x in fruits:
    print(x);
#循环一组代码一定次数
for x in range(10):#从0开始，不包括10  可以range(3,6) 3 4 5
    print(x);
for x in range(2,15,3):#第三个参数为增量
    print(x);
else:
    print("stop");#循环结束时打印

#函数
def my_func(c="now"):#设置默认参数
    print(c);
my_func();

def list_second_item(l):
    return l[1];#返回值

list=["11","1"];
print(list_second_item(list));

def my_func2(c1,c2):#关键字参数
    print("a"+c1);
my_func2(c1="1",c2="3");

def my_func3(*k):#任意参数
    print(k[1]);
my_func3("1","2","3");

#作用域  python在代码主体创建的变量为全局变量 若在函数外部和内部使用同名变量，则或许独立
#除非在函数内部用上global进行声明
x=100;
def my_func():
    global x;
    print(x);


#lambda函数  简化函数的写法
x=lambda a:a+10; #函数名为x 输入参数为a 函数体为a+10
print(x(10));

#类与对象 python内部所有内容都为对象，拥有属性和方法
class myClass():
    x=5;
class Person():
    name="me";
    age=12;
    def __init__(self,name,age): #启动类时执行 每次在使用类创建新对象时会自动调用
        self.name=name;#self表示对类当前实例的引用，必须写入参数列表中
        self.age=age;
    def myfunc(self):
        print(self.name);
    def myfunc2(myself):#不一定要self，可以命名为其他
        print(myself.age);
p1=Person("a",13);
p1.myfunc();

#继承
class Student(Person):
   # pass;#表示只有继承关系，没有多余的属性和方法
    def __init__(self,name,age):#子类的启动函数会覆盖对父类启动函数的继承
        self.name=name+"4";
        self.age=age+4;
        Person.__init__(self,name,age);#保持对父类的启动函数的继承
 #       super().__init__(self,name,age);#效果同上，只是不用使用父类元素的名称
        #若定义了一个和父类同名方法，会覆盖
s1=Student("jack",14);
s1.myfunc();#调用父类的方法

#迭代器 iter next 列表、元组、集合、字典、字符串都是可迭代对象
#也可以使用for进行循环遍历
myt=("12","212");
mytiter=iter(myt);#创建迭代器
print(next(mytiter));#遍历
#类也可以创建迭代器 只是类似__init__()  要在类中实现__iter__() 和 __next__()

#导入模块，调用其中函数
import mymodule as mm;
mm.greeting("wbc");
a=mm.person1[1];#访问模块变量

#仅仅导入需要部分
from mymodule import person1 as p1;
print(p1[0]);

#导入时间模块
import datetime;
x=datetime.datetime.now();#当前完整时间
print(x);
print(x.date());
x1=datetime.datetime(2010,5,10);#使用datetime里的datetime类 创建对象

#捕获异常
x='1';
try:
    print(x);
except NameError:#捕获指定异常
    print("Variable x is not defined");
except:
    print("An exception occurred");
else:
    print("Nothing happened");
finally:#无论是否异常都执行
    print("bye");

#主动引发异常
x=1;
if(x<1):
    raise Exception("stop");

#输入
print("enter your name:");
x=input();
print("hi "+x);

#字符串格式化format()
txt="hi,{}";
print(txt.format("wbc"));
txt="the price is {:.2f} dollars";#添加参数指定转换值
print(txt.format(0.01611));
txt="my name is {0}, i love {1},{1}konw？";#多参数时可以通过使用索引号确保值被正确放置，无索引是按顺序
#可以使用多次重复的索引，表示多次引用
print("who do you love?");
u=input();
print(txt.format("wbc",u));

#文件夹处理 默认为读
f=open("wbc.txt","x");#创建文件
f.write("Hello,India mi fans!");
f.close;

f=open("wbc.txt","a");#追加
f.write("Do you like me?");
f.close;

f=open("wbc.txt","r");#读取
print(f.read());
f.close;
