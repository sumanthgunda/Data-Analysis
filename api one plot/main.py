import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns
from flask import Flask,send_file,render_template
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import pymongo
from pymongo import MongoClient
import urllib.parse
import collections 

import numpy as np


username = urllib.parse.quote_plus('PTE')
password = urllib.parse.quote_plus('TCOE@123')
url = "mongodb+srv://{}:{}@cluster0.m1goo.mongodb.net/OlcademyCommunity?ssl=true&ssl_cert_reqs=CERT_NONE".format(username, password)
db_name='OlcademyCommunity'

cluster = pymongo.MongoClient(url)
db = cluster[db_name]


#objectid to category
b={}

a=list (db.categories.find({}))
for i in a:
  b[i['_id']]={}
  b[i['_id']]=i['name']

print(b)

c={}
d=list (db.posts.find({}))

for i in d:
    for j,l in b.items():
      if j==i['category']:
        if l in c:
          c[l]=i['num_of_views']+c[l]
        else:
          c[l]=i['num_of_views']
 


print(c)

c={}
d=list (db.posts.find({}))

for i in d:
    for j,l in b.items():
      if j==i['category']:
        if l in c:
          c[l]=i['num_of_views']+c[l]
        else:
          c[l]=i['num_of_views']
 
list1=c.keys()     

list2=c.values()

print(c)



print(list1)
print(list2)


l1 = np.array(list1)
l2 = np.array(list2)
print(l1,l2) 

def do_plot():
    import matplotlib.pyplot as plt
    
    plt.switch_backend('agg')
    
    plt.bar(list1,list2, color=['firebrick', 'green', 'blue', 'black', 'red',])
    plt.xlabel('Categories')
    plt.xticks(rotation=90) 
    plt.xticks(fontsize=3)
    plt.ylabel("views")
    plt.title('Categories Bar Plot')
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


from io import StringIO
import io
def do_plot2():
  
    db1=db['posts']

    info={}
    agg_result= db1.aggregate( 
        [{ 
        "$group" :  
            {"_id" : "$user_id",  
            "Total views" : {"$sum" :"$num_of_views"} 
            }} 
        ]) 
    for i in agg_result: 
        info[i['_id']]=i['Total views']
    info


    info={}
    agg_result= db1.aggregate( 
        [{ 
        "$group" :  
            {"_id" : "$user_id",  
            "Total shares" : {"$sum" :"$num_of_shares"} 
            }} 
        ]) 
    for i in agg_result: 
        info[i['_id']]=i['Total shares']
    info

    #objectid to likes
    f={}
    for i in db.posts.find({}):
      f[i['_id']]={}
      f[i['_id']]=i['likes']
    print(f)

    for x in db1.find({}, {'user_id':1,'likes':1, '_id':0}):
        print(x)

    imp={}
    for row in db1.aggregate( [ { "$project": { "likes": 1,"category":1, '_id':0 } } ] ):
        sum=0
        
        for i in row['likes']:
            if row['category'] in imp.keys():
                imp[row['category']]=imp[row['category']]+len(i)
                
            else:
                sum=sum+len(i)
                imp[row['category']]=sum
                #print(row['user_id'])
                #print(sum)

    imp

    likeslist={"IT & Software":120,"Personality Developement":120,"Marketing":192,"Lifestyle":72,"Photography":24,"Music":24,"Examination":72}

    print(likeslist.keys())
    print(likeslist.values())

    list3=likeslist.keys()     

    list4=likeslist.values()

    import matplotlib.pyplot as plt
    plt.switch_backend('agg')

    plt.bar(list3,list4, color=['firebrick', 'green', 'blue', 'black', 'red',])

    plt.xlabel('Categories')
    plt.xticks(rotation=90) 
    plt.ylabel("likes")
    plt.title('Categories Bar Plot')
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


