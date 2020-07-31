# import sys
# sys.path.append("/home/qc/work/imdb_adversarial_attack")
import pickle
import pandas as pd
import torch


class Bunch(object):
    def __init__(self, adict):
        self.__dict__.update(adict)


class SklearnTokenizer:
    def __init__(self, tokenizer_path):
        # load tokenizer from file
        self.tokenizer = pickle.load(open(tokenizer_path, "rb"))

    def batch_encode(self, text_list):
        if isinstance(text_list[0], tuple):  # unroll tuples passed in by TextAttack
            text_list = [x[0] for x in text_list]
        encoded_text_matrix = self.tokenizer.transform(text_list)
        return torch.tensor(encoded_text_matrix.toarray())

    def encode(self, text):
        return self.batch_encode([text])


class SklearnModelWrapper:
    def __init__(self, model_path, feature_names):
        self.model = pickle.load(open(model_path, 'rb'))
        self.feature_names = feature_names

        # dummy attribute that will also not be necessary in the future
        def dummy_params():
            yield Bunch({'device': torch.device('cuda')})

        setattr(self.model, 'parameters', dummy_params)

    def __call__(self, tokenized_text_input):
        tokenized_text_df = pd.DataFrame(tokenized_text_input, columns=self.feature_names)
        return torch.tensor(self.model.predict_proba(tokenized_text_df))

    def to(self, *args):
        # dummy method that will not be necessary in the future
        return self


tokenizer = SklearnTokenizer('/home/qc/work/imdb_adversarial_attack/tf_idf_vectorizor2.pkl')
feature_names = tokenizer.tokenizer.get_feature_names()
model = SklearnModelWrapper('/home/qc/work/imdb_adversarial_attack/tf_idf_logistic_reg.pkl', feature_names)

