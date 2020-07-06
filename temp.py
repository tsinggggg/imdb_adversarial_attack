if __name__ == '__main__':
    # provide data and use exiting model
    # import os
    # os.system("""
    # textattack attack --recipe textfooler --dataset-from-file "test_data.py" --model bert-base-uncased-mr
    # """)
    # provi
    import os
    import spacy
    nlp = spacy.load('en_core_web_md')
    def spacy_tokenizer(sentence):
        mytokens = nlp(sentence)
        mytokens = [word.lemma_ for word in mytokens if not word.is_punct and not word.is_stop]
        return mytokens


    os.system("""
    textattack attack --model-from-file model1.py --recipe deepwordbug --num-examples 1000
    """)


    # csv_data = """1,"Wall St. Bears Claw Back Into the Black ( Reuters ) . Reuters - Short - sellers , Wall Street 's dwindling band of ultra - cynics , are seeing green again ."
    # 1,"Carlyle Looks Toward Commercial Aerospace ( Reuters ) . Reuters - Private investment firm Carlyle Group , which has a reputation for making well - timed and occasionally controversial plays in the defense industry , has quietly placed its bets on another part of the market ."
    # 0,Oil and Economy Cloud Stocks ' Outlook ( Reuters ) . Reuters - Soaring crude prices plus worries about the economy and the outlook for earnings are expected to hang over the stock market next week during the depth of the summer doldrums .
    # 0,"Iraq Halts Oil Exports from Main Southern Pipeline ( Reuters ) . Reuters - Authorities have halted oil export flows from the main pipeline in southern Iraq after intelligence showed a rebel militia could strike infrastructure , an oil official said on Saturday ."
    # 1,"Oil prices soar to all - time record , posing new menace to US economy ( AFP ) . AFP - Tearaway world oil prices , toppling records and straining wallets , present a new economic menace barely three months before the US presidential elections ."
    # 0,"Stocks End Up , But Near Year Lows ( Reuters ) . Reuters - Stocks ended slightly higher on Friday but stayed near lows for the year as oil prices surged past # 36;46 a barrel , offsetting a positive outlook from computer maker Dell Inc. ( DELL.O )"
    # 1,"Money Funds Fell in Latest Week ( AP ) . AP - Assets of the nation 's retail money market mutual funds fell by # 36;1.17 billion in the latest week to # 36;849.98 trillion , the Investment Company Institute said Thursday ."
    # 0,"Fed minutes show dissent over inflation ( USATODAY.com ) . USATODAY.com - Retail sales bounced back a bit in July , and new claims for jobless benefits fell last week , the government said Thursday , indicating the economy is improving from a midsummer slump ."
    # 1,"Safety Net ( Forbes.com ) . Forbes.com - After earning a PH.D. in Sociology , Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of # 36;70,000 . Soon after , a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer . But , at 32 , "" buying insurance was the furthest thing from my mind , "" says Riley ."
    # 0,"Wall St. Bears Claw Back Into the Black . NEW YORK ( Reuters ) - Short - sellers , Wall Street 's dwindling band of ultra - cynics , are seeing green again ."
    # """
    #
    # open('test_data.csv', 'w').write(csv_data)
    #
    # import pandas as pd
    # df = pd.read_csv('test_data.csv')
    # df.columns = ['label', 'text']
    # df[['text', 'label']].values.tolist()
    #
    # data_py = """import pandas as pd
    # df = pd.read_csv('test_data.csv')
    # df.columns = ['label', 'text']
    # dataset = df[['text', 'label']].values.tolist()
    # """
    #
    # open('test_data.py', 'w').write(data_py)