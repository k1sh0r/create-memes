import base64
import praw
import requests
import send_files
from io import BytesIO
from io import StringIO 
from PIL import Image
from flask import redirect, render_template, request, send_file, session, url_for

def downloadMeme(category, count = 1):
    reddit = praw.Reddit(client_id='PTELqQeemTWiZ-L61Q3REA', client_secret='M8hcW0t8L8W8y-zSnhaOr7ZYhUH_fg', user_agent='MemeBot')
    if category == "hot":
        hot_posts = reddit.subreddit('css_irl+ProgrammerHumor+programming+programming_memes+programmingmemes+programminghorror').hot()
    elif category == "new":
        hot_posts = reddit.subreddit('css_irl+ProgrammerHumor+programming+programming_memes+programmingmemes+programminghorror').new()

    for post in hot_posts:
        try:
            if(post.post_hint and post.post_hint == 'image'):
                count = count -1
                if count <= 1:
                    memeurl = post.url
                    print('meme available')
                    break
        except:
            print("this post had a error")

    # for post in hot_posts:
    #     print(post.url + " " + post.post_hint)

    print(memeurl)
    memebg = Image.open('memebg.jpg')
    memecontent = Image.open(BytesIO(requests.get(memeurl).content))
    print(memecontent.size)

    width, height = memecontent.size

    if(width>=height):
        scaleratio = 904/width
        newwidth = round(scaleratio*width)
        newheight = round(scaleratio*height)    
        memecontent = memecontent.resize((newwidth,newheight))
        memebg.paste(memecontent,(88,round(674-(newheight/2))))
    else:
        scaleratio = 1080/height
        newheight = round(scaleratio*height)
        newwidth = round(scaleratio*width)
        if(newwidth>904):
            scaleratio = 904/width
            newwidth = round(scaleratio*width)
            newheight = round(scaleratio*height)
        memecontent = memecontent.resize((newwidth,newheight))
        memebg.paste(memecontent,(round(540-(newwidth/2)),round(674-(newheight/2))))

    # memebg.save('final.jpg')
    img_io = BytesIO()
    memebg.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')
    # return memebg

def downloadZenMeme(category, count = 1):
    reddit = praw.Reddit(client_id='PTELqQeemTWiZ-L61Q3REA', client_secret='M8hcW0t8L8W8y-zSnhaOr7ZYhUH_fg', user_agent='MemeBot')
    if category == "hot":
        hot_posts = reddit.subreddit('css_irl+ProgrammerHumor+programming+programming_memes+programmingmemes+programminghorror').hot()
    elif category == "new":
        hot_posts = reddit.subreddit('css_irl+ProgrammerHumor+programming+programming_memes+programmingmemes+programminghorror').new()

    for post in hot_posts:
        try:
            if(post.post_hint == 'image'):
                count = count -1
                if count <= 1:
                    memeurl = post.url
                    print('meme available')
                    break
        except:
            print("error in zen post")

    # for post in hot_posts:
    #     print(post.url + " " + post.post_hint)

    print(memeurl)
    memebg = Image.open('memebgzen.jpg')
    memecontent = Image.open(BytesIO(requests.get(memeurl).content))
    print(memecontent.size)

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

    # memebg.save('final.jpg')
    img_io = BytesIO()
    memebg.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    print( base64.b64encode(img_io.getvalue()).decode())
    return send_file(img_io, mimetype='image/jpeg')

    # return send_file('<img src="data:image/png;base64",' + base64.b64encode(img_io.getvalue()).decode() + '"/> <a href="/"><form action="/"><input class="btn" type="button" value="HOME" /></form></a>')
    # return memebg