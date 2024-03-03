from tkinter import *
from datetime import *
from threading import *
from urllib import request
from tkinter import ttk, filedialog, colorchooser, messagebox
import time, os, sys, shutil, re

global day, event, ft, fgg, bgg, fl, wea_inf, weat

xsm=40

'''
下面这段代码作者：@许书陌不会C，TA在不引入任何第三方库的前提下
巧妙地实现了爬取当前天气信息，特别感谢！
'''
def wt(event):
    global more
    try:
        req = request.Request('https://tianqi.2345.com/')
        weekly_weather = request.urlopen(req).read().decode('utf-8')
        tg = r'<span class="banner-whether-desc1">(.*)</span>'
        tg1=r'<!-- <span class="banner-whether-desc2">(.*)</span> -->'
        tg2=r'<div class="banner-right-con-list-temp">(.*)</div>'
        tg3=r'data-ajax25="(.*)" data-ajax25module="首屏内容区" data-ajax25location="空气质量">'
        tem=re.findall(tg, weekly_weather)
        wea=re.findall(tg1, weekly_weather)
        inf=wea[0]+' '+tem[0]
        tem_ft=re.findall(tg2, weekly_weather)
        air=re.findall(tg3,weekly_weather)
        inf1=str(air[0])+'\n今天'+str(tem_ft[1])+'\n明天'+str(tem_ft[2])
        l2.config(text=inf, font=('微软雅黑',22))
        l8.config(text=inf1, font=('微软雅黑',14),anchor='n')
        print(inf1)
    except:
        l2.config(text='获取天气信息失败！\n单击此处重试。', font=('微软雅黑',13))
        l8.config(text= ' ', font=('微软雅黑',15))
    
'''
这是这段代码的结尾
'''

try:
    with open('res/weather.txt') as a:
        weat = a.read()
    with open('res/disk0.txt') as a:
        disk0 = a.read()
    with open('res/disk1.txt') as a:
        disk1 = a.read()
    with open('res/disk2.txt') as a:
        disk2 = a.read()
    with open('res/tit.txt') as a:
        tit = a.read()
    with open('res/fgg.txt') as a:
        fgg = a.read()
    with open('res/bgg.txt') as a:
        bgg = a.read()
    with open('res/ft.txt') as a:
        ft = a.read()
    with open('res/fl.txt') as a:
        fl = int(a.read())
    with open('res/djs.txt') as f:
        day = (datetime.strptime(f.readlines()[1], '%Y-%m-%d') - datetime.now()).days
    with open('res/djs.txt') as f:
        event = f.readlines()[0]
    z=len(str(day))
    if z >= 5:
        xsm=24
except:
    messagebox.showerror('错误','由于配置文件错误，电子班务栏无法启动。请重新解压res配置文件夹。')

if weat=='1':
        wea_st='打开天气'
        wea_inf='0'
else:
    wea_st='关闭天气'
    wea_inf='1'

def readdjs():
    global day, event
    with open('res/djs.txt') as f:
        day = (datetime.strptime(f.readlines()[1], '%Y-%m-%d') - datetime.now()).days
    with open('res/djs.txt') as f:
        event = f.readlines()[0]
    l3.config(text=str(day + 1) + '天')
    z=len(str(day + 1))
    if z >= 5:
        xsm=25
    else:
        xsm=40
        
    l3_.config(text='距离' + event + '还有')
    l3.config(font=('微软雅黑', xsm))


def scan():
    while True:
        wt(None)
        time.sleep(1200)

def scan_t():
    l8.config(text= '又是元气满满\n的一天呢！', font=('微软雅黑',15))
    while True:
        l2.config(text=datetime.now().strftime('%H:%M'))
        time.sleep(1)

def animation():
    n = 0
    while n <= 0.9:
        win.attributes("-alpha", n)
        win.update()
        n = n + 0.1
        time.sleep(0.02)


def open_U():
    try:
        os.startfile(disk0+':')
    except:
        try:
            os.startfile(disk1+':')
        except:
            os.startfile(disk2+':')


def ext(event):
    win.destroy()
    os._exit(0)


def cls(line, cn):
    with open('res/kcb.txt') as f:
        c = f.readlines()[line]
        l1.config(text='\n' + c)
        l4_.config(text=cn)


