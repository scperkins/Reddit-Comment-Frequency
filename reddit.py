import praw
import re
from collections import Counter
import matplotlib.pyplot as plt

#Constants
COMMENT_LIMIT = 10
WORD_LIMIT = 10

#Globals
user_agent = ("/u/dyingtosaythis 's first reddit thing")
r = praw.Reddit(user_agent=user_agent)

def enterUser():
	'''Enter the username from the command line'''
	Trying = True
	while Trying:
		user_name = raw_input("Enter the username of a Redditor: ")
		#Check if the user actually exists
		try:
			user = r.get_redditor(user_name)
		except Exception, e:
			print "Username not found"
		else: Trying = False
	
	return user

def get_word_count(user):

	com = user.get_comments(limit=COMMENT_LIMIT, sort='new', time='all')
	com = '[%s]' % ','.join(map(str,com))
	words = re.findall(r'\w+', com)

	word_counter = 0
	while word_counter < WORD_LIMIT:

		for word in words: 
			word_count = Counter(words)
		word_counter += 1	
	
	return dict(word_count)


def gen_histogram(word_count):
	'''prints a histogram of most common occurences of the top 10 words'''
	plt.bar(range(len(word_count)), word_count.values(), align='center')
	plt.xticks(range(len(word_count)), word_count.keys())
	plt.xlabel('Words')
	plt.ylabel('Frequency')
	plt.title
	plt.show()

def main():
		
	user = enterUser()
	comments = get_word_count(user)
	histogram = gen_histogram(comments)
	print histogram
	#print comments


if __name__ == "__main__":
	main()