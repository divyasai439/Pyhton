def cheeseshop(kind, *argumnets, **Keywords):
	print("--Do u have any ", kind , "?")
	print("--I am sorry we r out of ", kind , "--")
	for arg in argumnets:
		print(arg)
	print("-" * 40)
	keys=sorted(Keywords.keys())
	for kw in keys:
		print(kw, ":", Keywords[kw])
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")
# can use keys=Keywords.keys()  instead of keys=sorted(Keywords.keys()) if we don't want sorted output