def show(event):
    w = Toplevel()
    w.wm_attributes('-topmost', 1)

    def clss(event):
        w.destroy()

    w.overrideredirect(True)
    w.geometry('%dx%d+%d+%d' % (500, 420, win.winfo_screenwidth() - 520, win.winfo_screenheight() - 480))
    img = PhotoImage(file='res/egg.gif')
    a = Label(w, image=img)
    x = Label(w, text='x', bg='red', fg='white')
    x.place(width=20, height=30, x=480, y=0)
    x.bind('<Button-1>', clss)
    a.pack()
    w.mainloop()

def djss(event):
    w = Tk()
    def clss(event):
        w.destroy()

    def save():
        e11 = e1.get()
        e22 = e2.get()
        if e11 == '':
            a = Label(w, text='请输入事件名称！')
            a.pack()
            return
        try:
            datetime.strptime(e22, '%Y-%m-%d')
        except:
            a = Label(w, text='请输入正确的时间格式！')
            a.pack()
            return
        
        f = open('res/djs.txt', 'w')
        f.write(e11 + '\n' + e22)
        f.close()
        readdjs()
        w.destroy()

    w.geometry('%dx%d+%d+%d' % (500, 420, win.winfo_screenwidth() - 520, win.winfo_screenheight() - 480))
    w.overrideredirect(True)
    w.wm_attributes('-topmost', 1)
    lt = Label(w,text='修改倒计时！', fg=bgg, font=(ft, fl, 'bold'))
    ll1 = Label(w, text='请输入事件名称')
    e1 = Entry(w, width=30)
    ll2 = Label(w, text='请输入目标日期，格式示例2023-9-10')
    e2 = Entry(w, width=30)
    b = Button(w, text='确定', command=lambda: save())
    tp = Label(w,text='修改倒计时也可以长按主页方块哦~')
    x = Label(w, text='x', bg='red', fg='white')
    x.place(width=20, height=30, x=480, y=0)
    x.bind('<Button-1>', clss)
    lt.pack()
    ll1.pack()
    e1.pack()
    ll2.pack()
    e2.pack()
    tp.place(x=150,y=250)
    b.pack()
    w.mainloop()


def ftft():
    def clss(e):
        bk.destroy()

    def savee():
        global title, ll1, ft, fl
        fl = scale.get()
        ft = b1.get()
        t.config(font=(ft, fl, 'bold'))
        title.config(font=(ft, fl, 'bold'))
        f = open('res/ft.txt', 'w')
        f.write(ft)
        f.close()
        g = open('res/fl.txt', 'w')
        g.write(str(fl))
        g.close()

    bk = Tk()
    bk.wm_attributes('-topmost', 1)
    bk.geometry('%dx%d+%d+%d' % (500, 420, bk.winfo_screenwidth() - 520, win.winfo_screenheight() - 480))
    bk.overrideredirect(True)
    x = Label(bk, text='x', bg='red', fg='white')
    t = Label(bk, text='修改字体', fg=bgg, font=(ft, fl, 'bold'))
    v = ('宋体', '隶书', '微软雅黑', '幼圆', '方正舒体', '方正姚体', '楷体', '仿宋', '也可以直接输入你想要的字体~')
    b1 = ttk.Combobox(bk)
    b1['value'] = v
    var = DoubleVar()
    scale = Scale(bk, variable=var, orient=HORIZONTAL, from_=15, to=35, length=170, width=20)
    b1.set(ft)
    scale.set(fl)
    b = Button(bk, text='保存', command=savee)
    x.place(width=20, height=30, x=480, y=0)
    t.pack()
    b1.pack()
    x.bind('<Button-1>', clss)
    scale.pack()
    b.pack()
    bk.mainloop()


def cg(event):
    os.startfile('res\kcb.txt')


