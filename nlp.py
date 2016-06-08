import nltk
sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good. I am fine."""
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

print tokens
print tagged