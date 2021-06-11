import Opener
import connection as Project
import GetName as In
from bs4 import BeautifulSoup
def AryNews():
    OpenUrl = Opener.myUrlOpener()
    urls = ["https://arynews.tv/en/category/pakistan/",
            "https://arynews.tv/en/category/pakistan/page/2/",
            "https://arynews.tv/en/category/pakistan/page/3/",
            "https://arynews.tv/en/category/pakistan/page/4/",
            "https://arynews.tv/en/category/pakistan/page/5/",
            "https://arynews.tv/en/category/pakistan/page/6/",
            "https://arynews.tv/en/category/pakistan/page/7/",
            "https://arynews.tv/en/category/pakistan/page/8/",
            "https://arynews.tv/en/category/pakistan/page/9/",
            "https://arynews.tv/en/category/pakistan/page/10/",
            "https://arynews.tv/en/category/pakistan/page/11/",
            "https://arynews.tv/en/category/pakistan/page/12/",
            "https://arynews.tv/en/category/pakistan/page/13/",
            "https://arynews.tv/en/category/pakistan/page/14/",
            "https://arynews.tv/en/category/pakistan/page/15/",
            "https://arynews.tv/en/category/pakistan/page/16/",
            "https://arynews.tv/en/category/pakistan/page/17/",
            "https://arynews.tv/en/category/pakistan/page/18/",
            "https://arynews.tv/en/category/pakistan/page/19/",
            "https://arynews.tv/en/category/pakistan/page/20/",
            "https://arynews.tv/en/category/pakistan/page/21/",
            "https://arynews.tv/en/category/pakistan/page/22/",
            "https://arynews.tv/en/category/pakistan/page/23/",
            "https://arynews.tv/en/category/pakistan/page/24/",
            "https://arynews.tv/en/category/pakistan/page/25/",
            "https://arynews.tv/en/category/pakistan/page/26/",
            "https://arynews.tv/en/category/pakistan/page/27/",
            "https://arynews.tv/en/category/pakistan/page/28/",
            "https://arynews.tv/en/category/pakistan/page/29/",
            "https://arynews.tv/en/category/pakistan/page/30/"]
    for url in urls:
        HtmlPage =OpenUrl.open(url)
    # driver.get("https://arynews.tv/en/")
    # Html = driver.page_source
        soup = BeautifulSoup(HtmlPage,'html.parser')
        print('------------------------------------------------------------------------------')
        section_tag = soup.find('div',{"class":"listing listing-blog listing-blog-1 clearfix columns-1"})
        article_tag = section_tag.find_all('article')
        for index in range(0,10):
            article_link = article_tag[index].h2.a.get('href')
            response = OpenUrl.open(article_link)
            soup1 = BeautifulSoup(response,'html.parser')
            next_link_div = soup1.find('div',{"class":"post-header post-tp-1-header"})
            next_link_div_img_src = next_link_div.img.get('data-src')
            if next_link_div_img_src is not None:
                next_link_div_h1 = next_link_div.h1.text
                description_div = soup1.find('div',{"class":"entry-content clearfix single-post-content"})
                description_text = description_div.p.text
                img_name = In.AddUrl_and_Get_Name(next_link_div_img_src)
                Page = Opener.UrlToOpen(article_link)
                soup = BeautifulSoup(Page, 'html.parser')
                div_of_Page = soup.find('div',{"class":"entry-content clearfix single-post-content"})
                all_Paras = div_of_Page.find_all('p')
                str1 = ''
                print(len(all_Paras))
                for para in range(0,len(all_Paras)-1):
                    str1 += all_Paras[para].text
                #print(div_of_Page)
                print(next_link_div_h1)
                print(next_link_div_img_src)
                print(str1)
                #Project.News(next_link_div_h1,str1,article_link,img_name,"ARY")
AryNews()