# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# Regex Version of strip()

import re

# takes input of a target string

target_string = input("> Please enter the string text you want to strip from.\n")

# takes input of chars to strip from start and/or end of target string

char_toStrip = input("> Please enter the characters/string text you want to strip.\n")

# strips the characters from start and/or end of target string



#####################################
# START STRIP TARGET CHAR
#####################################

# use Regex to match the start of the string with char_toStrip

def start_strip(char_toStrip,target_string):
	# https://regexr.com/3kjnf
	# char_processed = str(char_toStrip) # ensure character input is a string
	# print(char_processed + " is processed")

	start_strip = re.compile(r'^' + char_processed) # you need to join the string with a variable otherwise it sees char_processed as a string not a variable

	target_found = start_strip.search(target_string)
	print(target_found)

	return start_strip.sub('',target_string)

#####################################
# END START STRIP TARGET CHAR
#####################################



#####################################
# END STRIP TARGET CHAR
#####################################

# use Regex to match the end of the string with char_toStrip

def end_strip(char_toStrip,target_string):
	# https://regexr.com/3kjnl
	char_processed = str(char_toStrip) # ensure character input is a string
	print(char_processed + " is processed")

	end_strip = re.compile(r''+char_processed+'$') # you need to join the string with a variable otherwise it sees char_processed as a string not a variable
	# you can't use `rchar_processed` or `r + char_processed` because Python will see it as an undeclared variable 

	target_found = end_strip.search(target_string)
	print(target_found)

	return end_strip.sub('',target_string)

#####################################
# END END STRIP TARGET CHAR
#####################################



#####################################
# WHITE SPACE STRIP
#####################################

# strip white space characters from start and end of string if no arguments are passed
# i.e. char_toStrip = None (there's no input)
# i.e. char_toStrip = '' (there's no input, an empty string)
# 

def whitespace_start_strip(target_string):
	# whitespace start strip https://regexr.com/3kjnu
	ws_start_strip = re.compile(r'''
		(
			^(\s*) # match the whitespace from start of string
		)
	''', re.VERBOSE)

	return ws_start_strip.sub('',target_string)

def whitespace_end_strip(target_string):
	# whitespace end strip https://regexr.com/3kjo7
	ws_end_strip = re.compile(r'''
			(
				(\s*)$ # match the whitespace from start of string
			)
		''', re.VERBOSE)

	return ws_end_strip.sub('',target_string)

# returns copy of target string after characters stripped from start and/or end

#####################################
# END WHITE SPACE STRIP
#####################################

#####################################
# REGEX STRIP EQV
#####################################

def regex_strip(char_toStrip,target_string):
	if char_toStrip != '' or len(char_toStrip) > 0: # if characters to strip is not empty, and arg is passed
		process_word = start_strip(char_toStrip,target_string)
		print(process_word + " <strip target from start>")
		process_word = end_strip(char_toStrip,process_word)
		print(process_word + " <strip target from end>")
		return process_word
	else: # if characters to strip is empty, arg is not passed
		process_word = whitespace_start_strip(target_string)
		# print(process_word + " <strip white space from start>" )
		process_word = whitespace_end_strip(process_word)
		# print(process_word + " <strip white space from end>")
		return process_word

#####################################
# END REGEX STRIP EQV
#####################################



#####################################
# EXECUTE
#####################################

print(regex_strip(char_toStrip,target_string))

#####################################
# END EXECUTE
#####################################
