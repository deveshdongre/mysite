s = 'hello world'
a = list(s)
for x in range(len(a)//2):
	temp = a[x]
	a[x] = a[len(a) - 1 -x]
	a[len(a) - 1 -x] = temp
print(a)