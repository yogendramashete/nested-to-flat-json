# Function for flattening
# json
def flatten_json(y):
	out = {}

	def flatten(x, name =''):
		
		# If the Nested key-value
		# pair is of dict type
		if type(x) is dict:
			
			for a in x:
				flatten(x[a], name + a + '.')
				
		# If the Nested key-value
		# pair is of list type
		#elif type(x) is list:
			
		#	i = 0
			
		#	for a in x:				
		#		flatten(a, name + str(i) + '_')
		#		i += 1
		else:
			out[name[:-1]] = x

	flatten(y)
	return out


# for a array value of a key
unflat_json = {
  'user': {
    'Rachel': {
      'UserID': 1717171717,
      'Email': 'rachel1999@gmail.com',
      'friends': [
        'John',
        'Jeremy',
        'Emily'
      ]
    }
  }
}


# Driver code
print(flatten_json(unflat_json))

