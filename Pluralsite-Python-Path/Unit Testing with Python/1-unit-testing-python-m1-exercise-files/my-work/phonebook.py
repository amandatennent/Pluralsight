class Phonebook:
	def __init__(self):
		self.entries = {}

	def add(self, name, number):
		self.entries[name] = number

	def lookup(self, name):
		return self.entries[name]

	def is_consistent(self):
		for key1 in self.entries.keys():
			for key2 in self.entries.keys():
				if key1 != key2:
					if self.entries[key1].startswith(self.entries[key2]):
						return False
		return True

	def get_names(self):
		return list(self.entries.keys())

	def get_numbers(self):
		return list(self.entries.values())


