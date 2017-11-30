import markovify

with open("/home/pi/markovFakeNews/test/corpus.txt") as f:
    text = f.read()

# Build model.
textModel = markovify.Text(text)

for i in range(20):
    print(textModel.make_short_sentence(280))