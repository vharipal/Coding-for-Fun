from urllib.request import urlopen
from bs4 import BeautifulSoup

#points
passing_point = 25
rushing_point = 10
receiving_point = 10
td_point = 6
passing_td_point = 4
interception_point = -2
fumble_point = -2

#Web Scraping

url = 'https://www.pro-football-reference.com/years/2021/passing.htm'

html = urlopen(url)
stats_page = BeautifulSoup(html, "html.parser")

column_headers = stats_page.findAll('tr')[0]
column_headers = [i.getText() for i in column_headers.findAll('th')]

rows = stats_page.findAll('tr')[1:]

qb_stats = []
qb_rank = []

for i in range(len(rows)):
    qb_stats.append([col.getText() for col in rows [i].findAll('td')])

#list has empty row at this index
bad_num = 29

#cleaning up data
for i in range(len(qb_stats)):
    if i != bad_num:
        del qb_stats[i][2:4]
        del qb_stats[i][3:9]
        del qb_stats[i][4]
        del qb_stats[i][5:11]
        del qb_stats[i][6:]
        qb_stats[i][3] = int(qb_stats[i][3])/int(qb_stats[i][2])
        qb_stats[i][4] = int(qb_stats[i][4])/int(qb_stats[i][2])
        del qb_stats[i][2]
        qb_rank.append(qb_stats[i])
        
    else:
        bad_num += 31



#Web Scraping
url = 'https://www.pro-football-reference.com/years/2021/rushing.htm'

html = urlopen(url)
stats_page = BeautifulSoup(html, "html.parser")

column_headers = stats_page.findAll('tr')[0]
column_headers = [i.getText() for i in column_headers.findAll('th')]

rows = stats_page.findAll('tr')[1:]

rb_stats = []
rb_rank = []

for i in range(len(rows)):
    rb_stats.append([col.getText() for col in rows [i].findAll('td')])

#empty rows
del rb_stats[0]
bad_num = 29

#trim data
for i in range(len(rb_stats)):
    if i != bad_num:
      del rb_stats[i][2:4]
      del rb_stats[i][3:6]
      del rb_stats[i][4:7]
      rb_stats[i][3] = int(rb_stats[i][3])/int(rb_stats[i][2])
      rb_stats[i][5] = int(rb_stats[i][5])/int(rb_stats[i][2])
      del rb_stats[i][2]
      rb_rank.append(rb_stats[i])
        
    else:
        bad_num += 31



#Web Scraping
url = 'https://www.pro-football-reference.com/years/2021/receiving.htm'

html = urlopen(url)
stats_page = BeautifulSoup(html, "html.parser")

column_headers = stats_page.findAll('tr')[0]
column_headers = [i.getText() for i in column_headers.findAll('th')]

rows = stats_page.findAll('tr')[1:]

wr_stats = []
wr_rank = []

for i in range(len(rows)):
    wr_stats.append([col.getText() for col in rows [i].findAll('td')])

bad_num = 29

for i in range(len(wr_stats)):
    if i != bad_num:
        del wr_stats[i][2:4]
        del wr_stats[i][3:9]
        del wr_stats[i][4:8]
        wr_stats[i][3] = int(wr_stats[i][3])/int(wr_stats[i][2])
        wr_stats[i][5] = int(wr_stats[i][5])/int(wr_stats[i][2])
        del wr_stats[i][2]
        wr_rank.append(wr_stats[i])
        
    else:
        bad_num += 31



#web scraping
url = 'https://www.pro-football-reference.com/years/2021/opp.htm'

html = urlopen(url)
stats_page = BeautifulSoup(html, "html.parser")

column_headers = stats_page.findAll('tr')[0]
column_headers = [i.getText() for i in column_headers.findAll('th')]

rows = stats_page.findAll('tr')[1:]

def_stats = []
def_rank = []

for i in range(len(rows)):
    def_stats.append([col.getText() for col in rows [i].findAll('td')])

del def_stats[0]

for i in range(32):

    del def_stats[i][1:7]
    del def_stats[i][3:4]
    del def_stats[i][4]
    del def_stats[i][7:10]
    del def_stats[i][9:]
    def_rank.append(def_stats[i])

print("Top 5 qbs")
#player, team, tdspg, intspg, ypg
for i in range(5):
    print(qb_rank[i])

print("\nTop 5 rbs")
#player, team, tdpg, ypg, fumblespg
for i in range(5):
    print(rb_rank[i])
    
print("\nTop 5 wrs")
#player, team, tdspg, ypg, fumblespg
for i in range(5):
    print(wr_rank[i])

print("\nTop 5 defenses")
#team, fumbles, completions, passing yards, passing tds, ints, rushing yards, rushing tds
for i in range(5):
    print (def_rank[i])

with open("2022 schedule") as file:
    for line in file:
        print(line)
        

