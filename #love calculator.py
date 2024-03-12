name1=input("enter your name")
name2=input("enter your crushes name")
combine_string=name1+name2
lower_string_combine= combine_string.lower()
t=lower_string_combine.count('t')
r=lower_string_combine.count('r')
u=lower_string_combine.count('u')
e=lower_string_combine.count('e')
true= t+r+u+e
l=lower_string_combine.count('l')
o=lower_string_combine.count('o')
v=lower_string_combine.count('v')
e=lower_string_combine.count('e')
love=l+o+v+e
love_score=int(str(true)+ str(love))
print(love_score)