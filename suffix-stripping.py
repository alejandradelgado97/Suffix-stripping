text = input('Enter a text: ')
words = text.split()
suffixes = ['ly','ing','ed']
new_words = []
for word in words:
  for suffix in suffixes:
    if word.endswith(suffix):
      word = word[:-len(suffix)]
  if len(word) > 8:
    word = word[:8]
  new_words.append(word)
  t = ' '
print(t.join(new_words))