def do_plot3():
  share={}


  for i in d:
      for j,l in b.items():
        if j==i['category']:
          if l in share:
            share[l]=i['num_of_shares']+share[l]
          else:
            share[l]=i['num_of_shares']
  


  print(share)

  list5=share.keys()
  list6=share.values()

  import matplotlib.pyplot as plt
  plt.switch_backend('agg')

  plt.bar(list5,list6, color=['firebrick', 'green', 'blue', 'black', 'red',])

  plt.xlabel('Categories')
  plt.xticks(rotation=90) 
  plt.ylabel("share")
  plt.title('Categories Bar Plot')
  bytes_image = io.BytesIO()
  plt.savefig(bytes_image, format='png')
  bytes_image.seek(0)
  return bytes_image

def do_plot4():
    spam={}


    for i in d:
        for j,l in b.items():
          if j==i['category']:
            if l in spam:
              spam[l]=i['num_of_shares']+spam[l]
            else:
              spam[l]=i['num_of_shares']
    


    print(spam)
    list7=spam.keys()
    list8=spam.values()

    import matplotlib.pyplot as plt
    plt.switch_backend('agg')
    plt.bar(list7,list8, color=['firebrick', 'green', 'blue', 'black', 'red',])

    plt.xlabel('Categories')
    plt.xticks(rotation=90) 
    plt.ylabel("spam")
    plt.title('Categories Bar Plot')
    plt.show()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

def do_plot5():
    inappropriate_content={}

    for i in d:
        for j,l in b.items():
          if j==i['category']:
            if l in inappropriate_content:
              inappropriate_content[l]=i['inappropriate_content']+inappropriate_content[l]
            else:
              inappropriate_content[l]=i['inappropriate_content']
    


    print(inappropriate_content)

    list9=inappropriate_content.keys()
    list10=inappropriate_content.values()

    import matplotlib.pyplot as plt
    plt.switch_backend('agg')

    plt.bar(list9,list10, color=['firebrick', 'green', 'blue', 'black', 'red',])

    plt.xlabel('Categories')
    plt.xticks(rotation=90) 
    plt.ylabel("inappropriate_content")
    plt.title('Categories Bar Plot')
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


def do_plot6():
  harassment={}
  for i in d:
      for j,l in b.items():
        if j==i['category']:
          if l in harassment:
            harassment[l]=i['harassment']+harassment[l]
          else:
            harassment[l]=i['harassment']
  


  print(harassment)

  list11=harassment.keys()
  list12=harassment.values()

  import matplotlib.pyplot as plt
  plt.switch_backend('agg')
  plt.bar(list11,list12, color=['firebrick', 'green', 'blue', 'black', 'red',])

  plt.xlabel('Categories')
  plt.xticks(rotation=90) 
  plt.ylabel("harassment")
  plt.title('Categories Bar Plot')
  bytes_image = io.BytesIO()
  plt.savefig(bytes_image, format='png')
  bytes_image.seek(0)
  return bytes_image


def do_plot7():
    copyright_issue={}
    for i in d:
        for j,l in b.items():
          if j==i['category']:
            if l in copyright_issue:
              copyright_issue[l]=i['copyright_issue']+copyright_issue[l]
            else:
              copyright_issue[l]=i['copyright_issue']
    


    print(copyright_issue)

    list13=copyright_issue.keys()
    list14=copyright_issue.values()

    import matplotlib.pyplot as plt
    plt.switch_backend('agg')
    plt.bar(list13,list14, color=['firebrick', 'green', 'blue', 'black', 'red',])

    plt.xlabel('Categories')
    plt.xticks(rotation=90) 
    plt.ylabel("copyright_issue")
    plt.title('Categories Bar Plot')
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

def do_plot8():
    other={}
    for i in d:
        for j,l in b.items():
          if j==i['category']:
            if l in other:
              other[l]=i['other']+other[l]
            else:
              other[l]=i['other']
    


    print(other)

    list15=other.keys()
    list16=other.values()

    import matplotlib.pyplot as plt
    plt.switch_backend('agg')

    plt.bar(list15,list16, color=['firebrick', 'green', 'blue', 'black', 'red',])

    plt.xlabel('Categories')
    plt.xticks(rotation=90) 
    plt.ylabel("other")
    plt.title('Categories Bar Plot')
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

