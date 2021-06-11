import Opener
import Dataset as d
import connection as Project
from bs4 import BeautifulSoup
import GetName as In
def DawnNews():
    # driver.get("https://www.dawn.com")
    # Html = driver.page_source

    OpenUrl =Opener.myUrlOpener()
    response =OpenUrl.open("https://www.dawn.com")
    soup = BeautifulSoup(response,'html.parser')
    top_stories = soup.find('div',{"class":"mb-4 pr-0 sm:pr-2 sm:border-r sm:border-r-solid sm:border-r-grey-lighter"})
    articles = top_stories.find_all('article')
    print(len(articles))
    # driver.quit()
    for article in articles:
        article_link = article.h2.a.get('href')
        article_heading = article.h2.a.text
        article_img_src = article.figure.img.get('src')
        article_div_text = article.find('div',{'class':'story__excerpt'})
        article_div_description = article_div_text.text
        print(article_heading)
        print(article_link)
        Page = Opener.UrlToOpen(article_link)
        soup1 = BeautifulSoup(Page,'html.parser')
        div = soup1.find('div',{"class":"story__content"})
        all_paras = div.find_all('p')
        text = ''
        for para in all_paras:
            text += para.text
        print(text)
        print(article_img_src)
        article_img_name = In.AddUrl_and_Get_Name(article_img_src)
        print(article_div_text.text)
        d.data_set(text,"Dawn")
        #Project.News(article_heading,text,article_link,article_img_name,"DAWN")