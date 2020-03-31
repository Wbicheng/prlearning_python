import tkinter as tk;
import tkinter.messagebox;#需要import

from PIL import Image,ImageTk;#tk库本身不能显示png jpg格式 使用pillow可以

#参考：https://blog.csdn.net/ahilll/article/details/81531587
#创建窗口
window=tk.Tk();
window.title('try_window');
window.geometry('700x900');#设置长宽x

on_hit=False;
def hit_me():
    global on_hit;
    if on_hit==False:
        on_hit = True;
        var.set('hit success');
    else:
        on_hit =False;
        var.set('please hit');

var=tk.StringVar();#tk的字符串变量
la=tk.Label(window,textvariable=var,bg='red',width=15,height=10);#在窗口window上的label
#width和height为字符长度的尺度
la.pack();#进行放置

bu=tk.Button(window,text='点击',width=2,height=2,command=hit_me);#放置在window上，点击执行hit_me
bu.pack();

e=tk.Entry(window,show='*');#输入以*显示
e.pack();

def insert_content():
    t.delete(1.0,'end');
    var=e.get();#得到e的输入内容
    # t.insert('insert',var);#放置到指针位置为insert
    t.insert(1.1, var);  # 放置到第一行第一位  行从1开始检索 列从0开始

b1=tk.Button(window,text='提交信息',width=15,height=2,command=insert_content);
b1.pack();

t=tk.Text(window,height=2);
t.pack();

#可选列表
var2=tk.StringVar();
var2.set((1,3,4));
lb=tk.Listbox(window,listvariable=var2);#放置于windows上，并赋值
lb.insert('end','123');
#不支持command属性回调函数，可以用bind指定，与事件绑定
def show(event):#event为参数必填
    t.delete(1.0, 'end');
    var2=lb.get(lb.curselection());#返回当前选择项
    t.insert('end','你选择了'+str(var2));

lb.bind('<Double-Button-1>',show);
lb.pack();

#scale拉动条
def scale_show(v):
    t.delete(1.0,'end');#1.0或0.0都可以从头到尾清空内容
    t.insert('end','you slide at'+str(v));
#滑动条从0-10，刻度为2，分辨率为0.01
s=tk.Scale(window,label='slide me',from_=0,to=10,orient=tk.HORIZONTAL,
           length=200,tickinterval=2,resolution=0.01,command=scale_show);
s.pack();

#Menu窗口部件，实现下拉和弹出式菜单
#创建一个多级菜单
def do_job():
    t.delete(1.0,'end');
    t.insert('end','open new');

menubar=tk.Menu(window);#创建一个菜单栏,此处相当于一个容器
filemenu=tk.Menu(menubar,tearoff=0);#再创建一级菜单，默认不下拉
menubar.add_cascade(label='File',menu=filemenu);#将子菜单放入菜单
filemenu.add_command(label='New',command=do_job);
filemenu.add_command(label='Open');
filemenu.add_separator();#加入分割线
filemenu.add_command(label='Save');
filemenu.add_command(label='Exit',command=window.quit);#tk自动quit函数
submenu=tk.Menu(filemenu,tearoff=0);#创建二级菜单
filemenu.add_cascade(label='Import',menu=submenu);#将二级菜单放入一级菜单

#messageBox信息窗口(弹窗)
def hit_Box():
    tk.messagebox.showinfo(title='爆炸',message='hello');#info信息窗口

submenu.add_command(label='bye',command=hit_Box);

window.config(menu=menubar);#在窗口显示菜单

#显示图片
img_open=Image.open('./img/20200313104903928.jpg');
img_jpg=ImageTk.PhotoImage(img_open);
label_img=tk.Label(window,image=img_jpg);
label_img.pack();




window.mainloop();#进行循环，进行动态刷新
