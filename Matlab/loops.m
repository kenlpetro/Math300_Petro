clc;
A=randn(2,2);
a=sum(A,"all");
disp(A);
disp(a);
if a>0
    disp('The sum of the elements of A are positive!')
elseif a<0
    disp('The sum of the elements of A are negative!')
elseif a==0
    disp('The sum of the elements of A is 0!')
end
%% print 10 b's
clc;
N=10;
for b=1:N
    disp('b');
end
%%
clc;
c=randi(7);
disp(sum(c,"all"))
j=0;
for i=1:length(c)
 j=j+c(i);
end
disp(j);

%% random # 1:1000
clc;
d=randi([1,1000]);
disp(d);
%% random # 500:600
clc;
e=0;
while e<500 || e>600
e=randi([1 1000]);
disp(e);
end













