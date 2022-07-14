clc; close all;
t=@(t) t;
x=@(t) 1+cos(2*t);
y=@(t) -1+3*sin(4*t);

fplot3(x,y,t,[0 pi]);