def do_plot9():

    reports={}
    for i in d:
        for j,l in b.items():
          if j==i['category']:
            if l in reports:
              reports[l]=i['reports']+reports[l]
            else:
              reports[l]=i['reports']
    


    print(reports)

    list17=reports.keys()
    list18=reports.values()

    import matplotlib.pyplot as plt
    plt.switch_backend('agg')

    plt.bar(list17,list18, color=['firebrick', 'green', 'blue', 'black', 'red',])

    plt.xlabel('Categories')
    plt.xticks(rotation=90) 
    plt.ylabel("reports")
    plt.title('Categories Bar Plot')
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

def do_plot10():

    comments={}
    for i in d:
        for j,l in b.items():
          if j==i['category']:
            if l in comments:
              comments[l]=i['comments']+comments[l]
            else:
              comments[l]=i['comments']
    


    print(comments)

    list19=comments.keys()
    list20=comments.values()

    import matplotlib.pyplot as plt

    plt.bar(list19,list20, color=['firebrick', 'green', 'blue', 'black', 'red',])

    plt.xlabel('Categories')
    plt.xticks(rotation=90) 
    plt.ylabel("comments")
    plt.title('Categories Bar Plot')
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

def do_plot11():

    trending={}
    for i in d:
        for j,l in b.items():
          if j==i['category']:
            if l in trending:
              trending[l]=i['trending score']+trending[l]
            else:
              trending[l]=i['trending score']
    


    print(trending)
    list21=trending.keys()
    list22=trending.values()

    import matplotlib.pyplot as plt

    plt.bar(list21,list22, color=['firebrick', 'green', 'blue', 'black', 'red',])

    plt.xlabel('Categories')
    plt.xticks(rotation=90) 
    plt.ylabel("trending")
    plt.title('Categories Bar Plot')
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

#dataframe data

db1=db['posts']
imp1={}
for row in db1.aggregate( [ { "$project": { "likes": 1, '_id':1 } } ] ):
    sum=0
    
    if row['_id'] in imp1.keys():
        for i in row['likes']:
            imp1[row['_id']]=imp1[row['_id']]+len(i)            
else:
    for i in row['likes']:
        sum=sum+len(i)
        imp1[row['_id']]=sum
postid={}
for i in db.posts.find({}):
  postid[i['_id']]={}
  postid[i['_id']]=i['category']
print(postid)
list25=postid.keys()
list26=postid.values()

userid={}
for i in db.posts.find({}):
  userid[i['_id']]={}
  userid[i['_id']]=i['user_id']
print(userid)

hashtags={}
for i in db.posts.find({}):
  hashtags[i['_id']]={}
  hashtags[i['_id']]=i['hashtags']
print(hashtags)

comment={}
for i in db.posts.find({}):
  comment[i['_id']]={}
  comment[i['_id']]=i['comments']
print(comment)

view={}
for i in db.posts.find({}):
  view[i['_id']]={}
  view[i['_id']]=i['num_of_views']
print(view)

share={}
for i in db.posts.find({}):
  share[i['_id']]={}
  share[i['_id']]=i['num_of_shares']
print(share)

spampostid={}
for i in db.posts.find({}):
  spampostid[i['_id']]={}
  spampostid[i['_id']]=i['spam']
print(spampostid)

inappropriate_contentpostid={}
for i in db.posts.find({}):
  inappropriate_contentpostid[i['_id']]={}
  inappropriate_contentpostid[i['_id']]=i['inappropriate_content']
print(inappropriate_contentpostid)

harassmentpostid={}
for i in db.posts.find({}):
  harassmentpostid[i['_id']]={}
  harassmentpostid[i['_id']]=i['harassment']
