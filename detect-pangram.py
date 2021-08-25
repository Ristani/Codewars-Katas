"""
A pangram is a sentence that contains every single letter of
the alphabet at least once. For example, the sentence
"The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True
if it is, False if not. Ignore numbers and punctuation.
"""

def is_pangram(s):
	# Create an empty list to store unique characters
	set = []
	# Case doesn't matter, so make them all lower for simplicity
	s = s.lower()
	# For each character in the string
	for c in s:
		# Check if it's a letter and not in the list
		if c.isalpha() and c not in set:
			# Then add it
			set.append(c)
	# If the set contains exactly 26 characters(a-z) return True, else False
	return len(set) == 26