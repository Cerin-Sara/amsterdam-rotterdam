test_str = "Geeks"
print("The original string is : " + str(test_str))
n=len(test_str)
res = [test_str[i: j] for i in range(n)for j in range(i+1, n+1)]
print("All substrings of string are : " + str(res))