print(harassmentpostid)

copyright_issuepostid={}
for i in db.posts.find({}):
  copyright_issuepostid[i['_id']]={}
  copyright_issuepostid[i['_id']]=i['copyright_issue']
print(copyright_issuepostid)

reportspostid={}
for i in db.posts.find({}):
  reportspostid[i['_id']]={}
  reportspostid[i['_id']]=i['reports']
print(reportspostid)

import datetime

noofdays={}

for i in db.posts.find({}):
  
  Day=datetime.datetime.now()-i['published_on']

  noofdays[i['_id']]={}
  noofdays[i['_id']]=Day.days
print(noofdays)

data = pd.DataFrame (list25,columns=['postid'])
data['categories']=data['postid'].map(postid)
data['userid']=data['postid'].map(userid)
data['categories2']=data['categories'].map(b)
data['likes']=data['postid'].map(imp1)
data['comments']=data['postid'].map(comment)
data['views']=data['postid'].map(view)
data['shares']=data['postid'].map(share)
data['spam']=data['postid'].map(spampostid)
data['inappropriate_content']=data['postid'].map(inappropriate_contentpostid)
data['harassment']=data['postid'].map(harassmentpostid)
data['copyright_issue']=data['postid'].map(copyright_issuepostid)
data['reports']=data['postid'].map(reportspostid)
data['hashtags']=data['postid'].map(hashtags)
data['noofdays']=data['postid'].map(noofdays)

##############################
import io
import flask
import pandas as pd

app = flask.Flask (__name__)

@app.route("/tab")

def do_plot12(): 


    return render_template('table1.html',data=data.to_html())
################################
exception=data


exception['report_score']=((exception['spam']*2+exception['copyright_issue']*5+ exception['harassment']*4+exception['inappropriate_content']*3
                                                        +exception['reports'])/exception['views'])*100
exception



most_viewed_cat=exception.groupby('categories2').sum()
most_viewed_cat

def do_plot13():


    plt.figure()
    br=sns.barplot(x="categories2",y="views",data=most_viewed_cat.reset_index())
    for i,r in most_viewed_cat.reset_index().iterrows():
        br.text(r.name,r['views'], round(r['views'],2), color='black', ha="center")
    br.set_xlabel("Categories",fontsize=30)
    plt.xticks(rotation=90)
    br.set_ylabel("Views",fontsize=20)
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


mvc=most_viewed_cat.reset_index()
mvc

mvc['trending']=((mvc['likes']*4+mvc['comments']*6+mvc['shares']*10+mvc['views']*2)-(mvc['spam']*2+mvc['copyright_issue']*5+
                                                                                    mvc['harassment']*4+mvc['inappropriate_content']*3
                                                                                    +mvc['reports']))/mvc['noofdays']

mvc.sort_values(by='trending',ascending= False, inplace= True)
df = mvc[['categories2', 'trending']]
df                                                                                    

#applied method
df['percentile'] = pd.qcut(df['trending'], 5, labels=False)
df

def do_plot14():


    # trending category
    plt.figure()
    br=sns.barplot(x="categories2",y="trending",data=mvc)
    for i,r in mvc.iterrows():
        br.text(r.name,r['trending'], round(r['trending'],2), color='black', ha="center")
    br.set_xlabel("Categories",fontsize=30)
    plt.xticks(rotation=90)
    br.set_ylabel("Score",fontsize=20)
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

user_cat=data.groupby('userid').sum()
user_cat

df_user=user_cat.reset_index()
df_user

df_user['trending']=((df_user['likes']*4+df_user['comments']*6+df_user['shares']*10+df_user['views']*2)-(df_user['spam']*2+df_user['copyright_issue']*5+
                                                                                    df_user['harassment']*4+df_user['inappropriate_content']*3
                                                                                    +df_user['reports']))/df_user['noofdays']

df_user.sort_values(by='trending',ascending= False, inplace= True)
df_user      

