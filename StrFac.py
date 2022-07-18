import math
import cmath
import pandas as pd

Ce=4.84
Ge=8.185
Zn=5.680
z=0.38
l=2.4
a=[4.0,4.0,10.0]
#path='/Users/kobayashinaoki/Desktop/nakajima\ lab/python\ code/structurefactor/atm2.csv  '
path='./atm2.csv'

def f(plane,path):
    file=open(path)
    row=file.read()
    row2=row.split('\n')
    ldata=[i.split(',') for i in row2]
    data=[[float(j) for j in i] for i in ldata] #csvを配列に変換
    p=((plane[0]/a[0])**2+(plane[1]/a[1])**2+(plane[2]/a[2])**2)**(1/2)/2/(1/l)
    t=math.asin(p)
    o=math.atan2((plane[2]/a[2]),(plane[0]/a[0]))
    F=0
    for i in range(0,len(data)):
        v=data[i][0]*cmath.exp(1j*(plane[0]*data[i][1]+plane[1]*data[i][2]+plane[2]*data[i][3])*2*math.pi)
        F=F+v
    return [t*2*180/math.pi,(o+t)*180/math.pi,F]

def pl(ax): #(0,0,0),座標axを通る方向を回転軸とした時に現れる散乱の逆格子ベクトル
    lh=0
    lk=0
    ll=1
    vec=[]
    while ((lh/a[0])**2+(lk/a[1])**2+(ll/a[2])**2)**(1/2)/2/(1/l)<1:
        while ((lh/a[0])**2+(lk/a[1])**2+(ll/a[2])**2)**(1/2)/2/(1/l)<1:
            while ((lh/a[0])**2+(lk/a[1])**2+(ll/a[2])**2)**(1/2)/2/(1/l)<1:
                if ax[0]*lh+ax[1]*lk+ax[2]*ll==0: #軸と逆格子ベクトルが垂直
                    vec.append([lh,lk,ll])
                else:
                    pass
                ll=ll+1
            ll=0
            lk=lk+1
        lk=0
        lh=lh+1
    return vec

def list(ax,path):
    data=[]
    pln=pl(ax)
    for i in pln:
        data.append(f(i,path))
    df=pd.DataFrame(data,columns=['2theta','omega','StructureFactor'])
    df2=df.sort_values('2theta')
    return df2

list([0,1,0],path)