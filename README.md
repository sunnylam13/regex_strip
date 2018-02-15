# Regex Strip Tool

a function that works like the strip() string method using regex

If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. 

Otherwise, the characters specified in the second argument to the function will be removed from the string.

## Example to test

from https://www.tutorialspoint.com/python/string_strip.htm

	str = "0000000this is string example....wow!!!0000000";
	print str.strip( '0' )

	0000000this is string0000000 example....wow!!!0000000 (don't want the 0's in the middle)
	this is string example....wow!!!             

https://regexr.com/

## REFERENCES

https://www.tutorialspoint.com/python/string_strip.htm

The method strip() returns a copy of the string in which all chars have been stripped from the beginning and the end of the string (default whitespace characters).

This method returns a copy of the string in which all chars have been stripped from the beginning and the end of the string.


