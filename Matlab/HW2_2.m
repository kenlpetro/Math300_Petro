clc;
A=[1 1 1;1 2 3;1 3 6];
b=[1;5;10];

x=linsolve(A,b);
y=A\b;

det(A);
rank(A);