def dev(event):
    def re(event):
        w.destroy()

    def cgtt():
        title.config(text=bte.get())
        c = open('res/tit.txt', 'w')
        c.write(bte.get())
        c.close()
        tit = bte.get()
        z = Label(w, text='操作成功完成。')
        z.pack()

    def disk_0():
        global disk0
        c = open('res/disk0.txt', 'w')
        c.write(bdl1.get())
        c.close()
        disk0 = bdl1.get()

    def disk_1():
        global disk1
        c = open('res/disk1.txt', 'w')
        c.write(bdl2.get())
        c.close()
        disk1 = bdl2.get()

    def disk_2():
        global disk2
        c = open('res/disk2.txt', 'w')
        c.write(bdl3.get())
        c.close()
        disk2 = bdl3.get()

    def svdk():
        disk_0()
        disk_1()
        disk_2()
        z = Label(w, text='操作成功完成。')
        z.pack()

    def helpme(event):
        os.startfile('README.TXT')

    def ipt():
        i = filedialog.askdirectory(initialdir='settings/')
        if i == '':
            pass
        else:
            f = os.path.exists(i + '/bgg.txt')
            g = os.path.exists(i + '/egg.gif')
            h = os.path.exists(i + '/weather.txt')
            if not f or not g or not h:
                z = Label(w, text='无效的配置文件夹。')
                z.pack()
            else:
                shutil.rmtree('res')
                shutil.copytree(i, './res')
                rest()
        w.wm_attributes('-topmost', 1)

    def opt():
        o = 'settings/' + datetime.now().strftime('%y_%m_%d_%H_%M_%S')
        shutil.copytree('res/', o)
        z = Label(w, text='导出为' + o)
        z.pack()
        w.wm_attributes('-topmost', 1)

    def chooseclr():
        global bgg
        w.wm_attributes('-topmost', 0)
        cl = colorchooser.askcolor()
        if str(cl[1]) == 'None':
            w.wm_attributes('-topmost', 1)
            pass
        else:
            a = open('res/bgg.txt', 'w')
            a.write(str(cl[1]))
            a.close()
            w.wm_attributes('-topmost', 1)
            f = str(cl[1])
            bgg = f
            ll1.config(fg=f)
            sb.config(fg=f)
            title.config(fg=f)
            l1.config(bg=f)
            l1_.config(bg=f)
            l2.config(bg=f)
            l3.config(bg=f)
            l3_.config(bg=f)
            l4.config(bg=f)
            l4_.config(bg=f)
            l6.config(fg=f)
            st.config(bg=f)
            l7.config(fg=f)
            z = Label(w, text='操作成功完成。')
            z.pack()

    def choosef():
        global fgg
        w.wm_attributes('-topmost', 0)
        cl = colorchooser.askcolor()
        if str(cl[1]) == 'None':
            w.wm_attributes('-topmost', 1)
            pass
        else:
            b = str(cl[1])
            fgg = b
            win.config(bg=b)
            sb.config(bg=b)
            title.config(bg=b)
            l1.config(fg=b)
            l1_.config(fg=b)
            l2.config(fg=b)
            l3.config(fg=b)
            l3_.config(fg=b)
            l4.config(fg=b)
            l4_.config(fg=b)
            l6.config(bg=b)
            st.config(fg=b)
            l7.config(bg=b)
            a = open('res/fgg.txt', 'w')
            a.write(str(cl[1]))
            a.close()
            w.wm_attributes('-topmost', 1)
            sb.config(bg=str(cl[1]))
            z = Label(w, text='操作成功完成。')
            z.pack()

    def rest():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def cgwe():
        global wea_inf, weat
        print(wea_inf)
        a = open('res/weather.txt', 'w')
        a.write(wea_inf)
        weat=wea_inf
        a.close()
        rest()

    w = Tk()
    w.overrideredirect(True)
    w.wm_attributes('-topmost', 1)
    w.geometry('%dx%d+%d+%d' % (500, 420, win.winfo_screenwidth() - 520, win.winfo_screenheight() - 480))
    ll1 = Label(w, text='设置', fg=bgg, font=(ft, fl, 'bold'))
    cb = Button(w, text='修改课表', command=lambda: cg(0))
    sb = Button(w, fg=bgg, bg=fgg, text='修改倒计时', command=lambda:djss(1))
    bt = Label(w, text='修改标题')
    op = Button(w, text='导出设置', command=opt)
    ip = Button(w, text='导入设置', command=ipt)
    b22 = Button(w, text='选取前景颜色', command=chooseclr)
    b33 = Button(w, text='选取背景颜色', command=choosef)
    b5 = Button(w, text='重启程序', fg='red', command=rest)
    bdl = Label(w, text='可能的U盘盘符')
    bwe=Button(w, text=wea_st, command=cgwe)
    bd1 = Entry(w, width=5)
    bd2 = Entry(w, width=5)
    bd3 = Entry(w, width=5)
    v = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w',
        'x', 'y', 'z')
    bdl1 = ttk.Combobox(w)
    bdl1['value'] = v
    bdl1.set(disk0)
    bdl2 = ttk.Combobox(w)
    bdl2['value'] = v
    bdl2.set(disk1)
    bdl3 = ttk.Combobox(w)
    bdl3['value'] = v
    bdl3.set(disk2)
    b66 = Button(w, text='修改标题字体', command=ftft)
    bdl4 = Button(w, text='保存', command=svdk)
    hp = Label(w, text='背景颜色设为前景颜色对应的浅色更漂亮哦~', fg=bgg, font=(ft, 15))
    hp1 = Label(w, text='到底怎么改？', fg='blue', font=('微软雅黑', 12, 'underline'))
    bte = Entry(w, width=30)
    btb = Button(w, text='保存', command=cgtt)
    x = Label(w, text='x', bg='red', fg='white')
    x.place(width=20, height=30, x=480, y=0)
    x.bind('<Button-1>', re)

    ll1.pack()
    bt.place(x=70, y=45)
    bte.place(x=130, y=45)
    btb.place(x=350, y=45)
    b22.place(x=100, y=95)
    b33.place(x=300, y=95)
    sb.place(x=340, y=185)
    bdl.place(x=200, y=130)
    bdl1.place(x=100, y=150, width=40)
    bdl2.place(x=200, y=150, width=40)
    bdl4.place(x=400, y=150)
    bdl3.place(x=300, y=150, width=40)
    hp.place(x=60, y=360)
    hp1.place(x=200, y=320)
    op.place(x=170, y=240)
    cb.place(x=240, y=185)
    ip.place(x=250, y=240)
    hp1.bind('<Button-1>', helpme)
    b5.place(x=330, y=240)
    b66.place(x=120, y=185)
    bwe.place(x=90, y=240)
    w.mainloop()