def do_plot15():        

    plt.figure()
    br=sns.barplot(x="userid",y="trending",data=df_user)
    for i,r in mvc.iterrows():
        br.text(r.name,r['trending'], round(r['trending'],2), color='black', ha="center")
    br.set_xlabel("user ",fontsize=30)
    plt.xticks(rotation=90)
    br.set_ylabel("Score",fontsize=20)
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

u_df = df_user[['userid', 'trending']]
u_df

def do_plot16():
    #pie_chart
    u_df.groupby(['userid']).sum().plot(kind='pie', subplots=True, shadow = True, startangle=90,
    figsize=(15,10), autopct='%1.1f%%')
    #donut chart
    circle = plt.Circle(xy=(0,0),  radius = .75, facecolor='white')
    plt.gca().add_artist(circle)
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

user_posts=data.groupby('userid').sum()

user_posts['report_score']=((user_posts['spam']*2+user_posts['copyright_issue']*5+ user_posts['harassment']*4+user_posts['inappropriate_content']*3
                                                        +user_posts['reports'])/user_posts['views'])*100
user_posts

def do_plot17():
    plt.figure(figsize=(20,10))
    br=sns.barplot(x="userid",y="report_score",data=user_posts.reset_index())
    for i,r in user_posts.reset_index().iterrows():
        br.text(r.name,r['report_score'], round(r['report_score'],2), color='black', ha="center",fontsize=15)
    br.set_xlabel("user",fontsize=30)
    plt.xticks(rotation=90)
    br.set_ylabel("Report_score",fontsize=30)
    br.tick_params(labelsize=20)
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

import io
def pymongo3(d):
    z=list(db.posts.find({}))
    l={}
    for i in z:
        l[i["author_name"]]=i[d]
        
    s=[]
    p=[]
    for j,k in l.items():
        p.append(k)
    return(p)
        

z=(pymongo3("author_name"))
x=(pymongo3("num_of_views"))

d1=pymongo3("num_of_shares")
e1=pymongo3("comments")
f1=pymongo3("spam")
g1=pymongo3("inappropriate_content")

df3=pd.DataFrame()
df3["Name"]=z
df3["number_of_views"]=x
df3["number_of_shares"]=d1
df3["comments"]=e1
df3["spam"]=f1
df3["inappropiate_content"]=g1
df3

####not finished

def do_plot18():
  for i in range(len(df3["Name"])):
      s=["views","comments"]
      d=[df3["number_of_views"][i]+10,df3["comments"][i]+10]
      colors = ["red","blue"]
      plt.pie(d, labels=s,explode = [0.1,0.1] ,colors=colors,autopct='%1.1f%%', shadow=True)
      plt.title(df3["Name"][i])
      bytes_image = io.BytesIO()
      plt.savefig(bytes_image, format='png')
      bytes_image.seek(0)     
      return bytes_image

    
def pymongo4(d):
    z=list(db.posts.find({}))
    l={}
    for i in z:
        l[i["author_name"]]=i[d]
        
    s=[]
    p=[]
    for j,k in l.items():
        p.append(len(k))
    return(p)

t=pymongo4("likes")
df3["likes"]=t
m=pymongo3("copyright_issue")
df3["copyright"]=m

def do_plot19():
  ax2 = sns.barplot(df3["Name"],df3["likes"])
  ax2.set_xticklabels(ax2.get_xticklabels(),rotation = 90)
  bytes_image = io.BytesIO()
  plt.savefig(bytes_image, format='png')
  bytes_image.seek(0)     
  return bytes_image

def do_plot20():
  s=["likes","comments"]
  d=[df3["likes"].sum(),df3["comments"].sum()]
  colors = ["aqua","red"]
  plt.pie(d,labels=s,colors=colors,explode=[0.1,0.1],shadow=True)
  bytes_image = io.BytesIO()
  plt.savefig(bytes_image, format='png')
  bytes_image.seek(0)     
  return bytes_image

