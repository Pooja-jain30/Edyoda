from profile import Profile

class EdYoda:

	__sess_id = None
	__sess_pwd = None
	__sess_obj = None

	id_counter = 1

	main_menu = ['1. Register User','2. Search User Taking Care','3. Search User getting Care',
		'4. Login User','Press * to Exit']

	old_login_menu = ['1. Profile Detail','2. Check Care-Taker Details','3. Get Details of Young',
		'4. Check Caring Requests','5. Approve Caring Request','6. Remove Care-Taker','7. Logout']

	young_login_menu = ['1. Profile Detail','2. List Caring Oldies','3. Get all oldies status',
		'4. Get detail of oldie','5. Send request to oldie','6. Remove Oldie for Caring','7. Logout']

	def __init__(self):

		self.profile_list = [
			Profile('1','Pooja Jain','23','Young','pooja','pooja'),
			Profile('2','Rakesh Shrivastav','54','Old','rakesh','rakesh')]

		self.startInterface()

	def startInterface(self):
		print('Welcome to EdYoda')

		while(True):
			self.printOptions(self.main_menu)

			ch = input('Enter Choice: ')

			if(ch == '1'):
				self.registerUser()
			elif(ch == '2'):
				self.searchUserTakingCare()
			elif(ch == '3'):
				self.searchUserGettingCare()
			elif(ch == '4'):
				self.loginUser()
			elif(ch == '*'):
				break
			else:
				print('Wrong Choice')

	def loginUser(self):
		if(not self.checkSession()):
			uname = input('Enter Username: ')
			pwd = input('Enter Password: ')

			found = False

			for profile in self.profile_list:
				u = getattr(profile,'uname')
				p = getattr(profile,'pwd')

				if(u == uname and p == pwd):
					self.__sess_obj = profile
					found = True
					break

			if(found):
				self.createSession(uname,pwd)

				if(self.__sess_obj.utype.__name__ == 'Old'):
					self.oldLoginMenu()
				else:
					self.youngLoginMenu()
			else:
				print('User Not Found!!')
		else:
			print('Logout from current session to login again')

	def youngLoginMenu(self):
		while(True):
			self.printOptions(self.young_login_menu)

			ch = input('Enter Choice: ')

			if(ch == '1'):
				self.__sess_obj.printDetails()
			elif(ch == '2'):
				print(self.__sess_obj.utype.caring_ids)
			elif(ch == '3'):
				self.listUsers('Old')
			elif(ch == '4'):
				id = input('Enter oldie ID: ')
				if(self.isType(id,'Old')):
					user = self.userExistByID(id)
					if(user != None):
						user.printDetails()
					else:
						print('User does not exist')
				else:
					print('User is not of the type Old')

			elif(ch == '5'):
				id = input('Enter oldie ID: ')
				if(self.isType(id,'Old')):
					user = self.userExistByID(id)
					if(user != None):
						user.utype.pending_request_ids.append(getattr(self.__sess_obj,'id'))
					else:
						print('User does not exist')
				else:
					print('User is not of the type Old')				
			elif(ch == '6'):
				print('Oldies you can remove are: ',self.__sess_obj.caring_ids)
				id = input('Enter ID to remove: ')

				if(id not in self.__sess_obj.caring_ids):
					print('ID not available')
				else:
					self.__sess_obj.caring_ids.remove(id)
					print('Oldie removed Successfully')
			elif(ch == '7'):
				self.logout()
				break
			else:
				print('Wrong Choice')			

	def oldLoginMenu(self):
		while(True):
			self.printOptions(self.old_login_menu)

			ch = input('Enter Choice: ')

			if(ch == '1'):
				self.__sess_obj.printDetails()
			elif(ch == '2'):
				if(self.__sess_obj.utype.carer_id != None):
					user = self.userExistByID(self.__sess_obj.utype.carer_id)
					if(user != None):
						user.printDetails()
					else:
						print('Person does not exist')
				else:
					print('You dont have any carer')

			elif(ch == '3'):
				self.listUsers('Young')
			elif(ch == '4'):
				print(self.__sess_obj.utype.pending_request_ids)
			elif(ch == '5'):
				self.approveRequest()
			elif(ch == '6'):
				self.__sess_obj.utype.carer_id = None
				print('Successfully Removed Carer')
			elif(ch == '7'):
				self.logout()
				break
			else:
				print('Wrong Choice')

	def approveRequest(self):
		ch = input('Enter one of the Carer ID which is requesting: ')

		if(self.isType(ch,'Young') and self.haveSlots(ch) and self.isRequesting(ch)):
			self.__sess_obj.utype.carer_id = ch
			self.__sess_obj.utype.pending_request_ids = []
		else:
			print('Given ID is invalid or its slots are full')


	def listUsers(self,utype):
		for profile in self.profile_list:
			#print(profile.utype.__name__)
			if(profile.utype.__name__ == utype):
				if(getattr(profile,'ratings') == 0):
					print(getattr(profile,'name'),'0')
				else:
					print(getattr(profile,'name'),getattr(profile,'ratings')/getattr(profile,'no_of_rating'))

	def logout(self):
		self.__sess_id = None
		self.__sess_pwd = None

		print('Logged out Successfully')

	def checkSession(self):
		if(self.__sess_id == None and self.__sess_pwd == None):
			return False
		else:
			return True

	def createSession(self,uname,pwd):
		self.__sess_id = uname
		self.__sess_pwd = pwd

		print('Logged in and Session created')

	def searchUserTakingCare(self):
		young_list = set()
		for profile in self.profile_list:
			if(profile.utype.__name__ == 'Old'):
				if(profile.utype.carer_id != None):
					young_list.add(profile.utype.carer_id)

		for user in young_list:
			for profile in self.profile_list:
				if(getattr(profile,'id') == user):
					profile.printDetails()

	def searchUserGettingCare(self):
		for profile in self.profile_list:
			if(profile.utype.__name__ == 'Old'):
				if(profile.utype.carer_id != None):
					profile.printDetails()		

	def registerUser(self):
		name = input('Enter Name: ')
		age = input('Enter Age: ')
		uname = input('Enter Username: ')

		while(True):
			if(self.userExist(uname)):
				uname = input('Username Exist please choose different username: ')
			else:
				break
		pwd = input('Enter Password: ')

		utype = input('Type of user(Case Sensitive): Old/Young: ')

		self.profile_list.append(Profile(self.id_counter,name,age,utype,uname,pwd))

		self.id_counter += 1

		print('User Created Successfully')

	def isRequesting(self,id):
		if(id in self.__sess_obj.utype.pending_request_ids):
			return True
		return False

	def haveSlots(self,id):
		for profile in self.profile_list:
			if(getattr(profile,'id') == id and len(profile.utype.caring_ids)<3):
				return True
		return False

	def isType(self,id,utype):
		for profile in self.profile_list:
			if(getattr(profile,'id') == id and profile.utype.__name__ == utype):
				return True
		return False

	def userExistByID(self,id):
		for profile in self.profile_list:
			if(getattr(profile,'id') == id):
				return profile

		return None

	def userExist(self,uname):
		for profile in self.profile_list:
			if(getattr(profile,'uname') == uname):
				return True

		return False

	def printOptions(self,menu):
		print('\n---------------------------\n')
		for option in menu:
			print(option)
		print('\n---------------------------\n')

ed = EdYoda()