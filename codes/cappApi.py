# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:45:47 2019

@author: Winchester
"""

import flask
import json
import nltk
import pandas as pd
from nltk import word_tokenize
from flask import request,Flask

app = Flask(__name__)

class WordPreprocess:
    
    def __init__(self):
        self.num_of_words = 2
                
    def top_words(self,text):
        
        word_tokens = word_tokenize(text)
        word_tokens = [word for word in word_tokens if len(word)>2]
        text_df = pd.DataFrame({'words':word_tokens})
        count_dict = dict(text_df.words.value_counts())
        top_words = list(count_dict.keys())[:self.num_of_words]
        return top_words

    def last_words(self,text):
        
        word_tokens = word_tokenize(text)
        word_tokens = [word for word in word_tokens if len(word)>2]
        text_df = pd.DataFrame({'words':word_tokens})
        count_dict = dict(text_df.words.value_counts())
        last_words = list(count_dict.keys())[-self.num_of_words:]
        return last_words


#if __name__=='__main__':
#    word_process_obj = WordPrepocess()
#    #word_process_obj.num_of_words = 4
#    text = """HOUSTON: US President Donald Trump is expected to deliver a major, 30-minute speech on India and Indian Americans at the "Howdy, Modi!" event here in the world's energy capital on Sunday, which US officials asserted would bring fresh energy in the long-lasting relationship between the two democracies.
#Contrary to what was reported earlier, Trump, the 45th president of the United States, is no longer making a guest appearance or making a notional brief remark at the diaspora event.
#Trump, who as a Republican presidential candidate in 2016 promised to be India's best friend, is flying to Houston only to attend the "Howdy, Modi!" event.
#Full coverage of Howdy Modi
#As per the schedule released by the White House on late Saturday night, Trump will spend 100 minutes at the NRG Stadium.
#While the duration of his speech is not yet known, it is believed his remarks could last as long as 30 minutes.
#He is also expected to be present in the audience during Prime Minister Narendra Modi's address.
#More than 50,000 Indian-Americans from across the country have registered for the "Howdy, Modi!" event, the largest-ever gathering of this minority but effluent ethnic community in the US.
#"By coming to Houston and attending the "Howdy, Modi!" event, he (Trump) has won the hearts of Indian-Americans. He will earn more votes from Indian Americans in the 2020 presidential elections," eminent Indian-American community leader from Indiana Bharat Barai told PTI in an interview"""
#    least_words = word_process_obj.least_words(text)
        
        