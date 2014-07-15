# sum = 0
# for i in range(1, 1000):
# 	if i%3 == 0 or i%5 == 0:
# 		sum = sum + i
# print sum

###############################
l = [1,2]
while True:
	l.append(l[len(l)-1] + l[len(l)-2])
	if l[len(l)-1] > 4000000:
		break

sum = 0
for i in l:
	if i%2 == 0:
		sum = sum + i
print sum