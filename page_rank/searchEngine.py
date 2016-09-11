"""Version: python2"""

import urllib2
from BeautifulSoup import *
from urlparse import urljoin

ignoreWords = set(['the','of','and','it','to','a','in','is','in','this','too','for'])

class webCrawler:
    
    def __init__(self, database):
        pass

    def __del__(self):
        pass

    def dbcommit(self):
        pass

    def getEntryId(self, table, field, value, createnew=True):
        return None

    def addToIndex(self, url, soup):
        print "Indexing %s" % url

    def getText(self, soup):
        return None

    def separateWords(self, text):
        return None

    def isIndexed(self, url):
        return False

    def addReferencelink(self, urlFrom, urlTo, linkText):
        pass

    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    c=urllib2.urlopen(page)
                except:
                    print "Could not open %s" % page
                    continue
                soup=BeautifulSoup(c.read())
                self.addToIndex(page,soup)

                links = soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url=urljoin(page,link['href'])
                        if url.find("'") is not -1:
                            continue
                        url=url.split('#')[0]
                        if url[0:4] is 'http' and not self.isIndexed(url):
                            newpages.add(url)
                        linkText=self.getText(link)
                        self.addReferencelink(page, url, linkText)

                self.dbcommit()
                        


    def createIndexTables(self):
        pass

