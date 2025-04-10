from simple_tokenizer import SimpleTokeinzerV1, SimpleTokeinzerV2
from create_token import vocab

tokenizer = SimpleTokeinzerV2(vocab)

text1 = "Hello do you like tea."
text2 = "In the sunlit terraces of palace."

text = " |endoftext| ".join([text1, text2])
print(text)

ids = tokenizer.encode(text)
print(ids)
print(tokenizer.decode(ids))