a = datetime.now().strftime('%a')
win = Tk()
win.overrideredirect(True)
win.config(bg=fgg)
width = win.winfo_screenwidth()
height = win.winfo_height()
win.geometry('%dx%d+%d+%d' % (500, 420, win.winfo_screenwidth() - 520, win.winfo_screenheight() - 480))
win.attributes("-alpha", 0)

title = Label(win, text=tit, fg=bgg, bg=fgg, font=(ft, fl, 'bold'))
l1 = Label(win, text='--', bg=bgg, fg=fgg, font=('微软雅黑', 23), wraplength=250)
l1_ = Label(win, text='今日课程', bg=bgg, fg=fgg, font=('隶书', 15))
l2 = Label(win, text='--', bg=bgg, fg=fgg, font=('微软雅黑', 30))
l3 = Label(win, text=str(day + 1) + '天', bg=bgg, fg=fgg, font=('微软雅黑', xsm))
l3_ = Label(win, text='距离' + event + '还有', bg=bgg, fg=fgg, font=('隶书', 15))
l4 = Label(win, text=datetime.now().strftime('%m-%d'), bg=bgg, fg=fgg, font=('微软雅黑', 30))
l4_ = Label(win, text='--', bg=bgg, fg=fgg, font=('隶书', 18))
l6 = Button(win, text='打开U盘', bg=fgg, fg=bgg, font=('微软雅黑', 25), command=lambda: open_U())
l7 = Label(win, bg=fgg, fg=bgg, text='Version 2.6 | 设置')
l8=Label(win,bg=bgg,fg=fgg,text='')

if a == 'Mon':
    cls(0, '星期一')
if a == 'Tue':
    cls(1, '星期二')
if a == 'Wed':
    cls(2, '星期三')
if a == 'Thu':
    cls(3, '星期四')
if a == 'Fri':
    cls(4, '星期五')
if a == 'Sat':
    cls(5, '星期六')
if a == 'Sun':
    cls(6, '星期日')

title.place(width=500, height=60, x=0, y=10)
l2.place(width=150, height=75, x=20, y=80)
l1_.place(width=150, height=20, x=245, y=100)
l1.place(width=305, height=150, x=175, y=80)
l3.place(width=150, height=150, x=175, y=235)
l3_.place(width=148, height=40, x=175, y=250)
l4.place(width=150, height=150, x=20, y=235)
l4_.place(width=65, height=20, x=65, y=250)
l6.place(width=150, height=150, x=330, y=235)
l7.place(width=150, height=30, x=175, y=388)
l8.place(width=150, height=96, x=20, y=134)

c = Thread(target=scan)
c2 = Thread(target=scan_t)
if weat == '1':
    c2.start()
else:
    c.start()
    l2.bind('<Button-1>', wt)
c1 = Thread(target=animation)
c1.start()

win.bind('<Control-Shift-R>', ext)
l7.bind('<Button-3>', show)
l1.bind('<Button-3>', cg)
l3.bind('<Button-3>', djss)
l3_.bind('<Button-3>', djss)
l7.bind('<Button-1>', dev)

win.mainloop()
