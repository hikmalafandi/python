translation = str.maketrans({'h': 'b', 'l': 'r'})
text = 'hikmal'
translation_text = text.translate(translation)

print('text:', text)
print('translation_text:', translation_text)