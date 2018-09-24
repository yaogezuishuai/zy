import tkinter as tk
import time
import tkinter.messagebox


def Love():
    # love = tk.Toplevel(window)
    love = new_windows(300,200)
    # love.geometry('300x200')
    love.title("好巧,我也是")
    lable = tk.Label(love,text="好巧,我也是", font=("Arial", 24))
    btn = tk.Button(love, text="确定")
    btn.config(command=lambda: closelove(love))
    lable.pack()
    love.protocol('WM_DELETE_WINDOW', closeall)
    btn.pack()


def NoLove():
    # no_love = tk.Toplevel(window)
    no_love = new_windows(300,200)
    # no_love.geometry('300x200')
    no_love.title("在考虑考虑呗")
    lable = tk.Label(no_love,text="在考虑考虑呗", font=("Arial", 24))
    btn = tk.Button(no_love, text="确定")
    btn.config(command=lambda: closenolove(no_love))
    lable.pack()
    btn.pack()


def closewindow():
    tkinter.messagebox.showerror(title="警告",message = "不许关闭,好好回答!")
    return


def closeall():
    main_window.destroy()


def closelove(love):
    love.destroy()
    main_window.destroy()


def closenolove(no_love):
    no_love.destroy()


# window = tk.Tk()
# sw = window.winfo_screenwidth()#得到屏幕宽度
# sh = window.winfo_screenheight()#得到屏幕高度
# ww = 500
# wh = 400
# x = (sw-ww) / 2
# y = (sh-wh) / 2
# window.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
# window.title('你喜欢我吗?')
# window.protocol('WM_DELETE_WINDOW', closewindow)

def new_windows(ww, wh):
    window = tk.Tk()
    sw = window.winfo_screenwidth()  # 得到屏幕宽度
    sh = window.winfo_screenheight()  # 得到屏幕高度
    x = (sw - ww) / 2
    y = (sh - wh) / 2
    window.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
    return window


main_window = new_windows(500, 400)
main_window.title('你喜欢我吗?')

main_window.protocol('WM_DELETE_WINDOW', closewindow)

lable1 = tk.Label(main_window, text="hey,小姐姐", font=("Arial", 14))
lable2 = tk.Label(main_window, text="喜欢我吗?", font=("Arial", 34))

photo = tk.PhotoImage(file='1.gif')
imgLabel = tk.Label(main_window, imag=photo)


btn1 = tk.Button(main_window, text="喜欢")
btn1.config(command=Love)
btn2 = tk.Button(main_window, text="不喜欢")
btn2.config(command=NoLove)

lable1.pack()
lable2.pack()
imgLabel.pack()
btn1.pack()
btn2.pack()

main_window.mainloop()
