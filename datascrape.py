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

EXCLUDE_LINKS = [
    'http://www.portlandhikersfieldguide.org/wiki/148th_Avenue_Trailhead',
    'http://www.portlandhikersfieldguide.org/wiki/Quartz_Creek_Trailhead',
    'http://www.portlandhikersfieldguide.org/wiki/Jefferson_Park_from_South_Breitenbush_Trailhead',
    'http://www.portlandhikersfieldguide.org/wiki/Latourell_Falls_Trailhead',
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


def get_trailhead_links(section_url):
    soup = make_soup(section_url)
    content = soup.find('div', 'mw-content-ltr')
    hike_links = [BASE_URL + li.a['href'] for li in content.findAll('li')]
    trailhead_links = []
    for hike in hike_links:
        if hike.endswith('Trailhead') and hike not in EXCLUDE_LINKS:
            trailhead_links.append(hike)
    return trailhead_links


def get_trailhead_details(section_url):
    soup = make_soup(section_url)
    content = soup.find('div', 'mw-content-ltr')
    trailhead_name = soup.find('h1').string
    hikes_here = soup.find('span', 'mw-headline')
    hikes_here = hikes_here.findNext('ul')
    hike_links = [BASE_URL + li.a['href'] for li in hikes_here.findAll('li')]
    lat_long = [li.string for li in content.findAll('li', limit=2)]
    good_hike_links = []
    for hike in hike_links:
        if hike.find('.php') == -1 and hike.find('usda') == -1:
            good_hike_links.append(hike)
    return trailhead_name, lat_long, good_hike_links


def get_hike_details(section_url):
    soup = make_soup(section_url)
    hike_name = soup.find('h1').string
    hikes_here = hike_name.findNext('ul').findNext('ul')
    hike_details = [li.string for li in hikes_here.findAll('li')]
    return hike_name, hike_details


def write_to_file(filename, dict):
    f = open(filename, 'w')
    for key, value in dict.items():
        try:
            print(key)
            f.write("\n{}\t{}".format(key, value))
        except:
            f.write("\nunicode error")
    f.close()


# initialize dictionary variables to links for next stage
trailhead_links_dict = {}
hike_links_dict = {}

# initialize dictionary variables to hold date for each section to send to file
region_count_dict = {}
trailheads_dict = {}
hike_details_dict = {}

# compile all the links for regional sub pages
region_dict = create_regions_dict()

# follow all region sub page links to gather links to trailheads and get count of trailheads per region
for key, value in region_dict.items():
    trailhead_links = []
    for link in value:
        links = get_trailhead_links(link)
        trailhead_links += links
        trailhead_links_dict[key] = trailhead_links
    region_count_dict[key] = len(trailhead_links)

# follow all trailhead links by region to get hike links and trailhead details (lat/long, count of hikes)
for key, value in trailhead_links_dict.items():
    for link in value:
        if link not in EXCLUDE_LINKS:
            print(link)
            name, coords, hikes = get_trailhead_details(link)
            hike_links_dict[name] = hikes
            trailheads_dict[name] = (key, coords, len(hikes))

# follow all hike links by trailhead to get details for each hike
for key, value in hike_links_dict.items():
    for link in value:
        if link not in EXCLUDE_LINKS:
            print(key, link)
            name, details = get_hike_details(link)
            hike_details_dict[name] = (key, details)

write_to_file('hikedetails', hike_details_dict)
write_to_file('trailheads', trailheads_dict)

# print(get_hike_details('http://www.portlandhikersfieldguide.org/wiki/North_and_McKenzie_Heads_Hike'))