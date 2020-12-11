# Python program for insert and search 
# operation in a Trie 

import pickle
import string
from string import digits
import os

class TrieNode: 
	
	# Trie node class 
	def __init__(self): 
		self.children = {}

		# isEndOfWord is True if node represent the end of the word 
		self.isEndOfWord = False
		self.count = 0

	def getChildren(self) :
		children = self.children
		return children.keys()

class Tkinter :
	def __init__(self) :
		self.root = Tk()
		self.btns = []

class Trie: 
	
	# Trie data structure class 
	def __init__(self): 
		self.root = self.getNode() 
		self.word_list = []


	def getNode(self): 
		return TrieNode()


	def insert(self,key): 
		pCrawl = self.root 
		length = len(key) 
		key = key.lower()

		for level in range(length): 
			a = key[level]

			if a not in pCrawl.children: 
				pCrawl.children[a] = self.getNode() 
			pCrawl = pCrawl.children[a] 

		pCrawl.isEndOfWord = True
		pCrawl.count += 1

	def search(self, key): 
		pCrawl = self.root 
		length = len(key) 
		for level in range(length): 
			index = key[level]
			if(index in pCrawl.children) :
				pCrawl = pCrawl.children[index]
			else :
				pCrawl = None
				break 

		return pCrawl != None and pCrawl.isEndOfWord 

	def suggestionsRec(self, node, word):  
		if node.isEndOfWord: 
			self.word_list.append((word, node.count)) 

		childs = node.getChildren()

		for i in childs: 
			self.suggestionsRec(node.children[i], word + i) 

	def printAutoSuggestions(self, key): 
		if(key[-1]==" ") :
			print("don't use space at the end")
			return
		key = key.split()[-1]
		node = self.root 
		not_found = False
		temp_word = '' 

		for index in list(key): 
			if index not in node.children :
				not_found = True
				break
			temp_word += index
			node = node.children[index] 

		if not_found: 
			return 0
		childs = node.getChildren()

		if(node.isEndOfWord and len(childs)==0): 
			self.word_list.append(temp_word, node.count)

		else :
			self.suggestionsRec(node, temp_word) 

		words = sorted(self.word_list, key=lambda x : (x[1], x[0]), reverse=True)[:5]

		for word in words: 
			print(word[0])
		self.word_list=[] 
		return 1

def createTrie() :
	t = Trie() 

	data = open("shakespeare.txt", "r").read()
	data = data.translate(data.maketrans("","", string.punctuation))
	# remove_digits = data.maketrans('', '', digits)
	# data = data.translate(remove_digits)
	lines = data.splitlines()

	for line in lines :
		words = line.split()
		for word in words :
			t.insert(word) 

	data = open("warpeace.txt", "r").read()
	data = data.translate(line.maketrans("","", string.punctuation))
	# remove_digits = data.maketrans('', '', digits)
	# data = data.translate(remove_digits)
	lines = data.splitlines()
	
	for line in lines :
		words = line.split()
		for word in words :
			t.insert(word) 

	pickle.dump(t, open("corpus1.p", 'wb') )

# driver function 
def main(): 
	t = pickle.load( open("corpus1.p", "rb" ) )
	x = input("Enter word: ")
	t.printAutoSuggestions(x)

if __name__ == '__main__': 
	if(not os.path.isfile("corpus1.p")) :
		createTrie()
	main() 

# This code is contributed by Atul Kumar (www.facebook.com/atul.kr.007) 
