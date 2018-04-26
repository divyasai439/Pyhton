#global variable
f=101
print f;

def test1():
	# calling the global varibale
	global f
	print f;
	# changing the global varibale values
	f="changing the global varibale values";
	print f;
	
test1()

print f;