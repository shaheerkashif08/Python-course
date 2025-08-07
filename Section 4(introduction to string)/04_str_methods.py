s = "hello world"  # string is immutable

print(len(s)) # prints the lenght of str
print(s.upper())  # prints the uppercase of str
print(s.lower())  # prints the lowercase of str
print(s.capitalize()) # print the str with first element capital
print(s.title())   # print the str with first element of every word capital

text = " shaheer kashif "
print(text.strip())  # output: "hello world"
print(text.lstrip())  # output: "hello world "
print(text.rstrip())  # output: " hello world"

text1 = "Python is simple"
print(text1.find("is"))   # find the index of first occurence
print(text1.replace("simple", "awesome"))

text2 = "Apples,Banana,Grapes"
print(text2.split(","))
print(",".join(['Apples','Banana','Grapes']))

tex3 = "Python123"
print(tex3.isalpha())
print(tex3.isdigit())
print(tex3.isalnum())
print(tex3.isspace())


