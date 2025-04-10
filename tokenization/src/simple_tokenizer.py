import re
class SimpleTokeinzerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {v: k for k, v in self.str_to_int.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\´]|--|\s)', text)

        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[item] for item in preprocessed]
        return ids
    
    def decode(self, ids):
        text = " ".join([self.int_to_str[item] for item in ids])
        text = re.sub(r'([,.?!"()\´])', r'\1', text)
        return text	
    
class SimpleTokeinzerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {v: k for k, v in self.str_to_int.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\´]|--|\s)', text)

        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [
            item if item in self.str_to_int
            else "<|unk|>" for item in preprocessed
        ]
        
        ids = [self.str_to_int[item] for item in preprocessed]
        return ids
    
    def decode(self, ids):
        text = " ".join([self.int_to_str[item] for item in ids])
        text = re.sub(r'([,.?!"()\´])', r'\1', text)
        return text	

