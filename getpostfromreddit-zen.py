import praw
import requests
from io import BytesIO
from PIL import Image
reddit = praw.Reddit(client_id='PTELqQeemTWiZ-L61Q3REA', client_secret='M8hcW0t8L8W8y-zSnhaOr7ZYhUH_fg', user_agent='MemeBot')
hot_posts = reddit.subreddit('css_irl+ProgrammerHumor+programming+programming_memes+programmingmemes+programminghorror').hot()

for post in hot_posts:
    if(post.post_hint == 'image'):
        memeurl = post.url
        print('meme available')
        break

# for post in hot_posts:
#     print(post.url + " " + post.post_hint)

print(memeurl)
memebg = Image.open('memebgzen.jpg')
# memecontent = Image.open('test.jpg')
memecontent = Image.open(BytesIO(requests.get(memeurl).content))
print(memecontent.size)
memecontent.save('meme.jpg')

width, height = memecontent.size

if(width>=height):
    scaleratio = 968/width
    newwidth = round(scaleratio*width)
    newheight = round(scaleratio*height)    
    memecontent = memecontent.resize((newwidth,newheight))
    memebg.paste(memecontent,(56,round(508-(newheight/2))))
else:
    scaleratio = 824/height
    newheight = round(scaleratio*height)
    newwidth = round(scaleratio*width)
    if(newwidth>904):
        scaleratio = (968/width)
        newwidth = round(scaleratio*width)
        newheight = round(scaleratio*height)
    memecontent = memecontent.resize((newwidth,newheight))
    memebg.paste(memecontent,(round(540-(newwidth/2)),round(508-(newheight/2))))

memebg.save('final.jpg')