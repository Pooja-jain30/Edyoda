

class Person:

	def __init__(self,id,name,age):
		self.id = id
		self.name = name
		self.age = age

	def personDetail(self):
		print('ID: '+self.id)
		print('Name: '+self.name)
		print('Age: '+self.age)

	# def getID(self):
	# 	return self.id

	# def getName(self):
	# 	return self.name

	# def getAge(self):
	# 	return self.age