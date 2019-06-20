# -*- coding: utf-8 -*-
"""Text an tokens normalization module

This module defines the class Normalizer wich is meant to be used
for text normalization

"""
import nltk
from nltk.tokenize import word_tokenize
import unidecode
import string

class Normalizer:
	"""Defines a set of operations to normalize text

	Attributes:
		sent_tokenizer: nltk sentence tokenizer
		word_tokenizer: nltk word tokenizer
		stemmer: nltk stemmer
		stopwords: nltk list of Portuguese words "not relevant for meaning"
	"""
	def __init__(self):

		self.sent_tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')
		self.word_tokenizer = word_tokenize
		self.stemmer = nltk.stem.RSLPStemmer()
		self.stopwords = nltk.corpus.stopwords.words('portuguese')


	def remove_punctuation(self, text):
		"""Removes punctuation from a string text

		:param text: the text in string format
		:return: text without punctuation
		"""
		return text.translate(str.maketrans('', '', string.punctuation))


	def remove_accents(self, text):
		"""Removes accents from a string text

		:param text: the text in string format
		:return: text without accents
		"""
		return unidecode.unidecode(text)


	def to_lowercase(self, text):
		"""Transforms a string text to lowercase

		:param text: the text in string format
		:return: the text in lowercase
		"""
		return text.lower()


	def tokenize_sentences(self, text):
		"""Splits a text in list by its sentences

		:param text: the text in string format
		:return: a list with each sentence from text
		"""
		return self.sent_tokenizer.tokenize(text)


	def tokenize_words(self, text):
		"""Splits a text in list by its words or punctuation characters

		:param text: the text in string format
		:return: a list containing each word and punctuation characters from text
		"""
		return self.word_tokenizer(text)


	def remove_stopwords(self, tokens):
		"""Removes words with only structural functions in a text

		:param tokens: a list of tokens
		:return: a list of tokens without stopwords
		"""
		return [token for token in tokens if token not in self.stopwords]


	def stemmize(self, tokens):
		"""Reduces words to their stem

		:param tokens: a list of tokens
		:return: a list of stem of each token with stemmized words
		"""

		stemized_words = []

		for word in tokens:
			stemized_words.append(self.stemmer.stem(word))

		return stemized_words
