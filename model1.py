import pandas as pd


class Tokenizer:
    def __init__(self):
        import pandas as pd

        def spacy_tokenizer(sentence):
            import spacy
            nlp = spacy.load('en_core_web_md')
            mytokens = nlp(sentence)
            mytokens = [word.lemma_ for word in mytokens if not word.is_punct and not word.is_stop]
            return mytokens

        self.t = pd.read_pickle("./tf_idf_vectorizor.pkl")

    def encode(self, x):
        return self.t.transform(x)


model = pd.read_pickle('./tf_idf_logistic_reg.pkl')

tokenizer = Tokenizer()

