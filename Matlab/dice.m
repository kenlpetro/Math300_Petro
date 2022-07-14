clc;
n=10000;

for l=1:n
    A=0;
    B=0;
    tries=0;

    while A~=B || A~=6
        A=randi(6);
        B=randi(6);
        tries=tries+1;
    end
    overall_count(l)=tries;
end

avg_count=sum(overall_count)/n;
disp(avg_count);

disp(A);
disp(B);
histogram(overall_count);