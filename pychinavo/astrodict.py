#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import urllib.request
import urllib.parse
import json

class astrodict:
    def __init__(self,isdev=False):
        self.__isdev=isdev
        
    def getUrl(self, call, params=None):
        url = 'http://astrodict.china-vo.org/' 
        if self.__isdev:
            url = 'http://lastrodict.china-vo.org/'
        url += call
        if params is None:
            response = urllib.request.urlopen(url)
        else:
            response = urllib.request.urlopen(url, urllib.parse.urlencode(params).encode('utf-8'))
        data = response.read().decode(response.headers.get_content_charset())
        j=json.loads(data)
        if j["count"]>0:
            return j["result"]
        return {}
    
    def publicwordscount(self):
        return self.getUrl("publicwordscount")
    
    def precise(self, word):
        call = 'precise?word={0}&fmt=json'.format(word)
        return self.getUrl(call)
    
    def fuzzy(self, word):
        call = 'fuzzy?word={0}&fmt=json'.format(word)
        return self.getUrl(call)
    
    def termdetails(self, id):
        call = 'termdetails?id={0}&fmt=json'.format(id)
        return self.getUrl(call)        
