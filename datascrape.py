from bs4 import BeautifulSoup
from urllib2 import urlopen
from lxml import html
import requests

BASE_URL = "http://www.portlandhikersfieldguide.org"
REGIONS = ['Gorge', 'Mount Hood', 'Central OR', 'OR Coast', 'East OR', 'South OR', 'Portland', 'SW WA', 'WA Coast']
REGION_INDEXS = [
    'http://www.portlandhikersfieldguide.org/wiki/Category:Columbia_River_Gorge',
    'http://www.portlandhikersfieldguide.org/wiki/Category:Mount_Hood_Area',
    'http://www.portlandhikersfieldguide.org/wiki/Category:Central_Oregon',
    'http://www.portlandhikersfieldguide.org/wiki/Category:Oregon_Coast',
    'http://www.portlandhikersfieldguide.org/wiki/Category:Eastern_Oregon',
    'http://www.portlandhikersfieldguide.org/wiki/Category:Southern_Oregon',
    'http://www.portlandhikersfieldguide.org/wiki/Category:Portland',
    'http://www.portlandhikersfieldguide.org/wiki/Category:Southwest_Washington',
    'http://www.portlandhikersfieldguide.org/wiki/Category:Washington_Coast'
]


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


def get_region_pages(region_url_list):
    soup = make_soup(region_url_list[-1])
    pages = soup.find('div', id='mw-pages')
    region_links = [BASE_URL + a['href'] for a in pages.findAll('a', limit=2)]
    for link in region_links:
        if not link.find('pagefrom') == -1:
            region_url_list.append(link)
            get_region_pages(region_url_list)

    return region_url_list


def create_regions_dict():
    region_dict = {}
    for i in range(0, len(REGIONS)):
        region_list = get_region_pages([REGION_INDEXS[i]])
        region_dict[REGIONS[i]] = region_list
    return region_dict


def get_hike_links(section_url):
    soup = make_soup(section_url)
    content = soup.find('div', 'mw-content-ltr')
    hike_links = [BASE_URL + li.a['href'] for li in content.findAll('li')]
    hike_names = [li.string for li in content.findAll('li')]
    trailhead_links = []
    trailhead_names = []
    for hike in hike_links:
        if hike.endswith('Trailhead'):
            trailhead_links.append(hike)

    for name in hike_names:
        if name.endswith('Trailhead'):
            trailhead_names.append(name)
    return trailhead_links, trailhead_names

def get_trailhead_details(section_url):
    soup = make_soup(section_url)
    content = soup.find('div', 'mw-content-ltr')
    hike_links = [BASE_URL + li.a['href'] for li in content.findAll('li')]
    hike_names = [li.string for li in content.findAll('li')]


region_dict = create_regions_dict()
trailhead_links_dict = {}
trailhead_names_dict = {}
for key, value in region_dict.items():
    trailhead_links = []
    trailhead_names = []
    for link in value:
        links, names = get_hike_links(link)
        trailhead_links += links
        trailhead_names += names
    trailhead_links_dict[key] = trailhead_links
    trailhead_names_dict[key] = trailhead_names

for key, value in trailhead_links_dict.items():
    print("{} - {}".format(key, value))

for key, value in trailhead_names_dict.items():
    print("\n{}\t{}".format(key, value))

