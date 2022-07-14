clc;
A=[2 -1 4;9 6 2;1 3 8];
B=ones(3);
x=[3;6;8];
y=[5 10 15];

a=A*B;
b=A*x;
c=x'*B;
%d=B*y; %needs the "." to correctly multiply the martrix
%e=x*A; %also needs the "."
f=x*y;
g=y*x;
%h=x*y'; %doesn't work because the "'" 
i=x.*y;
j=A.*B;