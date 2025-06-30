# Question 1
def f(x):
    return x**2 - 3

def g(x):
    return 3*(x**2) + x - 6

def fg(x):
    return f(g(x))

def gf(x):
    return g(f(x))

#Question 2
#Since we cannot use max() func
#And we want to use a structural approach
def max3(a,b,c):
    def max2(a,b):
        return a if a > b else b
    return max2(max2(a,b), max2(b,c))

#Question 3
#This question is fairly futile for a factorial func
#Ex. fact(5) -> 5 * fact(4) --> 5 * 4 * fact(3) --> ... --> 5 * 4 * 3 * 2 * fact(1) which is 1 in base case
def step_count_k(n):
    return n + 1

#Question 4
#A tree is similar if it has the same shape
class Tree:
    def __init__(self, left, right, val):
        self.val = val
        self.left = left
        self.right = right

def is_similar(a,b):
    if not a and not b:
        return True
    if not b or not a:
        return False
    else: 
        return is_similar(a.left, b.left) and is_similar(a.right, b.right)

#Question 5
#My first intuition
def full(root):
    def max_height(node):
        if not node:
            return 0
        else:
            return 1 + max(max_height(node.left), max_height(node.right))
    h = 2**max_height(root) - 1
    
    def count_nodes(node):
        if not node:
            return 0
        else:
            return 1 + count_nodes(node.left) + count_nodes(node.right)

    return h == count_nodes(root)
#Alternative (probably better function)
def is_full(node):
    if not node:
        return True
    if (node.left is None and node.right is None):
        return True
    if node.left and node.right:
        return is_full(node.left) and is_full(node.right)
    return False

#Question 6
#Iterative appraoch (probably not racketlike)
def perms(lst):
    if not lst:
        return [[]]    
    result = []
    for i, elem in enumerate(lst):
        rest = lst[:i] + lst[i+1:]
        for p in perms(rest):
            result.append([elem] + p)
    return result

#Probably a more racket-lise approach
def perms_structural(lst):
    if not lst:
        return [[]]
    
    head, tail = lst[0], lst[1:]
    tail_perms = perms(tail)
    
    result = []
    for perm in tail_perms:
        result.extend(insert_all_positions(head, perm))
    return result

def insert_all_positions(x, lst):
    result = []
    for i in range(len(lst) + 1):
        result.append(lst[:i] + [x] + lst[i:])
    return result
