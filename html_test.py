#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sgmllib import SGMLParser
from re_test import extract_data

class ProdInfoParser(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.products = {}
        
    def start_span(self, attrs):
        attrs = dict(attrs)
        #print attrs
        if attrs.get('productid') and attrs.get('yhdprice'):
            #print attrs
            productId = attrs.get('productid')
            if not self.products.get(productId):
                self.products[productId] = {}
            self.products[productId]['yhdprice'] = attrs.get('yhdprice')
            #print self.products
            
    def start_a(self, attrs):
        attrs = dict(attrs)
        #print attrs
        if attrs.get('id') and attrs.get('pmid') and attrs.get('title'):
            #print attrs
            productId = attrs.get('id').split('_')[1]
            if not self.products.get(productId):
                self.products[productId] = {}
            self.products[productId]['title'] = attrs.get('title')
            result = extract_data(attrs.get('title'))
            if result:
#                net, unit = result
                self.products[productId]['net'] = result
                
            #print self.products

    def output(self):
        return self.products

#    def parse_declaration(self, i):
#        SGMLParser.parse_declaration(self, i)
#        return -1
    
def test_run():
    parser = ProdInfoParser()
    f = open('yhd.html')
    c = f.read()
 #   print c[:100]
    parser.feed(c)
    f.close()
    d = parser.output()
    print d
    for k, v in d.items():
        result = extract_data(v['title'])
        if result:
            net, unit = extract_data(v['title'])
            unit_price = float(v['yhdprice']) / net * 500
            print k
            print v['title']
            print "Unit price: ￥%.2f/500%s" % (unit_price, unit)
    #print data[:1000]

if __name__ == "__main__":
    test_run()
#    print '中文'
