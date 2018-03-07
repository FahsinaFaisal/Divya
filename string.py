a='Python Programming'
a=str(a)
print("1   :  Length of the string")
print("2   :  Substring program in the string")
print("3   :  Repeat the string 3 times")
print("4   :  Print the characters of a string in vertical and horizontal fashion")
print("5   :  Character in the 4th position")
print("6   :  Extract 4 characters starting at index 5")
print("7   :   Print all the characters except the last two")
print("8   :  Append another string 'Lab excercises 2013' to the existing string")
print("9   :  Change the string 'e' to '&'")
print("10  : Split the string using the letter 'o'")
print("11  : Join the string using '#' symbol")
print("12  : Count the no of spaces, alphabets, digits") 
print("13  : Justified the string (left and right)")
print("14  : Change the case of the string") 
print("15  :  Exist")
ch=int(input("Enter your choice:"))
if ch==1:
	print("Length of the string")
	l=len(a)
	print("Length   :",l)
if ch==2:
	print("Substring in the string")
	print(a[3:7])
if ch==3:
	print("String 3 times")
	print(a*3)
if ch==4:
	print("Characters of a string in vertical and horizontal fashion")
	print("Horizontal fashion:")
	for i in a:
		print(i,end=' ')
	print("\n")
	print("Vertical fashion :")
	for j in a:
		print(j)
if ch==5:
	print("Character in the 4th position")
	print(a[4])
if ch==6:
	print("Extract 4 characters starting at index 5")
	print(a[5:10])
if ch==7:
	print(" Print all the characters except the last two")
	print(a[0:16])
if ch==8:
	print("8   :  Append another string 'Lab excercises 2013' to the existing string")
	s1=a.replace(a,'Lab excercises 2013')
	print(s1)
if ch==9:
	print("9   :  Change the string 'e' to '&'")
	s2=a.replace('e','&')
	print(s2)
if ch==10:
	print("10  : Split the string using the letter 'o'")
	s3=a.split('o')
	print(s3)
if ch==11:
	print("Join the string using '#' symbol")
	s4=a+'#'
	print(s4)
if ch==12:
	alphabets=0
	digits=0
	space=0
	l=len(a)
	print(" Count the no of spaces, alphabets, digits") 
	for i in a:
		if i.isalpha():
			alphabets+=1
		if i.isnumeric():
			digit+=1
		if i.isspace():
			space+=1
	print("Alphabets in the string  :   ",alphabets)
	print("Digits in the string  :  ",digits)
	print("Spaces in the string  :",space) 
if ch==13:
	print("13  : Justified the string (left and right)")
if ch==14:
	print("14  : Change the case of the string") 
	if a.isupper():
		u=a.lower()
		print(u)
	else:
		l=a.upper()
		print(l)


	
	
	
	
	
