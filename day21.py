
#list comprehensions
# For example, if you want to generate all combinations of lists  and , write:

# >>> print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])
# [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]

# This is equivalent to:

# >>> results = []
# >>> for x in [1, 2, 3]:
# ...     for y in [4, 5, 6]:
# ...         results.append([x, y])
# ... 
# >>> print(results)
# [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print(list([i,j,k] for i in range (x+1) for j in range (y+1) for k in range (z+1)     if i+j+k!= n))