def pymong2(d):
    
    

    s=[]
    u=[]
    
    for i in list(db.categories.find({})):
        s.append(i["_id"])
        u.append(i["name"])
    r={}
    

    for j in list((db.posts.find({}))):
        r[j["category"]]=j["hashtags"]
        
        
        
        
    p=[]



    for l in (s):
        z=[]
        for a,b in r.items():
            if a==l:
                z.append((r.get(a)))
            
        p.append(z)
        
    return(p)


p=(pymong2("h"))
s=[]
for i in p:
    for k in i:
        for l in k:
            s.append(l)
            
t=list(set(s))
print(t)
o=[]
for u in t:
    o.append(s.count(u))
    
def do_plot21():
  ax2 = sns.barplot(t,o)
  ax2.set_xticklabels(ax2.get_xticklabels(),rotation = 90)
  bytes_image = io.BytesIO()
  plt.savefig(bytes_image, format='png')
  bytes_image.seek(0)     
  return bytes_image

#routes
app=Flask(__name__)

@app.route("/",methods=['GET'])
def home1():
    bytes_obj = do_plot()
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route("/c-likes",methods=['GET'])
def home2():
    bytes_obj = do_plot2()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route("/c-shares",methods=['GET'])
def home3():
    bytes_obj = do_plot3()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route("/c-spam",methods=['GET'])
def home4():
    bytes_obj = do_plot4()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route("/c-inappropriate",methods=['GET'])
def home5():
    bytes_obj = do_plot5()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route("/c-harassment",methods=['GET'])
def home6():
    bytes_obj = do_plot6()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route("/c-copyright",methods=['GET'])
def home7():
    bytes_obj = do_plot7()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route("/c-other",methods=['GET'])
def home8():
    bytes_obj = do_plot8()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route("/c-reports",methods=['GET'])
def home9():
    bytes_obj = do_plot9()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')                    


@app.route("/c-comments",methods=['GET'])
def home10():
    bytes_obj = do_plot10()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')  
                     
@app.route("/c-trending",methods=['GET'])
def home11():
    bytes_obj = do_plot11()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')  

@app.route("/c-views2",methods=['GET'])
def home13():
    bytes_obj = do_plot13()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')  

@app.route("/c-score",methods=['GET'])
def home14():
    bytes_obj = do_plot14()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png') 

@app.route("/u-score",methods=['GET'])
def home15():
    bytes_obj = do_plot15()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')  

@app.route("/u-trending",methods=['GET'])
def home16():
    bytes_obj = do_plot16()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')  

@app.route("/u-reportscore",methods=['GET'])
def home17():
    bytes_obj = do_plot17()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')                       

@app.route("/v-comments",methods=['GET'])
def home18():
    bytes_obj = do_plot18()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')  

@app.route("/n-likes",methods=['GET'])
def home19():
    bytes_obj =do_plot19()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')    

@app.route("/l-comments",methods=['GET'])
def home20():
    bytes_obj =do_plot20()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')                                          

@app.route("/hashtags",methods=['GET'])
def home21():
    bytes_obj =do_plot21()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')  

@app.route("/table1")
def show_tables():
    
    return data.to_html()

@app.route("/table2")
def show_tables2():
    
    return exception.to_html()


@app.route("/table3")
def show_tables3():
    
    return most_viewed_cat.to_html()

@app.route("/table4")
def show_tables4():
    
    return mvc.to_html()

@app.route("/table5")
def show_tables5():
    
    return df.to_html()

@app.route("/table6")
def show_tables6():
    
    return user_cat.to_html()            

@app.route("/table7")
def show_tables7():
    
    return df_user.to_html() 

@app.route("/table8")
def show_tables8():
    
    return u_df.to_html() 

@app.route("/table9")
def show_tables9():
    
    return user_posts.to_html() 

@app.route("/table10")
def show_tables10():
    
    return df3.to_html()         
    
if __name__ == "__main__":
    app.run(debug=True)
