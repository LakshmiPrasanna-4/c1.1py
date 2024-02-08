#Create a student dictionary with 5 subjects and generate results.

s={}
n=int(input('Enter number of students:'))
for i in range(n):
    l=[]
    htno=int(input('Enter htno:'))
    sname=input('Enter name:')
    s1=int(input('Enter maths marks:'))
    s2=int(input('Enter english marks:'))
    s3=int(input('Enter computer marks:'))
    s4=int(input('Enter physics marks:'))
    s5=int(input('Enter electronic marks:'))
    l.append(sname)
    l.append(s1)
    l.append(s2)
    l.append(s3)
    l.append(s4)
    l.append(s5)
    s[htno]=l
hno=int(input('Enter htno:'))
print('Name of the student:',s[hno][0])
total=s[hno][1]+s[hno][2]+s[hno][3]+s[hno][4]+s[hno][5]
avg=total//5
print('Total:',total)
print('Average:',avg)
if(avg>60):
    print('Pass')
else:
    print('Fail')
