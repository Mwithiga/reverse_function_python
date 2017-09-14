# a function that receives a string and returns  the string's reverse
def reverse(text):
	a = []
	for char in range(len(text)-1, -1, -1):
		a.append(text[char])
	return ''.join(a)


#example of calling the function with text desired to be reversed
print reverse("kandabongoman")
