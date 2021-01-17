class Flames:
	'''
	class containing attributes and methods required to play flames game.
	Attributes : 
	name1 - string with name of first person
	name2 - string with name of second person
	n1 - list of letters in name1 after removing common letters
	n2 - list of letters in name2 after removing common letters
	expansion - dictionary with expansions(value) of the letters(key) in flames
	common_letters - list containing common letters of the two names
	order_of_elimination - list containing 5 letters of flames in the order they were eliminated
	count - integer which is the total number of letters in both names after removal of common letters
	Methods :
		get_names()
		make_properties()
		find_value()
		display_properties()
		display_message()
		display_interactive()
	'''
	expansion = {'F':'Friends','L':'Lovers','A':'Acquaintances','M':'Married','E':'Enemies','S':'Siblings'}
	common_letters = []
	order_of_elimination = []
	def __init__(self):
		self.get_names()
		self.make_properties()
		self.find_value()
	def get_names(self):
		self.name1 = input('Enter the first name : ')
		self.name2 = input('Enter the second name : ')
	def make_properties(self):
		self.n1 = list(self.name1.lower().replace(' ',''))
		self.n2 = list(self.name2.lower().replace(' ',''))
		for i in self.n1:
			if i in self.n2:
				self.n1.remove(i)
				self.n2.remove(i)
				self.common_letters.append(i)
		self.count = len(self.n1) + len(self.n2)
	def find_value(self):
		flames_list = ['.']+list('FLAMES' * self.count)
		flag = self.count
		for i in range(5):
			element = flames_list[flag]
			temp = flames_list.index(element)
			self.order_of_elimination.append(element)
			while element in flames_list:
				flames_list.remove(element)
			flag = temp + self.count - 1
		self.value = flames_list[1]
	def display_properties(self):
		print(f'Names after removing common letters {self.common_letters} are {self.n1} and {self.n2}')
		print(f'the value is {self.count}')
	def display_message(self):
		print(f'{self.name1} and {self.name2} are {self.expansion[self.value]}')
	def display_interactive(self):
		self.display_properties()
		l = list('FLAMES')
		print(''.join(l))
		input()
		for x in self.order_of_elimination:
			l[l.index(x)] = 'X'
			print(''.join(l))
			input()
		self.display_message()
		def __str__(self):
			return f'checking relationship between {self.name1} and {self.name2}'
if __name__ == '__main__':
	f = Flames()
	f.display_interactive()
else:
	print('Instantiate class Flames and call display_message()\n ')
