import pandas as pd
import sys
sys.path.append("/home/qc/work/imdb_adversarial_attack")

# from imdb_adversarial_attack.vectorizor import spacy_tokenizer

# def spacy_tokenizer(sentence):
#     import spacy
#     nlp = spacy.load('en_core_web_md')
#     mytokens = nlp(sentence)
#     mytokens = [word.lemma_ for word in mytokens if not word.is_punct and not word.is_stop]
#     return mytokens
#
#
# spacy_tokenizer.__module__ = "vectorizor"


class Tokenizer:
    def __init__(self):
        import pandas as pd
        self.t = pd.read_pickle("~/work/imdb_adversarial_attack/tf_idf_vectorizor2.pkl")

    def encode(self, x):
        return self.t.transform(x)


model = pd.read_pickle('~/work/imdb_adversarial_attack/tf_idf_logistic_reg.pkl')

tokenizer = Tokenizer()

