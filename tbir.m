clear;clc
%p =0.85;
working = 'sample-tiny.txt'; 
D = load('matlabtmpfile.txt');
G = spconvert(D);
n = size(G,1);
G = full(G);
c = sum(G,2);

A = G./repmat(c,1,n);
A(c==0,:) = 0;

H=A';
x = ones(n,1)/n
sum(x)
for i = 1:10
    %fprintf('iteration %d\n', i);
    xnew = H*x
    %diff = sum(abs(xnew-x));
    %if diff < 1e-4, fprintf('converged in %d iterations', i); break; end
    x = xnew;
end
disp('ans')
x = x/sum(x)


