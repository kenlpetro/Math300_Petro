clc; close all;
x=-pi:0.1:pi;
plot(x,sin(x),'-.hb');
hold on
plot(x,cos(x),':*r');
plot(x,sin(2*x),'--<g')

%%
clc; close all;
x=linspace(0,3*pi,200);
y=cos(x)+rand(1,200);
scatter(x,y);