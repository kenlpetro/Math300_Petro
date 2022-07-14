clc;
r=0;
tries=0;
while r<=20
        r=randi(5)+r;
        tries=tries+1;
end
disp(r);
disp(tries);