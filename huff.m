% Huffman code
% Hongyu Tu
% 05/12/2020

val = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"];
pmf = [5.00000000000000e-07,8.50000000000000e-06,8.70000000000000e-05,0.000573900000000000,0.00301260000000000,0.0115827000000000,0.0346656000000000,0.0810719000000000,0.147420600000000,0.206042900000000,0.218599800000000,0.170062400000000,0.0916765000000000,0.0304545000000000,0.00474060000000000];

[sorted_pmf, order] = sort(pmf);
sorted_val = val(:,order);

% nodes is a list of nodes generated
% When the update is done, nodes(-1) should be the final huffman tree
nodes = {};
n = 1;

while length(sorted_val) > 1
    num_in = length(sorted_val);
    % node{1,1} is the combined value
    % node{1,2} is the left child
    % node{1,3} is the right child
    % node{1,4} is the height of the tree

    node = cell(1,4);
    sum = sorted_pmf(1) + sorted_pmf(2);
    node{1,1} = sum;
    node{1,4} = 1;

    nuno = string(sorted_val(1));

    if contains(nuno,'Node')
        index = str2num(extractAfter(nuno,'Node'));
        jaja = nodes{1,index};

        node{1,2} = jaja;
        node{1,4} = node{1,4} + jaja{1,4};
    else
        node{1,2} = sorted_val(1);
    end

    nuno = string(sorted_val(2));

    if contains(sorted_val(2),'Node')
        index = str2num(extractAfter(nuno,'Node'));
        jaja = nodes{1,index};

        node{1,3} = jaja;
        node{1,4} = node{1,4} + jaja{1,4};
    else
        node{1,3} = sorted_val(2);
    end

    nodes{1,n} = node;

    if length(num_in) == 2
        break
    end

    sorted_pmf = sorted_pmf(3:end);
    sorted_val = sorted_val(3:end);

    name = strcat('Node',string(n));

    sorted_pmf(length(sorted_pmf) + 1) = sum;
    sorted_val(length(sorted_val) + 1) = name;

    [sorted_pmf, order] = sort(sorted_pmf);
    sorted_val = sorted_val(:,order);

    n = n + 1;
end

curry = size(nodes);
tree = nodes{1,curry(2)};

dict = step(tree, "");

function code = step(current,str)
    left = current{1,2};
    right = current{1,3};
    if isa(left,'cell') 
        code1 = step(left,strcat(str,'0'));
    else
        tmp_code = strcat(str,'0');
        tmp.name = left;
        tmp.val = tmp_code;
        code1 = [tmp];
    end

    if isa(right,'cell') 
        code2 = step(right,strcat(str,'1'));
    else
        tmp_code = strcat(str,'1');
        tmp.name = right;
        tmp.val = tmp_code;
        code2 = [tmp];
    end

    code = [code1 code2];
end




