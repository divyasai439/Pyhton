# deleting the variable

f=101;
print f;

def test1():
	global f;
	print f;
	del f;
	
test1()
print f;