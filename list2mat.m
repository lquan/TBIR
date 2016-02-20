function [ A ] = list2mat( name )

% takes an adjacency list and converts it into a sparse matrix

unix(['awk ''/^[^%]/ { for (i=2;i<=NF;i++){print $1+1, $i+1, "1"}}'' < ' ...
name ' > matlabtmpfile.txt']);

%(i,j,v) pair matrix
D = dlmread('matlabtmpfile.txt',' ');

A = spconvert(D);


end

