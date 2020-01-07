from person import Person
from old import Old
from young import Young

class Profile(Person):

	def __init__(self,id,name,age,utype,uname,pwd):

		Person.__init__(self,id,name,age)

		if(utype == 'Old'):
			self.utype = Old()
		else:
			self.utype = Young()

		self.uname = uname
		self.pwd = pwd

		self.ratings = 0
		self.no_of_rating = 0
		self.reviews = []

	def printDetails(self):
		self.personDetail()

		print('Username: '+self.uname)

		if(self.no_of_rating == 0):
			print('Rating: 0')
		else:
			print('Rating: '+(self.ratings/self.no_of_rating))

		print('Reviews: ',self.reviews)

		self.utype.printDetails()

