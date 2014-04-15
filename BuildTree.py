import sys, re, os, time
import urllib2
import pprint
baseUrl = 'http://en.wikipedia.org/wiki/'
DEBUG = False
MAX_DEPTH = 10000000
#http://preshing.com/20110924/timing-your-code-using-pythons-with-statement/

class Timer:    
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
#http://interactivepython.org/courselib/static/pythonds/BasicDS/deques.html
class Deque:
    def __init__(self):
        self.items = []
    def __str__(self):
        string = ""
        for i in self.items:
            string = string + i + ","
        return string
    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
class ParsePage:
    def __init__(self,start,end):
        self.entries = 0
        #clean up user input
        start = start.replace(" ","_")
        end = end.replace(" ","_")
        self.start = end
        self.end = start
        self.deque = Deque()
        self.graph = {'dummy_XXX_JDKD': ['foo','bar']}#insert dummy node
        self.createGraph(start)#add first real node

        #keep adding elements
        while not (self.deque.isEmpty()) and self.entries < MAX_DEPTH:
                value = self.deque.removeFront()
                if DEBUG:
                    print("Just removed from deque: " + str(value))
                self.createGraph(value)
        if DEBUG:
            pprint.pprint(self.graph)
        for key in self.graph.keys():
            print(key)
            for link in self.graph[key]:
                if(link == end):
                    print("Can get to end: " + key + "=>" + str(link))
        
    #newNode -> name of thing to add to the dictionary    
    def createGraph(self,newNode):
        if DEBUG:
            print(newNode)
        if self.graph.has_key(newNode):
            return #already processed
        self.entries += 1 
        links = self.getLinks(newNode)
        self.graph[newNode] = links
        for link in links:
            if DEBUG:
                print("adding link: " + link)
            self.deque.addRear(link)
        if DEBUG:
            print(self.deque)
            
    def getLinks(self,name):
        try:
            html = urllib2.urlopen(baseUrl + name).read()
        except:
            print("UNABLE TO OPEN addr for: " + name)  
            return []            
        match = re.findall(re.escape('href="/wiki/')+ '(\w+)\"',html)
        links = list(set(match)) #deletes duplicate entries
        if match and DEBUG:
            print("Length: " + str(len(match)) + "Remove Duplicates: " + str(len(list(set(match)))))
        return links 
#temp = ParsePage("testPage.html")
with Timer() as t:
    temp = ParsePage("Baseball","Portland Trail Blazers")
print'Took %.03f sec.' % t.interval