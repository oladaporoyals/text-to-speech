import re
import requests
def get_page_content(url):
    r = requests.get(url)
    html_text = r.text
    html_text = re.sub("\s+"," ", html_text)
    return html_text

def extract_product _links(content:)
    product_url_regex = re.complier(r'<article class="project_pod">.*?<h3>.*?<a href=)"(.*?)"')
    result = re.findall(product_url_regex, content)
links = ["http://books.toscrape.com/" + x for x in result]
    return links


def get_product_links():
    url  "http://books.toscrape.com/catalogue/page-{}.html".format(page)
    print(url)


if __name__ == "__main__":
    #url = "http://books.toscrape.com/index.html")
    #content = get_page_content(url)
    #links = extract_product_links(content)
    #print(links)


    get_all_product_links()

#to be revisited has some errors 
