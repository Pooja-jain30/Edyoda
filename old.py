class Old:

	__name__ = 'Old'

	def __init__(self):

		self.carer_id = None
		self.pending_request_ids = []

	def printDetails(self):
		print('Taking Cared By: ',self.carer_id)
		print('Requested By: ',self.pending_request_ids)