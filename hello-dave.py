import urllib2
from bs4 import BeautifulSoup

# create a file called wunder.txt which wil be csv so why call it txt? hmmm
f = open('wunder-data.txt', 'w')

# iterate through months and days
for m in range(1, 13):
    for d in range(1, 32):
        # check if already gone through month
        if(m == 2 and d > 28):
            break
        elif(m in [4, 6, 9, 11] and d > 30):
            break
        
        # open wunderground url
        timestamp = '2009' + str(m) + str(d)
        print "Getting data for " + timestamp
        url = "http://www.wunderground.com/history/airport/KBUF/2009/" + str(m) + "/" + str(d) + "/DailyHistory.html"
        page = urllib2.urlopen(url)
        
        # get temperature from page
        soup = BeautifulSoup(page)
        # dayTemp = soup.body.wxdata.b.string
        dayTemp = soup.findAll(attrs={"class":"wx-data"})[0].span.string
        
        # format month for timestamp
        if len(str(m)) < 2:
            mStamp = "0" + str(m)
        else:
            mStamp = str(m)
            
        # format day for timestamp
        if len(str(d)) < 2:
            dStamp = "0" + str(d)
        else:
            dStamp = str(d)
            
        # build timestamp
        timestamp = "2009" + mStamp + dStamp
        
        # write timestamp and temperature to file
        f.write(timestamp + "," + dayTemp + "\n")
        
# done getting data! close file ...
print "closing ..."
f.close()
