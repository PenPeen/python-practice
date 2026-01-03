def is_truthy(value):
	"""Returns True if the value is considered truthy, False otherwise."""
	if value:
		print("True")
	else:
		print("False")

is_truthy(1)        # Should print "True"
is_truthy(0)        # Should print "False"
is_truthy([1])	   	# Should print "True"
is_truthy([])      	# Should print "False"
is_truthy(True)		# Should print "True"
is_truthy(False)	# Should print "False"
is_truthy(None)		# Should print "False"
