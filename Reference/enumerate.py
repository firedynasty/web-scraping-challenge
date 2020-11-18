# Python program to illustrate 
# enumerate function 
l1 = ["eat","sleep","repeat"] 
s1 = "geek"
  
# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 
 
#print "Return type:",type(obj1) 
list(obj1)
# [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

list(enumerate(s1,2))
# changing start index to 2 from 0 
#[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

type(obj1)
#enumerate


