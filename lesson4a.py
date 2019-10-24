a,b,c=5,3.2,"\"hello\""

print(a)
print(b)
print(c)

print("%s%s%s" % (a,b,c,))
print("%s%s%s" %(a,b,c))

print('I love {} and {}'.format('bread','butter'))
print('I love{1} and {0}'.format('bread','butter'))

age=23
message= "happy" + str(age) +"rd Birthday!"
print(message)

Y=10
X = "Happy {}th Birthday!".format(Y)
