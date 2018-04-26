def f1(n):
	a,b=0,1
	while b<n:
	  print(b)
	  a,b=b,a+b
f1(10)
# with functions and return value
def f1(n):
	result= []
	a,b=0,1
	while b<n:
	  result.append(b)
	  a,b=b,a+b
	return result
aa=f1(10)
print(aa)