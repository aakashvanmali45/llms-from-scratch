import re
from simple_tokenizer import SimpleTokeinzerV1

with open("data/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

#Tokenization Scheme
preprocessed = re.split(r'([,.:;?_!"()\´]|--|\s)', raw_text)
preprocessed = [item for item in preprocessed if item.strip()]

#Arrange in alphabetical order
all_words = sorted(set(preprocessed))
all_words.extend(["|endoftext|","<|unk|>"])
vocab_size = len(all_words)

vocab = {token:integer for integer, token in enumerate(all_words)}

for i, item in enumerate(list(vocab.items())[12]):
    print(item)

