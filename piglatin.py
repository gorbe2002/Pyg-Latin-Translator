pyg = 'ay' # add after new word 

original = raw_input('Enter a word: ')

if len(original) > 0 and original.isalpha():
  word = original.lower() # outputs word in lowercase
  first = word[0] # takes first character of inputed word
  new_word = word + first + pyg
  new_word = word[1:len(new_word)] + first + pyg
  # outputs slice between 2nd and last character and first character and 'ay'
  
  print original # Prints input
  print "Your word in Pig Latin: " + new_word
else:
  print 'Invalid word' # if word is invalid 
