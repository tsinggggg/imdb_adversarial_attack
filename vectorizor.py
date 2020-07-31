def spacy_tokenizer(sentence):
    import spacy
    nlp = spacy.load('en_core_web_md')
    mytokens = nlp(sentence)
    mytokens = [ word.lemma_ for word in mytokens if not word.is_punct and not word.is_stop]
    return mytokens