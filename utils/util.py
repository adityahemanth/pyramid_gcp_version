#!/usr/bin/env python

# Utility class that allows for 

# [START util]
class util:

	# checks whether the category represented 
	# by node1 is contained within that of node2
	def contains( self, node1, node2):

		# inital filter
		node1 = self.filter(node1)
		node2 = self.filter(node2)

		# return false if either of the 
		# nodes is none

		if not node1 or not node2:
			return False


		if node1 == node2:
			return True

		# if root return true
		if node1[0] == '1':
			return True

		if node1[0] != node2[0]:
			if len(node1) == 1 and len(node2) == 1:
				return True

			return False

		else:
			if len(node1) == 1:
				return True


		if node1[1] != node2[1]:
			if not (node1[1].isdigit() and node2[1].isdigit()):
				return False

		# match the first letters of the two letters to determine they 
		# belong in the same branch

		while True:
			if node1 and node2:
				if node1[0] == node2[0] and not node1[0].isdigit():
					node1 = node1[1:len(node1)]
					node2 = node2[1:len(node2)]

				else:
					break

			else:
				break


		# check if node1 and node2 are not None
		if node1 and node2:

			if not node1[0].isdigit():
				return False

			if not node2[0].isdigit():
				return False

			else:

				# split the node at '-'
				node1 = node1.split('-')
				node2 = node2.split('-')

				if len(node1) == 1:
					node1.append(node1[0])


				if len(node2) == 1:
					node2.append(node2[0])


				for node in [node1, node2]:
					for i in range(2):
						node[i] = node[i].split('.')

				for y in range(2):
					for x in node2[y]:
						if not x.isdigit():
							return True

				for x in node1[0]:
					if not x.isdigit():
						return False

				for i in range(2):

					if len(node1[i]) > 1:
						node1[i] = float(node1[i][0]) + float(node1[i][1])/ 10 ** len(node1[i][1])

					else:
						node1[i] = float(node1[i][0])

					if len(node2[i]) > 1:
						node2[i] = float(node2[i][0]) + float(node2[i][1])/ 10 ** len(node2[i][1])

					else:
						node2[i] = float(node2[i][0])


				

				if node1[0] == node2[0] and node1[1] == node2[1] :
					return False

				if node1[0] <= node2[0] and node1[1] >= node2[1] :
					return True


				else:
					return False



	# filter to stop the node's 
	# LCC number of trailing 
	# year values or space characters

	def filter(self, node):
		if ' ' in node:
			node = node.split(' ')
			node = node[0]

		
		for i in range(len(node) ):
			if node[i] == '.' and i < len(node) - 1:
				if not node[i + 1].isdigit():
					try:
						node.replace( node[i+1], '0')
					except:
						print node

		return node



	# a function to test the validity of a
	# term before comparision
	
	def validate(self, node):

		if not node:
			return False

		if node[0].isdigit():
			return False


		for letter in node:
			if letter.isdigit():
				return True

		return False


# [END util]







