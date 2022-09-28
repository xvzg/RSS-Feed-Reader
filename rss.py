import feedparser
import random

# Python-based RSS Reader and Downloader v1.1

rssfeed_1 = "https://yourfeed/index.xml"
feed_caller = feedparser.parse(rssfeed_1)

"""
get_list_of_articles():
"""
def rssOverview():
    article_list = []
    if rssfeed_1 != "":
        print(f'Fetching first RSS feed from {rssfeed_1}\n')
        for a in feed_caller.entries:
            title = a['title']
            published_date = a.published
            url = a.link
            article = {
                'title': title,
                # use strftime here
                'date': published_date,
                'url': url,
                }
            article_list.append(article)
    else:
      print("Error loading RSS feed.")
      
    return article_list


# rssParse() being worked on in future versions

def pick_random_number(count):
    pick = random.randint(0, count)
    return pick

def random_article(count):
    index = 0
    for i, v in enumerate(rssOverview(), start=count):
        if index == 1:
            break
        else:
            print(i, v)
            index += 1


# saveRss() being worked on in future versions

if __name__ == "__main__":
    article_list = rssOverview()
    total_count = len(article_list)
    random_count = pick_random_number(total_count)
    random_article(random_count)
