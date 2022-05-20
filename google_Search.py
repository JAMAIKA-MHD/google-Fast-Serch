import requests,bs4,webbrowser,sys


# set parameters and parse the query from command line
params = {
  'q': ' '.join(sys.argv[2:]),
  'gl': 'us',
  'hl': 'en',
}
# set request's headers  
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
}

# get length and list of arguments
args_len = len(sys.argv)
args_list = sys.argv

# check if the option is correctly set
def check_args(opt):
    if opt != '-l':
        print("Please Run With '-l' Option ")
        return False
    else : 
        return True

# request sender --- returns response object
def Page_Retrv(params,headers):
    req = requests.get('https://www.google.com/search?q=',headers=headers,params=params)
    return req

# get the web site name for more clear print on terminal 
def Get_web_sites(bs4_obj):
    web_sites = []
    for i in bs4_obj.find_all('div', class_='BNeawe UPmit AP7Wnd'):
        web_sites.append((i.text.split(' ')[0]+'\n'))
    return web_sites

# get the search results links 
def Get_urls(bs4_obj):
    urls = []
    for i in bs4_obj.find_all('div', class_='egMi0 kCrYT'):
        urls.append((i.a.attrs.get('href').split("url=")[1].split("&")[0]+'\n'))
    return urls

# open Links In New Tab if possible on default browser
def open_url(web_site,url):
    webbrowser.open_new_tab(url)
    return "Openning Site : %s with URl : %s \n"%(web_site,url)

# arguments error handeling
if args_len < 3:
    print(''*10+"\nWelcom To google fast searcher\n")
    exit("Usage : google_search.py -l [google search string]")

else : 
    if check_args(args_list[1]) == True:
        
        htmlPage = bs4.BeautifulSoup(Page_Retrv(params,headers).text,'html.parser')
        urls = Get_urls(htmlPage)
        web_sites = Get_web_sites(htmlPage)
        for w_site,link in zip(web_sites,urls) : 
            print(open_url(w_site,link))
    else: 
        exit()


