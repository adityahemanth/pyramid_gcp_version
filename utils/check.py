# a class to check extracted 
# term validity check 

# [START check]

class check:

	# function that checks if all the 
	# letters in the extracted term are
	# ASCII characters

	def _validate_word(self, word):

		for letter in word:
			if not ord(letter) < 128:
				return False


		return True



	# function to strip a word of 
	# numbers. 

	def _clean_word(self, word):

		new_word = ''
		for letter in word:
			if letter.isalpha() or letter.isdigit():
				new_word += letter

		return new_word


# [END check]