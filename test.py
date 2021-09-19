import matplotlib.pyplot as plt
import numpy as np

#第一节课 画平方和折线图
# x = np.linspace(-1,1,50)
# y = x**2
# y = 2*x+1
# plt.plot(x,y)
# plt.show()


#第二节课 Figure
# x = np.linspace(-3,3,50)
# y1 = x**2
# y2 = 2*x+1

# plt.figure()
# plt.plot(x,y1)


# plt.figure(num=3,figsize=(8,5))
# plt.plot(x,y2)
# plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
# plt.show()

#第三节课 修改坐标轴之间的间隔 坐标轴名称  转成英文坐标轴而不是 数值   正则表达式转数学形式  ......
x = np.linspace(-3,3,50)
y1 = x**2
y2 = 2*x+1

plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('x x')
plt.ylabel('y y')
new_ticks = np.linspace(-1,2,5) #-1,2分五个单位
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
            [r'$really\ bad$',r'$bad \ \alpha$',r'$normal$',r'$good$',r'$very\ good$'])
# 这里采取正则表达式的形式 将原有的英文形式 转换为 数学形式  注意\alpha  关联latex

plt.figure(num=4,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='green',linewidth=1.0,linestyle='--')
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('x x')
plt.ylabel('y y')
new_ticks = np.linspace(-1,2,5) #-1,2分五个单位
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
            ['really bad','bad','normal','good','very good'])
plt.show()