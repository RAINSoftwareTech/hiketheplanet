import os
import django


def populate():
    or_coast_region = add_region('Oregon Coast')
    wa_coast_region = add_region('Washington Coast & Olympics')
    sw_wa_region = add_region('Southwest Washington')
    gorge_region = add_region('Columbia Gorge')
    portland_region = add_region('Portland & Valley')
    mthood_region = add_region('Mount Hood')
    cent_or_region = add_region('Central Oregon')
    east_or_region = add_region('Eastern Oregon')
    south_or_region = add_region('Southern Oregon')

    add_trailhead(trailhead='Natural Arch Trailhead',
                  region=cent_or_region,
                  latitude=44.76794, longitude=-122.27606)
    add_trailhead(trailhead='Crane Prairie Trailhead',
                  region=mthood_region,
                  latitude=45.27600, longitude=-121.59308)
    add_trailhead(trailhead='Indian Henry Trailhead',
                  region=mthood_region,
                  latitude=45.10882, longitude=-122.07544)
    add_trailhead(trailhead='Yaquina Head Light Trailhead',
                  region=or_coast_region,
                  latitude=44.67634, longitude=-124.07768)
    add_trailhead(trailhead='Wamic Road Trailhead',
                  region=mthood_region,
                  latitude=45.24462, longitude=-121.61104)
    add_trailhead(trailhead='Hummocks Trailhead',
                  region=sw_wa_region,
                  latitude=46.28179, longitude=-122.26305)
    add_trailhead(trailhead='Olallie Lake Trailhead',
                  region=cent_or_region,
                  latitude=44.8141, longitude=-121.7949)
    add_trailhead(trailhead='Three Corner Rock Trailhead',
                  region=sw_wa_region,
                  latitude=45.73587, longitude=-122.03197)
    add_trailhead(trailhead='Bottle Prairie Trailhead',
                  region=mthood_region,
                  latitude=45.395204, longitude=-121.499669)
    add_trailhead(trailhead='Dog River Trailhead',
                  region=mthood_region,
                  latitude=45.46447, longitude=-121.56557)
    add_trailhead(trailhead='Meadowbrook Marsh Trailhead',
                  region=sw_wa_region,
                  latitude=45.63625, longitude=-122.58037)
    add_trailhead(trailhead='Wildwood Trailhead',
                  region=portland_region,
                  latitude=45.51275, longitude=-122.71661)
    add_trailhead(trailhead='Firelane 15 Gate Trailhead',
                  region=portland_region,
                  latitude=45.59581, longitude=-122.82419)
    add_trailhead(trailhead='Cape Horn North Trailhead',
                  region=gorge_region,
                  latitude=45.59656, longitude=-122.18003)
    add_trailhead(trailhead='Rialto Beach Trailhead',
                  region=wa_coast_region,
                  latitude=47.9213, longitude=-124.6384)
    add_trailhead(trailhead='Lucia Falls Trailhead',
                  region=sw_wa_region,
                  latitude=45.84044, longitude=-122.44626)
    add_trailhead(trailhead='Steamboat Landing Trailhead',
                  region=sw_wa_region,
                  latitude=45.57617, longitude=-122.35556)
    add_trailhead(trailhead='Arcadia Beach Trailhead',
                  region=or_coast_region,
                  latitude=45.84634, longitude=-123.96020)
    add_trailhead(trailhead='Neskowin Beach Trailhead',
                  region=or_coast_region,
                  latitude=45.10326, longitude=-123.98202)
    add_trailhead(trailhead='Ozette Trailhead',
                  region=wa_coast_region,
                  latitude=48.154372, longitude=-124.6692)
    add_trailhead(trailhead='Devil\'s Punchbowl Trailhead',
                  region=or_coast_region,
                  latitude=44.74686, longitude=-124.06530)
    add_trailhead(trailhead='Harms Road Trailhead',
                  region=sw_wa_region,
                  latitude=45.72351, longitude=-121.03091)
    add_trailhead(trailhead='Wildwood Recreation Area Trailhead',
                  region=mthood_region,
                  latitude=45.3501, longitude=-121.9924)
    add_trailhead(trailhead='Sherwood Trailhead',
                  region=mthood_region,
                  latitude=45.40098, longitude=-121.57063)
    add_trailhead(trailhead='Mazama Trailhead',
                  region=mthood_region,
                  latitude=45.437125, longitude=-121.757221)
    add_trailhead(trailhead='Gumjuwac Trailhead',
                  region=mthood_region,
                  latitude=45.33950, longitude=-121.57020)
    add_trailhead(trailhead='Breakers Trailhead',
                  region=wa_coast_region,
                  latitude=46.37093, longitude=-124.05541)
    add_trailhead(trailhead='Mirror Lake Trailhead',
                  region=mthood_region,
                  latitude=45.30623, longitude=-121.79188)
    add_trailhead(trailhead='Leaf Hill Trailhead',
                  region=east_or_region,
                  latitude=44.65211, longitude=-120.28017)
    add_trailhead(trailhead='Top Spur Trailhead',
                  region=mthood_region,
                  latitude=45.4074, longitude=-121.7856)
    add_trailhead(trailhead='Bonney Butte Trailhead',
                  region=mthood_region,
                  latitude=45.26706, longitude=-121.58939)
    add_trailhead(trailhead='Tolinda Trailhead',
                  region=portland_region,
                  latitude=45.58832, longitude=-122.77881)
    add_trailhead(trailhead='Indian Cemetery Road Trailhead',
                  region=sw_wa_region,
                  latitude=45.8029, longitude=-121.4694)
    add_trailhead(trailhead='Upper Siouxon Trailhead',
                  region=sw_wa_region,
                  latitude=45.9305, longitude=-122.0655)
    add_trailhead(trailhead='Williams Mine Trailhead',
                  region=sw_wa_region,
                  latitude=46.1694, longitude=-121.626)
    add_trailhead(trailhead='Camas Heritage Park Trailhead',
                  region=sw_wa_region,
                  latitude=45.60490, longitude=-122.41157)
    add_trailhead(trailhead='Fisher Hill Bridge Trailhead',
                  region=sw_wa_region,
                  latitude=45.71179, longitude=-121.26657)
    add_trailhead(trailhead='Harvey Road Trailhead',
                  region=mthood_region,
                  latitude=45.30149, longitude=-122.14664)
    add_trailhead(trailhead='Bonanza Trailhead',
                  region=mthood_region,
                  latitude=45.3182, longitude=-121.9539)
    add_trailhead(trailhead='Crabtree Valley Trailhead',
                  region=cent_or_region,
                  latitude=44.603, longitude=-122.446)
    add_trailhead(trailhead='Mark Hatfield West Trailhead',
                  region=gorge_region,
                  latitude=45.70376, longitude=-121.48678)
    add_trailhead(trailhead='Sleeping Beauty Trailhead',
                  region=sw_wa_region,
                  latitude=46.0850, longitude=-121.6583)
    add_trailhead(trailhead='Timberline Lodge Trailhead',
                  region=mthood_region,
                  latitude=45.3308, longitude=-121.7113)
    add_trailhead(trailhead='Barlow Pass Trailhead',
                  region=mthood_region,
                  latitude=45.28192, longitude=-121.68453)
    add_trailhead(trailhead='Hart\'s Cove Trailhead',
                  region=or_coast_region,
                  latitude=45.06491, longitude=-123.99545)
    add_trailhead(trailhead='Columbia Springs Trailhead',
                  region=sw_wa_region,
                  latitude=45.59969, longitude=-122.54708)
    add_trailhead(trailhead='Sheppard\'s Dell Trailhead',
                  region=gorge_region,
                  latitude=45.54697, longitude=-122.19760)
    add_trailhead(trailhead='Hadley Trailhead',
                  region=gorge_region,
                  latitude=45.53533, longitude=-122.02317)
    add_trailhead(trailhead='Beards Hollow Trailhead',
                  region=wa_coast_region,
                  latitude=46.30384, longitude=-124.06314)
    add_trailhead(trailhead='Green Canyon Trailhead',
                  region=mthood_region,
                  latitude=45.2830, longitude=-121.9418)
    add_trailhead(trailhead='Washougal River Greenway Trailhead',
                  region=sw_wa_region,
                  latitude=45.58792, longitude=-122.37459)
    add_trailhead(trailhead='Mount Mitchell Trailhead',
                  region=sw_wa_region,
                  latitude=46.04468, longitude=-122.19413)
    add_trailhead(trailhead='Snipes Mountain Trailhead',
                  region=sw_wa_region,
                  latitude=46.09301, longitude=-121.47999)
    add_trailhead(trailhead='Cultus Creek Campground Trailhead',
                  region=sw_wa_region,
                  latitude=46.04756, longitude=-121.75645)
    add_trailhead(trailhead='Dodson Trailhead',
                  region=gorge_region,
                  latitude=45.60023, longitude=-122.04361)
    add_trailhead(trailhead='Nehalem Spit Trailhead',
                  region=or_coast_region,
                  latitude=45.68876, longitude=-123.93690)
    add_trailhead(trailhead='Lyle Cherry Orchard Trailhead',
                  region=gorge_region,
                  latitude=45.68645, longitude=-121.26557)
    add_trailhead(trailhead='Butte Creek Falls Trailhead',
                  region=cent_or_region,
                  latitude=44.92088, longitude=-122.51123)
    add_trailhead(trailhead='Twin Springs Trailhead',
                  region=mthood_region,
                  latitude=45.23159, longitude=-122.00897)
    add_trailhead(trailhead='Alki Road Trailhead',
                  region=sw_wa_region,
                  latitude=45.66079, longitude=-122.67197)
    add_trailhead(trailhead='North Burnt Lake Trailhead',
                  region=mthood_region,
                  latitude=45.3725, longitude=-121.8226)
    add_trailhead(trailhead='Cape Falcon Trailhead',
                  region=or_coast_region,
                  latitude=45.76405, longitude=-123.95435)
    add_trailhead(trailhead='Oneonta Trailhead',
                  region=gorge_region,
                  latitude=45.58849, longitude=-122.07849)
    add_trailhead(trailhead='Yaquina Head Interpretive Center Trailhead',
                  region=or_coast_region,
                  latitude=44.67536, longitude=-124.07417)
    add_trailhead(trailhead='Hurricane Creek Trailhead',
                  region=east_or_region,
                  latitude=45.31118, longitude=-117.30721)
    add_trailhead(trailhead='Leif Erikson Drive North Trailhead',
                  region=portland_region,
                  latitude=45.58910, longitude=-122.79029)
    add_trailhead(trailhead='Image Creek Trailhead',
                  region=mthood_region,
                  latitude=44.97064, longitude=-122.33240)
    add_trailhead(trailhead='McGee Creek Trailhead',
                  region=mthood_region,
                  latitude=45.42014, longitude=-121.77800)
    add_trailhead(trailhead='Germantown Road Trailhead',
                  region=portland_region,
                  latitude=45.58749, longitude=-122.79403)
    add_trailhead(trailhead='Red Rock Pass Trailhead',
                  region=sw_wa_region,
                  latitude=46.14366, longitude=-122.23500)
    add_trailhead(trailhead='Cottonwood Meadows Trailhead',
                  region=mthood_region,
                  latitude=45.1096, longitude=-121.9712)
    add_trailhead(trailhead='Painted Cove Trailhead',
                  region=east_or_region,
                  latitude=44.66069, longitude=-120.27815)
    add_trailhead(trailhead='Icehouse Lake Trailhead',
                  region=sw_wa_region,
                  latitude=45.65974, longitude=-121.90588)
    add_trailhead(trailhead='Cannon Beach Trailhead',
                  region=or_coast_region,
                  latitude=45.89748, longitude=-123.96002)
    add_trailhead(trailhead='Oak Flat Trailhead',
                  region=south_or_region,
                  latitude=42.5191, longitude=-124.04212)
    add_trailhead(trailhead='Sunset Spring Trailhead',
                  region=mthood_region,
                  latitude=45.32380, longitude=-121.47617)
    add_trailhead(trailhead='Elk Lake Junction Trailhead',
                  region=cent_or_region,
                  latitude=44.8252, longitude=-122.1250)
    add_trailhead(trailhead='Bagby Trailhead',
                  region=cent_or_region,
                  latitude=44.8230, longitude=-122.1314)
    add_trailhead(trailhead='Steigerwald Lake Trailhead',
                  region=sw_wa_region,
                  latitude=45.57024, longitude=-122.314586)
    add_trailhead(trailhead='Rattlesnake Falls Trailhead',
                  region=sw_wa_region,
                  latitude=45.88617, longitude=-121.34228)
    add_trailhead(trailhead='Smith and Bybee Trailhead',
                  region=portland_region,
                  latitude=45.61665, longitude=-122.71880)
    add_trailhead(trailhead='BPA Road Trailhead',
                  region=portland_region,
                  latitude=45.61162, longitude=-122.79745)
    add_trailhead(trailhead='Horsetail Falls Trailhead',
                  region=gorge_region,
                  latitude=45.59015, longitude=-122.06807)
    add_trailhead(trailhead='Lewisville Park Entrance Trailhead',
                  region=sw_wa_region,
                  latitude=45.8126, longitude=-122.5469)
    add_trailhead(trailhead='Eagle Creek Trailhead',
                  region=gorge_region,
                  latitude=45.63653, longitude=-121.919470)
    add_trailhead(trailhead='Cape Meares Beach Trailhead',
                  region=or_coast_region,
                  latitude=45.50185, longitude=-123.95927)
    add_trailhead(trailhead='Gumjuwac Saddle Trailhead',
                  region=mthood_region,
                  latitude=45.33335, longitude=-121.54904)
    add_trailhead(trailhead='Rooster Rock Trailhead',
                  region=gorge_region,
                  latitude=45.54783, longitude=-122.26460)
    add_trailhead(trailhead='Old Cascade Head Trailhead',
                  region=or_coast_region,
                  latitude=45.04717, longitude=-123.99497)
    add_trailhead(trailhead='Curly Creek Falls Trailhead',
                  region=sw_wa_region,
                  latitude=46.05989, longitude=-121.97082)
    add_trailhead(trailhead='Tryon Creek State Park Trailhead',
                  region=portland_region,
                  latitude=45.44101, longitude=-122.67480)
    add_trailhead(trailhead='Abiqua Falls Trailhead',
                  region=cent_or_region,
                  latitude=44.93127, longitude=-122.56800)
    add_trailhead(trailhead='Johnston Ridge Observatory Trailhead',
                  region=sw_wa_region,
                  latitude=46.276575, longitude=-122.216704)
    add_trailhead(trailhead='Lost Lake Trailhead',
                  region=mthood_region,
                  latitude=45.49672, longitude=-121.81979)
    add_trailhead(trailhead='South Neahkahnie Mountain Trailhead',
                  region=or_coast_region,
                  latitude=45.74081, longitude=-123.93458)
    add_trailhead(trailhead='Starway Trailhead',
                  region=sw_wa_region,
                  latitude=45.786, longitude=-122.2214)
    add_trailhead(trailhead='Breitenbush Cascades Trailhead',
                  region=cent_or_region,
                  latitude=44.78361, longitude=-121.82917)
    add_trailhead(trailhead='Bird Lake Trailhead',
                  region=sw_wa_region,
                  latitude=46.140489, longitude=-121.440039)
    add_trailhead(trailhead='Paradise Park Trailhead',
                  region=mthood_region,
                  latitude=45.31311, longitude=-121.81602)
    add_trailhead(trailhead='Marquam Nature Park Shelter Trailhead',
                  region=portland_region,
                  latitude=45.50302, longitude=-122.69175)
    add_trailhead(trailhead='Pyramid Lake Road Trailhead',
                  region=mthood_region,
                  latitude=45.1511, longitude=-121.9134)
    add_trailhead(trailhead='South Beach Trailhead',
                  region=or_coast_region,
                  latitude=44.60116, longitude=-124.06495)
    add_trailhead(trailhead='Alder Springs (Whychus Creek) Trailhead',
                  region=east_or_region,
                  latitude=44.4333, longitude=-121.3577)
    add_trailhead(trailhead='Summit Rest Area Trailhead',
                  region=mthood_region,
                  latitude=45.3023, longitude=-121.7448)
    add_trailhead(trailhead='Jack Lake Trailhead',
                  region=cent_or_region,
                  latitude=44.49179, longitude=-121.79447)
    add_trailhead(trailhead='Castle Canyon Trailhead',
                  region=mthood_region,
                  latitude=45.3360, longitude=-121.9142)
    add_trailhead(trailhead='East Crater Trailhead',
                  region=sw_wa_region,
                  latitude=45.98032, longitude=-121.75946)
    add_trailhead(trailhead='Bull of the Woods Trailhead',
                  region=cent_or_region,
                  latitude=44.91881, longitude=-122.10224)
    add_trailhead(trailhead='Rocky Top Trailhead',
                  region=cent_or_region,
                  latitude=44.78741, longitude=-122.28282)
    add_trailhead(trailhead='Wahclella Falls Trailhead',
                  region=gorge_region,
                  latitude=45.63099, longitude=-121.95407)
    add_trailhead(trailhead='Smith Rock Trailhead',
                  region=east_or_region,
                  latitude=44.36267, longitude=-121.13835)
    add_trailhead(trailhead='Elk Cove Trailhead',
                  region=mthood_region,
                  latitude=45.44673, longitude=-121.67765)
    add_trailhead(trailhead='Kalama Ski Trailhead',
                  region=sw_wa_region,
                  latitude=46.14635, longitude=-122.28455)
    add_trailhead(trailhead='Ape Canyon Trailhead',
                  region=sw_wa_region,
                  latitude=46.165341, longitude=-122.092216)
    add_trailhead(trailhead='Shorthorn Trailhead',
                  region=sw_wa_region,
                  latitude=46.13053, longitude=-121.51556)
    add_trailhead(trailhead='Mowich Lake Trailhead',
                  region=sw_wa_region,
                  latitude=46.93318, longitude=-121.86453)
    add_trailhead(trailhead='Rho Ridge Southern Trailhead',
                  region=cent_or_region,
                  latitude=44.8407, longitude=-121.9447)
    add_trailhead(trailhead='Indian Beach Trailhead',
                  region=or_coast_region,
                  latitude=45.93017, longitude=-123.97749)
    add_trailhead(trailhead='Ellis Street Trailhead',
                  region=portland_region,
                  latitude=45.48189, longitude=-122.51442)
    add_trailhead(trailhead='Horsethief Butte Trailhead',
                  region=gorge_region,
                  latitude=45.65075, longitude=-121.09856)
    add_trailhead(trailhead='Lemei Trailhead',
                  region=sw_wa_region,
                  latitude=46.028241, longitude=-121.685815)
    add_trailhead(trailhead='Cache Meadow Trailhead',
                  region=mthood_region,
                  latitude=45.1229, longitude=-122.0176)
    add_trailhead(trailhead='Snowgrass Flats Trailhead',
                  region=sw_wa_region,
                  latitude=46.4636, longitude=-121.5182)
    add_trailhead(trailhead='Lolo Pass Trailhead',
                  region=mthood_region,
                  latitude=45.42692, longitude=-121.79645)
    add_trailhead(trailhead='Pole Creek Trailhead',
                  region=cent_or_region,
                  latitude=44.18756, longitude=-121.70075)
    add_trailhead(trailhead='Crest Camp Trailhead',
                  region=sw_wa_region,
                  latitude=45.90928, longitude=-121.80252)
    add_trailhead(trailhead='Trillium Lake Trailhead',
                  region=mthood_region,
                  latitude=45.2672, longitude=-121.7389)
    add_trailhead(trailhead='Hardy Creek Trailhead',
                  region=mthood_region,
                  latitude=45.03968, longitude=-122.48929)
    add_trailhead(trailhead='Dog Mountain Trailhead',
                  region=sw_wa_region,
                  latitude=45.69927, longitude=-121.70542)
    add_trailhead(trailhead='Post Camp Trailhead',
                  region=mthood_region,
                  latitude=45.28159, longitude=-121.48843)
    add_trailhead(trailhead='Agate Beach Trailhead',
                  region=or_coast_region,
                  latitude=44.65927, longitude=-124.05532)
    add_trailhead(trailhead='Ainsworth Loop Trailhead',
                  region=gorge_region,
                  latitude=45.59232, longitude=-122.0584)
    add_trailhead(trailhead='Wyeth Trailhead',
                  region=gorge_region,
                  latitude=45.687655, longitude=-121.771774)
    add_trailhead(trailhead='Paradise Point Trailhead',
                  region=sw_wa_region,
                  latitude=45.87243, longitude=-122.71004)
    add_trailhead(trailhead='Starvation Creek Trailhead',
                  region=gorge_region,
                  latitude=45.68808, longitude=-122.68997)
    add_trailhead(trailhead='Little North Fork Trailhead',
                  region=cent_or_region,
                  latitude=44.8344, longitude=-122.3499)
    add_trailhead(trailhead='Cast Creek Trailhead',
                  region=mthood_region,
                  latitude=45.38202, longitude=-121.85906)
    add_trailhead(trailhead='Mike Miller Educational Trailhead',
                  region=or_coast_region,
                  latitude=44.60180, longitude=-124.05204)
    add_trailhead(trailhead='La Center Trailhead',
                  region=sw_wa_region,
                  latitude=45.86230, longitude=-122.67010)
    add_trailhead(trailhead='Fir Tree Trailhead',
                  region=mthood_region,
                  latitude=45.24797, longitude=-121.78766)
    add_trailhead(trailhead='Herman Creek Trailhead',
                  region=gorge_region,
                  latitude=45.6817, longitude=-121.84543)
    add_trailhead(trailhead='Coffin Mountain Trailhead',
                  region=cent_or_region,
                  latitude=44.608444, longitude=-122.049706)
    add_trailhead(trailhead='Sawtooth Trailhead',
                  region=sw_wa_region,
                  latitude=46.0922, longitude=-121.7656)
    add_trailhead(trailhead='Mist Falls Trailhead',
                  region=gorge_region,
                  latitude=45.57551, longitude=-122.13286)
    add_trailhead(trailhead='North Twin Pillars Trailhead',
                  region=east_or_region,
                  latitude=44.5143, longitude=-120.5288)
    add_trailhead(trailhead='Hantwick Road Trailhead',
                  region=sw_wa_region,
                  latitude=45.8376, longitude=-122.4344)
    add_trailhead(trailhead='Tooth Rock Trailhead',
                  region=gorge_region,
                  latitude=45.63364, longitude=-121.95004)
    add_trailhead(trailhead='Nestucca Bay Refuge Trailhead',
                  region=or_coast_region,
                  latitude=45.16224, longitude=-123.95126)
    add_trailhead(trailhead='Silver Star Trailhead',
                  region=sw_wa_region,
                  latitude=45.76656, longitude=-122.24174)
    add_trailhead(trailhead='Cold Creek Trailhead',
                  region=sw_wa_region,
                  latitude=45.76118, longitude=-122.34063)
    add_trailhead(trailhead='Oregon Caves Trailhead',
                  region=south_or_region,
                  latitude=42.09961, longitude=-123.41011)
    add_trailhead(trailhead='Big Creek Falls Trailhead',
                  region=sw_wa_region,
                  latitude=46.09276, longitude=-121.90644)
    add_trailhead(trailhead='Blue Lake Trailhead',
                  region=sw_wa_region,
                  latitude=46.16694, longitude=-122.26184)
    add_trailhead(trailhead='Fort Cascades Trailhead',
                  region=gorge_region,
                  latitude=45.64321, longitude=-121.95708)
    add_trailhead(trailhead='Pioneer Bridle Laurel Hill Trailhead',
                  region=mthood_region,
                  latitude=45.31009, longitude=-121.83719)
    add_trailhead(trailhead='Vancouver Quay Trailhead',
                  region=sw_wa_region,
                  latitude=45.62298, longitude=-122.67721)
    add_trailhead(trailhead='Coastal Forest Trailhead',
                  region=wa_coast_region,
                  latitude=46.28433, longitude=-124.05436)
    add_trailhead(trailhead='Moulton Falls Upper Trailhead',
                  region=sw_wa_region,
                  latitude=45.83317, longitude=-122.38374)
    add_trailhead(trailhead='Tam McArthur Rim Trailhead',
                  region=cent_or_region,
                  latitude=44.10078, longitude=-121.62198)
    add_trailhead(trailhead='North Siouxon Trailhead',
                  region=sw_wa_region,
                  latitude=45.97899, longitude=-122.25488)
    add_trailhead(trailhead='Hellroaring Meadows Trailhead',
                  region=sw_wa_region,
                  latitude=46.15688, longitude=-121.41226)
    add_trailhead(trailhead='Frazier Trailhead',
                  region=mthood_region,
                  latitude=45.15012, longitude=-121.96740)
    add_trailhead(trailhead='Kalama Horse Camp Trailhead',
                  region=sw_wa_region,
                  latitude=46.14307, longitude=-122.32381)
    add_trailhead(trailhead='Elk Lake Trailhead',
                  region=cent_or_region,
                  latitude=44.82547, longitude=-122.11530)
    add_trailhead(trailhead='Raymond Street Trailhead',
                  region=portland_region,
                  latitude=45.48648, longitude=-122.51680)
    add_trailhead(trailhead='New McIntyre Trailhead',
                  region=mthood_region,
                  latitude=45.33597, longitude=-122.03565)
    add_trailhead(trailhead='South Burnt Lake Trailhead',
                  region=mthood_region,
                  latitude=45.3232, longitude=-121.8581)
    add_trailhead(trailhead='Sellwood Park Trailhead',
                  region=portland_region,
                  latitude=45.46949, longitude=-122.65931)
    add_trailhead(trailhead='Upper Mount Defiance Trailhead',
                  region=gorge_region,
                  latitude=45.63621, longitude=-121.74248)
    add_trailhead(trailhead='Fogarty Street Trailhead',
                  region=or_coast_region,
                  latitude=44.64589, longitude=-124.04569)
    add_trailhead(trailhead='North Neahkahnie Mountain Trailhead',
                  region=or_coast_region,
                  latitude=45.74824, longitude=-123.96228)
    add_trailhead(trailhead='Woods Park South Trailhead',
                  region=portland_region,
                  latitude=45.45738, longitude=-122.72323)
    add_trailhead(trailhead='South Twin Pillars Trailhead',
                  region=east_or_region,
                  latitude=44.4396, longitude=-120.5807)
    add_trailhead(trailhead='Hoyt Arboretum Trailhead',
                  region=portland_region,
                  latitude=45.51530, longitude=-122.71597)
    add_trailhead(trailhead='High Prairie Trailhead',
                  region=mthood_region,
                  latitude=45.35238, longitude=-121.53120)
    add_trailhead(trailhead='Waikiki Beach Trailhead',
                  region=wa_coast_region,
                  latitude=46.28259, longitude=-124.05878)
    add_trailhead(trailhead='Tierra del Mar Trailhead',
                  region=or_coast_region,
                  latitude=45.24571, longitude=-123.96749)
    add_trailhead(trailhead='Indian Jack Slough Trailhead',
                  region=wa_coast_region,
                  latitude=46.23240, longitude=-123.39961)
    add_trailhead(trailhead='Leverich Park Trailhead',
                  region=sw_wa_region,
                  latitude=45.65069, longitude=-122.65771)
    add_trailhead(trailhead='Badger Creek Upper Trailhead',
                  region=mthood_region,
                  latitude=45.29153, longitude=-121.56805)
    add_trailhead(trailhead='Illinois Southeast Trailhead',
                  region=south_or_region,
                  latitude=42.378, longitude=-123.8047)
    add_trailhead(trailhead='Pinnacle Ridge Trailhead',
                  region=mthood_region,
                  latitude=45.4463, longitude=-121.6847)
    add_trailhead(trailhead='Sandy River Delta Trailhead',
                  region=gorge_region,
                  latitude=45.54496, longitude=-122.37747)
    add_trailhead(trailhead='Oak Ridge Trailhead',
                  region=mthood_region,
                  latitude=45.51997, longitude=-121.5620)
    add_trailhead(trailhead='Tilly Jane Trailhead',
                  region=mthood_region,
                  latitude=45.39939, longitude=-121.6481)
    add_trailhead(trailhead='Olallie Meadows Trailhead',
                  region=cent_or_region,
                  latitude=44.85778, longitude=-121.77327)
    add_trailhead(trailhead='Cape Kiwanda Trailhead',
                  region=or_coast_region,
                  latitude=45.21570, longitude=-123.97049)
    add_trailhead(trailhead='Squaw Mountain Road Trailhead',
                  region=mthood_region,
                  latitude=45.23668, longitude=-122.05917)
    add_trailhead(trailhead='Bob\'s Buck Camp Trailhead',
                  region=mthood_region,
                  latitude=45.1186, longitude=-122.0145)
    add_trailhead(trailhead='St. James Road Trailhead',
                  region=sw_wa_region,
                  latitude=45.66671, longitude=-122.63813)
    add_trailhead(trailhead='Cascade Head Upper Trailhead',
                  region=or_coast_region,
                  latitude=45.06068, longitude=-123.98842)
    add_trailhead(trailhead='Big Bend Trailhead',
                  region=south_or_region,
                  latitude=42.6432, longitude=-124.0493)
    add_trailhead(trailhead='Shingle Mill Trailhead',
                  region=or_coast_region,
                  latitude=45.80317, longitude=-123.95806)
    add_trailhead(trailhead='Coyote Wall Trailhead',
                  region=sw_wa_region,
                  latitude=45.7005, longitude=-121.4024)
    add_trailhead(trailhead='French Creek Ridge Trailhead',
                  region=cent_or_region,
                  latitude=44.782993, longitude=-122.206872)
    add_trailhead(trailhead='Pine Creek Trailhead',
                  region=sw_wa_region,
                  latitude=46.15473, longitude=-122.10282)
    add_trailhead(trailhead='Iron Mountain Trailhead',
                  region=cent_or_region,
                  latitude=44.39852, longitude=-122.15588)
    add_trailhead(trailhead='Lower Smith Creek Trailhead',
                  region=sw_wa_region,
                  latitude=46.18128, longitude=-122.05417)
    add_trailhead(trailhead='Battle Ground Lake Trailhead',
                  region=sw_wa_region,
                  latitude=45.80335, longitude=-122.49279)
    add_trailhead(trailhead='Steins Pillar Trailhead',
                  region=east_or_region,
                  latitude=44.394724, longitude=-120.623580)
    add_trailhead(trailhead='Seaview Trailhead',
                  region=wa_coast_region,
                  latitude=46.33043, longitude=-124.06387)
    add_trailhead(trailhead='Crystal Springs Trailhead',
                  region=portland_region,
                  latitude=45.48013, longitude=-122.63543)
    add_trailhead(trailhead='Mitchell Point Trailhead',
                  region=gorge_region,
                  latitude=45.70312, longitude=-121.61859)
    add_trailhead(trailhead='Lower Metolius Trailhead',
                  region=cent_or_region,
                  latitude=44.6066, longitude=-121.64573)
    add_trailhead(trailhead='Pyramid Lake Trailhead',
                  region=mthood_region,
                  latitude=45.1504, longitude=-121.9273)
    add_trailhead(trailhead='Lacamas Park Trailhead',
                  region=sw_wa_region,
                  latitude=45.60290, longitude=-122.40615)
    add_trailhead(trailhead='Opal Lake Trailhead',
                  region=cent_or_region,
                  latitude=44.78939, longitude=-122.22681)
    add_trailhead(trailhead='Mother Lode Mine Trailhead',
                  region=east_or_region,
                  latitude=44.339342, longitude=-120.358326)
    add_trailhead(trailhead='Trapper Creek Trailhead',
                  region=sw_wa_region,
                  latitude=45.88162, longitude=-121.98018)
    add_trailhead(trailhead='Old Bridge Trailhead',
                  region=mthood_region,
                  latitude=44.96146, longitude=-122.40894)
    add_trailhead(trailhead='Wahtum Lake Trailhead',
                  region=gorge_region,
                  latitude=45.57737, longitude=-121.79263)
    add_trailhead(trailhead='Vivian Lake Trailhead',
                  region=cent_or_region,
                  latitude=43.575790, longitude=-122.192388)
    add_trailhead(trailhead='South Wildcat Trailhead',
                  region=east_or_region,
                  latitude=44.4224, longitude=-120.5453)
    add_trailhead(trailhead='Hellroaring Creek Trailhead',
                  region=sw_wa_region,
                  latitude=46.16121, longitude=-121.40086)
    add_trailhead(trailhead='Pacific Avenue Trailhead',
                  region=or_coast_region,
                  latitude=45.20239, longitude=-123.96697)
    add_trailhead(trailhead='Kiwa Trailhead',
                  region=sw_wa_region,
                  latitude=45.79912, longitude=-122.75613)
    add_trailhead(trailhead='Tombstone Pass Trailhead',
                  region=mthood_region,
                  latitude=44.39911, longitude=-122.13544)
    add_trailhead(trailhead='Salmon River Trailhead',
                  region=mthood_region,
                  latitude=45.27813, longitude=-121.93965)
    add_trailhead(trailhead='Tillamook Head Trailhead',
                  region=or_coast_region,
                  latitude=45.972419, longitude=-123.958397)
    add_trailhead(trailhead='Ramona Falls Trailhead',
                  region=mthood_region,
                  latitude=45.3864, longitude=-121.831)
    add_trailhead(trailhead='Yale and 2nd Trailhead',
                  region=sw_wa_region,
                  latitude=45.58596, longitude=-122.37757)
    add_trailhead(trailhead='Trail of Two Forests Trailhead',
                  region=sw_wa_region,
                  latitude=46.099318, longitude=-122.213287)
    add_trailhead(trailhead='Whetstone Trailhead',
                  region=cent_or_region,
                  latitude=44.87543, longitude=-122.20246)
    add_trailhead(trailhead='Coffenbury Lake Trailhead',
                  region=or_coast_region,
                  latitude=46.17853, longitude=-123.96584)
    add_trailhead(trailhead='Cloud Cap Trailhead',
                  region=mthood_region,
                  latitude=45.4024, longitude=-121.6546)
    add_trailhead(trailhead='Cannery Hill Trailhead',
                  region=or_coast_region,
                  latitude=45.16652, longitude=-123.95305)
    add_trailhead(trailhead='Whitaker Ponds Trailhead',
                  region=portland_region,
                  latitude=45.57391, longitude=-122.61391)
    add_trailhead(trailhead='Berry Patch Trailhead',
                  region=sw_wa_region,
                  latitude=46.46665, longitude=-121.52772)
    add_trailhead(trailhead='Rimrock Trailhead',
                  region=mthood_region,
                  latitude=45.1106, longitude=-122.0223)
    add_trailhead(trailhead='John B Yeon Trailhead',
                  region=gorge_region,
                  latitude=45.6124, longitude=-122.00428)
    add_trailhead(trailhead='Lower Bridge Trailhead',
                  region=cent_or_region,
                  latitude=44.5568, longitude=-121.62)
    add_trailhead(trailhead='Aldrich Butte Trailhead',
                  region=sw_wa_region,
                  latitude=45.64875, longitude=-121.97627)
    add_trailhead(trailhead='Dickey Creek Trailhead',
                  region=cent_or_region,
                  latitude=44.94545, longitude=-122.04845)
    add_trailhead(trailhead='Douglas Cabin Trailhead',
                  region=mthood_region,
                  latitude=45.28917, longitude=-121.42880)
    add_trailhead(trailhead='Bayocean Spit Trailhead',
                  region=or_coast_region,
                  latitude=45.51958, longitude=-123.94758)
    add_trailhead(trailhead='Zigzag Trailhead',
                  region=mthood_region,
                  latitude=45.4103, longitude=-121.5703)
    add_trailhead(trailhead='Military Museum Trailhead',
                  region=or_coast_region,
                  latitude=46.20619, longitude=-123.96542)
    add_trailhead(trailhead='Middle Falls Trailhead',
                  region=sw_wa_region,
                  latitude=46.16622, longitude=-121.86705)
    add_trailhead(trailhead='Oneonta Gorge Trailhead',
                  region=gorge_region,
                  latitude=45.58948, longitude=-122.07531)
    add_trailhead(trailhead='Bonneville Trailhead',
                  region=sw_wa_region,
                  latitude=45.65036, longitude=-121.93281)
    add_trailhead(trailhead='Bolstad Street Trailhead',
                  region=wa_coast_region,
                  latitude=46.35153, longitude=-124.06134)
    add_trailhead(trailhead='Lewis and Clark Park Trailhead',
                  region=gorge_region,
                  latitude=45.54151, longitude=-122.37992)
    add_trailhead(trailhead='Strawberry Trailhead',
                  region=east_or_region,
                  latitude=44.3192, longitude=-118.6747)
    add_trailhead(trailhead='Placid Lake Trailhead',
                  region=sw_wa_region,
                  latitude=46.04876, longitude=-121.80935)
    add_trailhead(trailhead='Baz Riverfront Park Trailhead',
                  region=sw_wa_region,
                  latitude=45.58752, longitude=-122.38787)
    add_trailhead(trailhead='Painted Hills Trailhead',
                  region=east_or_region,
                  latitude=44.65211, longitude=-120.28017)
    add_trailhead(trailhead='Cripple Creek Trailhead',
                  region=mthood_region,
                  latitude=45.1201, longitude=-122.0638)
    add_trailhead(trailhead='Wahkeena Trailhead',
                  region=gorge_region,
                  latitude=45.57528, longitude=-122.12801)
    add_trailhead(trailhead='Willard Springs Trailhead',
                  region=sw_wa_region,
                  latitude=45.9657, longitude=-121.3464)
    add_trailhead(trailhead='Clatsop Spit Trailhead',
                  region=or_coast_region,
                  latitude=46.226373, longitude=-123.99053)
    add_trailhead(trailhead='Linnton Trailhead',
                  region=portland_region,
                  latitude=45.59628, longitude=-122.78428)
    add_trailhead(trailhead='Two Pan Trailhead',
                  region=east_or_region,
                  latitude=45.25, longitude=-117.3764)
    add_trailhead(trailhead='Macks Canyon Trailhead',
                  region=east_or_region,
                  latitude=45.3867, longitude=-120.8732)
    add_trailhead(trailhead='Goat Marsh Lake Trailhead',
                  region=sw_wa_region,
                  latitude=46.15443, longitude=-122.26919)
    add_trailhead(trailhead='Dick Thomas Trailhead',
                  region=sw_wa_region,
                  latitude=45.65488, longitude=-121.96279)
    add_trailhead(trailhead='Gordon Butte Trailhead',
                  region=mthood_region,
                  latitude=45.29817, longitude=-121.42875)
    add_trailhead(trailhead='Johnston Ridge Trailhead',
                  region=sw_wa_region,
                  latitude=46.27612, longitude=-122.21695)
    add_trailhead(trailhead='Rooster Rock Road Trailhead',
                  region=mthood_region,
                  latitude=44.94157, longitude=-122.32399)
    add_trailhead(trailhead='PCT Winter Trailhead',
                  region=gorge_region,
                  latitude=45.66195, longitude=-121.89464)
    add_trailhead(trailhead='Cove Palisades Upper Deschutes Trailhead',
                  region=east_or_region,
                  latitude=44.53124, longitude=-121.29117)
    add_trailhead(trailhead='Conrad Meadows Trailhead',
                  region=sw_wa_region,
                  latitude=46.50873, longitude=-121.28105)
    add_trailhead(trailhead='Lower Lake Trailhead',
                  region=cent_or_region,
                  latitude=44.82328, longitude=-121.79804)
    add_trailhead(trailhead='Netul Landing Trailhead',
                  region=or_coast_region,
                  latitude=46.12681, longitude=-123.87705)
    add_trailhead(trailhead='Fort Clatsop Trailhead',
                  region=or_coast_region,
                  latitude=46.13402, longitude=-123.88054)
    add_trailhead(trailhead='Stacker Butte Trailhead',
                  region=gorge_region,
                  latitude=45.6949, longitude=-121.0926)
    add_trailhead(trailhead='Hood River Meadows Trailhead',
                  region=mthood_region,
                  latitude=45.3231, longitude=-121.63575)
    add_trailhead(trailhead='Pitt Trailhead',
                  region=sw_wa_region,
                  latitude=45.79449, longitude=-121.19787)
    add_trailhead(trailhead='Goodwin Road Trailhead',
                  region=sw_wa_region,
                  latitude=45.63653, longitude=-122.45984)
    add_trailhead(trailhead='Table Rock Trailhead',
                  region=mthood_region,
                  latitude=44.98118, longitude=-122.32154)
    add_trailhead(trailhead='Klickitat Trailhead',
                  region=sw_wa_region,
                  latitude=45.81774, longitude=-121.15193)
    add_trailhead(trailhead='Sanborn Road Trailhead',
                  region=sw_wa_region,
                  latitude=45.7971, longitude=-121.4429)
    add_trailhead(trailhead='Kelley Point South Lot Trailhead',
                  region=portland_region,
                  latitude=45.64358, longitude=-122.76527)
    add_trailhead(trailhead='Wahkiacus Trailhead',
                  region=sw_wa_region,
                  latitude=45.82330, longitude=-121.09857)
    add_trailhead(trailhead='Stagman Ridge Trailhead',
                  region=sw_wa_region,
                  latitude=46.140394, longitude=-121.597788)
    add_trailhead(trailhead='Fall Creek Trailhead',
                  region=cent_or_region,
                  latitude=44.03114, longitude=-121.73567)
    add_trailhead(trailhead='Falls Creek Horse Camp Trailhead',
                  region=sw_wa_region,
                  latitude=45.96601, longitude=-121.84495)
    add_trailhead(trailhead='Hidden Lake Trailhead',
                  region=mthood_region,
                  latitude=45.31355, longitude=-121.79973)
    add_trailhead(trailhead='Devil\'s Peak Trailhead',
                  region=mthood_region,
                  latitude=45.25555, longitude=-121.86201)
    add_trailhead(trailhead='Devine Road Trailhead',
                  region=sw_wa_region,
                  latitude=45.63312, longitude=-122.61403)
    add_trailhead(trailhead='North Wildcat Trailhead',
                  region=east_or_region,
                  latitude=44.4979, longitude=-120.4827)
    add_trailhead(trailhead='Hunchback Mountain Trailhead',
                  region=mthood_region,
                  latitude=45.3423, longitude=-121.9405)
    add_trailhead(trailhead='Burnt Granite Trailhead',
                  region=mthood_region,
                  latitude=45.0045, longitude=-121.9374)
    add_trailhead(trailhead='Cape Meares Light Trailhead',
                  region=or_coast_region,
                  latitude=45.48588, longitude=-123.97459)
    add_trailhead(trailhead='Plaza Lake Trailhead',
                  region=mthood_region,
                  latitude=45.226877, longitude=-121.997466)
    add_trailhead(trailhead='McCully Trailhead',
                  region=east_or_region,
                  latitude=45.27721, longitude=-117.13593)
    add_trailhead(trailhead='Saint Cloud Trailhead',
                  region=gorge_region,
                  latitude=45.60074, longitude=-122.11051)
    add_trailhead(trailhead='Three Mile Trailhead',
                  region=mthood_region,
                  latitude=45.2724, longitude=-121.5435)
    add_trailhead(trailhead='Short Beach Trailhead',
                  region=or_coast_region,
                  latitude=45.47282, longitude=-123.96873)
    add_trailhead(trailhead='Pansy Lake Trailhead',
                  region=cent_or_region,
                  latitude=44.89991, longitude=-122.11636)
    add_trailhead(trailhead='Gotchen Creek South Trailhead',
                  region=sw_wa_region,
                  latitude=46.08625, longitude=-121.49153)
    add_trailhead(trailhead='Lava Lake Trailhead',
                  region=cent_or_region,
                  latitude=44.2593, longitude=-121.7871)
    add_trailhead(trailhead='Moulton Falls Lower Trailhead',
                  region=sw_wa_region,
                  latitude=45.83166, longitude=-122.38903)
    add_trailhead(trailhead='Sunset Beach Trailhead',
                  region=or_coast_region,
                  latitude=46.10142, longitude=-123.93547)
    add_trailhead(trailhead='Breitenbush Trailhead',
                  region=cent_or_region,
                  latitude=44.76471, longitude=-121.78649)
    add_trailhead(trailhead='Elk Lake Creek Trail Northern Trailhead',
                  region=cent_or_region,
                  latitude=44.89300, longitude=-122.00741)
    add_trailhead(trailhead='Grassy Knoll Trailhead',
                  region=sw_wa_region,
                  latitude=45.79759, longitude=-121.74112)
    add_trailhead(trailhead='Rainy Lake Trailhead',
                  region=gorge_region,
                  latitude=45.62469, longitude=-121.75830)
    add_trailhead(trailhead='Catalpa Lake Trailhead',
                  region=mthood_region,
                  latitude=45.21839, longitude=-121.63230)
    add_trailhead(trailhead='The Grotto Trailhead',
                  region=portland_region,
                  latitude=45.55325, longitude=-122.57468)
    add_trailhead(trailhead='Dry Ridge Trailhead',
                  region=mthood_region,
                  latitude=45.15857, longitude=-122.11591)
    add_trailhead(trailhead='Cape Horn Trailhead',
                  region=gorge_region,
                  latitude=45.58852, longitude=-122.17874)
    add_trailhead(trailhead='Hardy Ridge Equestrian Trailhead',
                  region=gorge_region,
                  latitude=45.64088, longitude=-122.03223)
    add_trailhead(trailhead='Bridal Veil Trailhead',
                  region=gorge_region,
                  latitude=45.55362, longitude=-122.18265)
    add_trailhead(trailhead='Big Spruce Trailhead',
                  region=or_coast_region,
                  latitude=45.48862, longitude=-123.96531)
    add_trailhead(trailhead='Angel\'s Rest Trailhead',
                  region=gorge_region,
                  latitude=45.56081, longitude=-122.17184)
    add_trailhead(trailhead='Fish Creek Trailhead',
                  region=mthood_region,
                  latitude=45.1578, longitude=-122.1511)
    add_trailhead(trailhead='Lower Deschutes Trailhead',
                  region=east_or_region,
                  latitude=45.6304, longitude=-120.9077)
    add_trailhead(trailhead='Wildwood Recreation Area Winter Trailhead',
                  region=mthood_region,
                  latitude=45.3559, longitude=-121.9864)
    add_trailhead(trailhead='Ridgefield Trailhead',
                  region=sw_wa_region,
                  latitude=45.83128, longitude=-122.74806)
    add_trailhead(trailhead='Labyrinth Trailhead',
                  region=gorge_region,
                  latitude=45.70508, longitude=-121.38970)
    add_trailhead(trailhead='Grouse Vista Trailhead',
                  region=sw_wa_region,
                  latitude=45.72200, longitude=-122.26950)
    add_trailhead(trailhead='Stewart Glen Trailhead',
                  region=sw_wa_region,
                  latitude=45.67338, longitude=-122.69025)
    add_trailhead(trailhead='Grave Creek Trailhead',
                  region=south_or_region,
                  latitude=42.6482, longitude=-123.5839)
    add_trailhead(trailhead='Cool Creek Trailhead',
                  region=mthood_region,
                  latitude=45.29724, longitude=-121.88349)
    add_trailhead(trailhead='Monon Lake Trailhead',
                  region=cent_or_region,
                  latitude=44.79475, longitude=-121.78971)
    add_trailhead(trailhead='Jean Lake Trailhead',
                  region=mthood_region,
                  latitude=45.30644, longitude=-121.57237)
    add_trailhead(trailhead='Siouxon Trailhead',
                  region=sw_wa_region,
                  latitude=45.94652, longitude=-122.17780)
    add_trailhead(trailhead='Warwick Trailhead',
                  region=sw_wa_region,
                  latitude=45.72066, longitude=-121.00091)
    add_trailhead(trailhead='Sacajawea Statue Trailhead',
                  region=portland_region,
                  latitude=45.52147, longitude=-122.70228)
    add_trailhead(trailhead='Vista Ridge Trailhead',
                  region=mthood_region,
                  latitude=45.442, longitude=-121.7255)
    add_trailhead(trailhead='Upper Oneonta Trailhead',
                  region=gorge_region,
                  latitude=45.528057, longitude=-122.081494)
    add_trailhead(trailhead='Soda Peaks Trailhead',
                  region=sw_wa_region,
                  latitude=45.89073, longitude=-122.06573)
    add_trailhead(trailhead='West Zigzag Trailhead',
                  region=mthood_region,
                  latitude=45.3452, longitude=-121.9298)
    add_trailhead(trailhead='Cascade Locks Trailhead',
                  region=gorge_region,
                  latitude=45.6619, longitude=-121.89805)
    add_trailhead(trailhead='Crescent Mountain Trailhead',
                  region=cent_or_region,
                  latitude=44.42915, longitude=-122.02995)
    add_trailhead(trailhead='Bonney Meadows Trailhead',
                  region=mthood_region,
                  latitude=45.26527, longitude=-121.58300)
    add_trailhead(trailhead='Whitewater Trailhead',
                  region=cent_or_region,
                  latitude=44.706730, longitude=-121.874899)
    add_trailhead(trailhead='Cornucopia Trailhead',
                  region=east_or_region,
                  latitude=44.145447, longitude=-120.583402)
    add_trailhead(trailhead='Little Zigzag Falls Trailhead',
                  region=mthood_region,
                  latitude=45.31400, longitude=-121.79596)
    add_trailhead(trailhead='Nichols Boulevard Trailhead',
                  region=sw_wa_region,
                  latitude=46.12755, longitude=-122.94369)
    add_trailhead(trailhead='Red Lake Trailhead',
                  region=cent_or_region,
                  latitude=44.81993, longitude=-121.87245)
    add_trailhead(trailhead='Bridge of the Gods Trailhead',
                  region=gorge_region,
                  latitude=45.6622, longitude=-121.89599)
    add_trailhead(trailhead='Holgate Trailhead',
                  region=portland_region,
                  latitude=45.48963, longitude=-122.51760)
    add_trailhead(trailhead='Boulder Lake Trailhead',
                  region=mthood_region,
                  latitude=45.25833, longitude=-121.55916)
    add_trailhead(trailhead='Ilwaco Waterfront Trailhead',
                  region=wa_coast_region,
                  latitude=46.30634, longitude=-124.03920)
    add_trailhead(trailhead='South Coldwater Trailhead',
                  region=sw_wa_region,
                  latitude=46.285809, longitude=-122.253799)
    add_trailhead(trailhead='Rowena Crest Trailhead',
                  region=gorge_region,
                  latitude=45.68259, longitude=-121.30065)
    add_trailhead(trailhead='Beacon Rock Trailhead',
                  region=gorge_region,
                  latitude=45.62844, longitude=-122.02206)
    add_trailhead(trailhead='Lacamas Creek Trailhead',
                  region=sw_wa_region,
                  latitude=45.58888, longitude=-122.39160)
    add_trailhead(trailhead='Woods Park Trailhead',
                  region=portland_region,
                  latitude=45.45751, longitude=-122.72630)
    add_trailhead(trailhead='Thomas Lake Trailhead',
                  region=sw_wa_region,
                  latitude=46.00555, longitude=-121.83761)
    add_trailhead(trailhead='South Climb Trailhead',
                  region=sw_wa_region,
                  latitude=46.13623, longitude=-121.49754)
    add_trailhead(trailhead='Filloon Trailhead',
                  region=sw_wa_region,
                  latitude=46.03426, longitude=-121.71620)
    add_trailhead(trailhead='Third Beach Trailhead',
                  region=wa_coast_region,
                  latitude=47.8888, longitude=-124.5984)
    add_trailhead(trailhead='Otter Bench Trailhead',
                  region=east_or_region,
                  latitude=44.462613, longitude=-121.283119)
    add_trailhead(trailhead='Hug Point Trailhead',
                  region=or_coast_region,
                  latitude=45.82866, longitude=-123.96084)
    add_trailhead(trailhead='Lower Lewis River Falls Trailhead',
                  region=sw_wa_region,
                  latitude=46.15469, longitude=-121.87958)
    add_trailhead(trailhead='Killen Creek Trailhead',
                  region=sw_wa_region,
                  latitude=46.2874, longitude=-121.5522)
    add_trailhead(trailhead='Wind Mountain Trailhead',
                  region=gorge_region,
                  latitude=45.71342, longitude=-121.75183)
    add_trailhead(trailhead='Powell Butte Main Trailhead',
                  region=portland_region,
                  latitude=45.49052, longitude=-122.49717)
    add_trailhead(trailhead='Lyle Trailhead',
                  region=sw_wa_region,
                  latitude=45.69668, longitude=-121.29019)
    add_trailhead(trailhead='Grizzly Peak Trailhead',
                  region=south_or_region,
                  latitude=42.27228, longitude=-122.60624)
    add_trailhead(trailhead='Laurel Hill Chute Trailhead',
                  region=mthood_region,
                  latitude=45.31121, longitude=-121.80145)
    add_trailhead(trailhead='Gold Butte Trailhead',
                  region=cent_or_region,
                  latitude=44.81876, longitude=-122.08686)
    add_trailhead(trailhead='Douglas Trailhead',
                  region=mthood_region,
                  latitude=45.30108, longitude=-122.06511)
    add_trailhead(trailhead='Cascade Head Lower Trailhead',
                  region=or_coast_region,
                  latitude=45.04225, longitude=-123.99187)
    add_trailhead(trailhead='Catherine Creek Trailhead',
                  region=gorge_region,
                  latitude=45.71043, longitude=-121.36172)
    add_trailhead(trailhead='Trout Creek Trailhead',
                  region=cent_or_region,
                  latitude=44.3985, longitude=-122.3472)
    add_trailhead(trailhead='Lower Macleay Park Trailhead',
                  region=portland_region,
                  latitude=45.53611, longitude=-122.71248)
    add_trailhead(trailhead='Cape Foulweather Trailhead',
                  region=or_coast_region,
                  latitude=44.77073, longitude=-124.07278)
    add_trailhead(trailhead='Polallie Trailhead',
                  region=mthood_region,
                  latitude=45.41756, longitude=-121.57002)
    add_trailhead(trailhead='Audubon Sanctuary Trailhead',
                  region=portland_region,
                  latitude=45.52676, longitude=-122.73013)
    add_trailhead(trailhead='Santiam Pass Trailhead',
                  region=cent_or_region,
                  latitude=44.425689, longitude=-121.849880)
    add_trailhead(trailhead='Opal Creek Trailhead',
                  region=cent_or_region,
                  latitude=44.85980, longitude=-122.26460)
    add_trailhead(trailhead='Climber\'s Bivouac Trailhead',
                  region=sw_wa_region,
                  latitude=46.14639, longitude=-122.18324)
    add_trailhead(trailhead='Bluff Mountain Trailhead',
                  region=sw_wa_region,
                  latitude=45.7804, longitude=-122.1666)
    add_trailhead(trailhead='Bachelor Mountain Trailhead',
                  region=cent_or_region,
                  latitude=44.6168, longitude=-122.03198)
    add_trailhead(trailhead='Ape Cave Trailhead',
                  region=sw_wa_region,
                  latitude=46.108408, longitude=-122.211442)
    add_trailhead(trailhead='Pilot Rock Trailhead',
                  region=south_or_region,
                  latitude=42.03059, longitude=-122.57022)
    add_trailhead(trailhead='Stahlman Point Trailhead',
                  region=cent_or_region,
                  latitude=44.7159, longitude=-122.1420)
    add_trailhead(trailhead='Salt Creek Trailhead',
                  region=sw_wa_region,
                  latitude=46.10548, longitude=-121.60400)
    add_trailhead(trailhead='Hamilton Mountain Trailhead',
                  region=sw_wa_region,
                  latitude=45.63279, longitude=-122.01973)
    add_trailhead(trailhead='Mark Hatfield East Trailhead',
                  region=gorge_region,
                  latitude=45.68094, longitude=-121.40850)
    add_trailhead(trailhead='South Breitenbush Trailhead',
                  region=cent_or_region,
                  latitude=44.742862, longitude=-121.888031)
    add_trailhead(trailhead='Echo Basin Trailhead',
                  region=cent_or_region,
                  latitude=44.4129, longitude=-122.0854)
    add_trailhead(trailhead='Wallowa Lake Trailhead',
                  region=east_or_region,
                  latitude=45.267040, longitude=-117.212834)
    add_trailhead(trailhead='Eastleg Road Trailhead',
                  region=mthood_region,
                  latitude=45.31073, longitude=-121.73023)
    add_trailhead(trailhead='Balfour-Klickitat Trailhead',
                  region=gorge_region,
                  latitude=45.69931, longitude=-121.29345)
    add_trailhead(trailhead='Scout Camp Trailhead',
                  region=east_or_region,
                  latitude=44.461055, longitude=-121.321400)
    add_trailhead(trailhead='Cape Lookout Day Use Trailhead',
                  region=or_coast_region,
                  latitude=45.35999, longitude=-123.97003)
    add_trailhead(trailhead='Multnomah Falls Trailhead',
                  region=gorge_region,
                  latitude=45.57758, longitude=-122.117)
    add_trailhead(trailhead='Falls Creek Falls Lower Trailhead',
                  region=sw_wa_region,
                  latitude=45.90571, longitude=-121.93984)
    add_trailhead(trailhead='Cape Lookout Trailhead',
                  region=or_coast_region,
                  latitude=45.34132, longitude=-123.97445)
    add_trailhead(trailhead='Terwilliger Trailhead',
                  region=portland_region,
                  latitude=45.49107, longitude=-122.68712)
    add_trailhead(trailhead='Bob Straub State Park Trailhead',
                  region=or_coast_region,
                  latitude=45.19277, longitude=-123.96727)
    add_trailhead(trailhead='Amanda\'s Trailhead',
                  region=mthood_region,
                  latitude=45.06675, longitude=-122.48973)
    add_trailhead(trailhead='Fret Creek Trailhead',
                  region=mthood_region,
                  latitude=45.349711, longitude=-121.472139)
    add_trailhead(trailhead='Whipple Creek Trailhead',
                  region=sw_wa_region,
                  latitude=45.74498, longitude=-122.69283)

    add_hikes(name='Perry Lake from Vista Ridge Hike',
              trailhead='Vista Ridge Trailhead',
              hike_type='out_and_back',
              distance=6.4, elevation=1000,
              difficulty_level='1moderate')
    add_hikes(name='Mount Mitchell Hike',
              trailhead='Mount Mitchell Trailhead',
              hike_type='out_and_back',
              distance=5.0, elevation=2050,
              difficulty_level='1moderate')
    add_hikes(name='Hamilton Mountain Loop Hike',
              trailhead='Hamilton Mountain Trailhead',
              hike_type='out_and_back',
              distance=7.5, elevation=2100,
              difficulty_level='1moderate')
    add_hikes(name='Bird Creek Meadows Loop Hike',
              trailhead='Bird Lake Trailhead',
              distance=6.2, elevation=1000,
              difficulty_level='1moderate')
    add_hikes(name='Audubon Sanctuaries Loop Hike',
              trailhead='Audubon Sanctuary Trailhead',
              hike_type='loop',
              distance=3.0, elevation=740, high_point=710,
              difficulty_level='0easy')
    add_hikes(name='Otter Bench Loop Hike',
              trailhead='Otter Bench Trailhead',
              hike_type='loop',
              distance=9.3, elevation=1700,
              difficulty_level='1moderate')
    add_hikes(name='Big Creek Falls Hike',
              trailhead='Big Creek Falls Trailhead',
              hike_type='out_and_back',
              distance=1.4, elevation=180,
              difficulty_level='0easy')
    add_hikes(name='Fort Cascades Hike',
              trailhead='Fort Cascades Trailhead',
              hike_type='loop',
              distance=1.5, elevation=20,
              difficulty_level='0easy')
    add_hikes(name='Coldwater Peak from South Coldwater Hike',
              trailhead='South Coldwater Trailhead',
              hike_type='out_and_back"',
              distance=14, elevation=3400,
              difficulty_level='2difficult')
    add_hikes(name='Hoyt Arboretum Loop Hike',
              trailhead='Hoyt Arboretum Trailhead',
              hike_type='loop',
              distance=4.7, elevation=425, high_point=850,
              difficulty_level='0easy')
    add_hikes(name='Powell Butte Summit Loop Hike',
              trailhead='Powell Butte Main Trailhead',
              hike_type='loop',
              distance=2.0, elevation=220,
              difficulty_level='0easy')
    add_hikes(name='Cooper Spur Hike',
              trailhead='Cloud Cap Trailhead',
              hike_type='out_and_back',
              distance=6.4, elevation=2800,
              difficulty_level='2difficult')
    add_hikes(name='Sunrise Camp Hike',
              trailhead='Bird Lake Trailhead',
              hike_type='lollipop',
              distance=10.8, elevation=3140, high_point=8350,
              difficulty_level='2difficult')
    add_hikes(name='Coffin Mountain Hike',
              trailhead='Coffin Mountain Trailhead',
              hike_type='out_and_back',
              distance=3, elevation=1000,
              difficulty_level='1moderate')
    add_hikes(name='Multnomah Falls Hike',
              trailhead='Multnomah Falls Trailhead',
              distance=2.6, elevation=700,
              difficulty_level='1moderate')
    add_hikes(name='Tanner Creek Hike',
              trailhead='Tooth Rock Trailhead',
              hike_type='out_and_back',
              distance=12.2, elevation=1400,
              difficulty_level='1moderate')
    add_hikes(name='Wahtum Lake via Pacific Crest Trail Hike',
              trailhead='Herman Creek Trailhead',
              hike_type='out_and_back',
              distance=33.8, elevation=6010,
              difficulty_level='2difficult')
    add_hikes(name='Eagle-Benson Loop Hike',
              trailhead='Eagle Creek Trailhead',
              hike_type='loop',
              distance=15.8, elevation=4260,
              difficulty_level='2difficult')
    add_hikes(name='Mount Defiance from Columbia River Hike',
              trailhead='Starvation Creek Trailhead',
              hike_type='out_and_back',
              distance=10.2, elevation=4840,
              difficulty_level='2difficult')
    add_hikes(name='Tam McArthur Rim Hike',
              trailhead='Tam McArthur Rim Trailhead',
              hike_type='out_and_back',
              distance=5, elevation=1200,
              difficulty_level='1moderate')
    add_hikes(name='Potato Butte Hike',
              trailhead='Red Lake Trailhead',
              hike_type='out_and_back',
              distance=7.2, elevation=1700,
              difficulty_level='1moderate')
    add_hikes(name='Kelley Point Loop Hike',
              trailhead='Kelley Point South Lot Trailhead',
              hike_type='loop',
              distance=1.7, elevation=45, high_point=40,
              difficulty_level='0easy')
    add_hikes(name='Lookingglass Lake via Stagman Ridge Hike',
              trailhead='Stagman Ridge Trailhead',
              hike_type='lollipop',
              distance=10.8, elevation=2415,
              difficulty_level='1moderate')
    add_hikes(name='Mountaineer Trail Loop Hike',
              trailhead='Timberline Lodge Trailhead',
              distance=2.7, elevation=1065, high_point=6925,
              difficulty_level='1moderate')
    add_hikes(name='Hood River Meadows Loop Hike',
              trailhead='Hood River Meadows Trailhead',
              hike_type='loop',
              distance=9.9, elevation=2055, high_point=5930,
              difficulty_level='2difficult')
    add_hikes(name='Dublin Lake Hike',
              trailhead='Tooth Rock Trailhead',
              hike_type='out_and_back',
              distance=13.8, elevation=3780,
              difficulty_level='2difficult')
    add_hikes(name='Ainsworth Loop Hike',
              trailhead='Ainsworth Loop Trailhead',
              hike_type='loop',
              distance=0.4, elevation=150,
              difficulty_level='0easy')
    add_hikes(name='Butte Creek Falls Loop Hike',
              trailhead='Butte Creek Falls Trailhead',
              hike_type='loop',
              distance=1.1, elevation=320,
              difficulty_level='0easy')
    add_hikes(name='Herman Creek Pinnacles Hike',
              trailhead='Herman Creek Trailhead',
              hike_type='out_and_back',
              distance=5.0, elevation=1000,
              difficulty_level='0easy')
    add_hikes(name='Larch Mountain Crater Hike',
              trailhead='Upper Oneonta Trailhead',
              distance=5.9, elevation=1310,
              difficulty_level='1moderate')
    add_hikes(name='Eagle Creek to Wahtum Lake Hike',
              trailhead='Eagle Creek Trailhead',
              hike_type='loop',
              distance=26.5, elevation=5310,
              difficulty_level='2difficult')
    add_hikes(name='Lookingglass Lake via Shorthorn Trail Hike',
              trailhead='Shorthorn Trailhead',
              distance=11.8, elevation=2495, high_point=6205,
              difficulty_level='1moderate')
    add_hikes(name='Big Slide Lake Hike',
              trailhead='Dickey Creek Trailhead',
              hike_type='out_and_back',
              distance=12.0, high_point=4405, elevation=1680,
              difficulty_level='1moderate')
    add_hikes(name='Catherine Creek to Coyote Wall Hike',
              trailhead='Catherine Creek Trailhead',
              hike_type='out_and_back',
              distance=8.2, elevation=1750,
              difficulty_level='1moderate')
    add_hikes(name='Rainy Lake via Gorton Creek Trail Hike',
              trailhead='Herman Creek Trailhead',
              hike_type='out_and_back',
              distance=23.0, elevation=5230,
              difficulty_level='2difficult')
    add_hikes(name='Palisade Point via Fret Creek Hike',
              trailhead='Fret Creek Trailhead',
              hike_type='out_and_back',
              distance=4.8, elevation=1325, high_point=5822,
              difficulty_level='1moderate')
    add_hikes(name='Casey Creek Loop Hike',
              trailhead='Herman Creek Trailhead',
              hike_type='loop',
              distance=11.3, high_point=4035, elevation=3995,
              difficulty_level='2difficult')
    add_hikes(name='Cascade Locks West Loop Hike',
              trailhead='Bridge of the Gods Trailhead',
              hike_type='loop',
              distance=3.0, elevation=100,
              difficulty_level='0easy')
    add_hikes(name='Salt Creek Hike',
              trailhead='Salt Creek Trailhead',
              hike_type='out_and_back',
              distance=8.4, elevation=730, high_point=3775,
              difficulty_level='1moderate')
    add_hikes(name='Ellen Davis Trail Hike',
              trailhead='St. James Road Trailhead',
              hike_type='out_and_back',
              distance=5.2, high_point=270, elevation=420,
              difficulty_level='0easy')
    add_hikes(name='Pechuck Lookout Hike',
              trailhead='Rooster Rock Road Trailhead',
              hike_type='out_and_back',
              distance=5.2, elevation=1580, high_point=4338,
              difficulty_level='1moderate')
    add_hikes(name='Pyramid Lake Hike',
              trailhead='Pyramid Lake Trailhead',
              hike_type='out_and_back',
              distance=2.4, elevation=340, high_point=3981,
              difficulty_level='0easy')
    add_hikes(name='Fish Lake-Si Lake Hike',
              trailhead='Lower Lake Trailhead',
              hike_type='out_and_back',
              distance=5.8, elevation=805, high_point=4835,
              difficulty_level='1moderate')
    add_hikes(name='Bridal Veil Falls Hike',
              trailhead='Bridal Veil Trailhead',
              hike_type='out_and_back',
              distance=0.6, elevation=70,
              difficulty_level='0easy')
    add_hikes(name='Triple Falls Hike',
              trailhead='Oneonta Trailhead',
              hike_type='out_and_back',
              distance=3.2, elevation=610,
              difficulty_level='1moderate')
    add_hikes(name='Cairn Basin from Top Spur Hike',
              trailhead='Top Spur Trailhead',
              distance=8.7, elevation=2200, high_point=5740,
              difficulty_level='2difficult')
    add_hikes(name='Chetwoot Loop Hike',
              trailhead='Mitchell Point Trailhead',
              hike_type='loop',
              distance=4.4,
              difficulty_level='1moderate')
    add_hikes(name='Yacolt Falls Hike',
              trailhead='Moulton Falls Lower Trailhead',
              hike_type='out_and_back',
              distance=0.6, elevation=30,
              difficulty_level='0easy')
    add_hikes(name='Lewis and Clark Park Hike',
              trailhead='Lewis and Clark Park Trailhead',
              hike_type='out_and_back',
              distance=3.0, elevation=100,
              difficulty_level='0easy')
    add_hikes(name='Siouxon Creek Hike',
              trailhead='Siouxon Trailhead',
              hike_type='lollipop',
              distance=8.2, elevation=1615, high_point=1560,
              difficulty_level='1moderate')
    add_hikes(name='Rattlesnake Falls Hike',
              trailhead='Rattlesnake Falls Trailhead',
              hike_type='out_and_back',
              distance=2.5, elevation=525, high_point=1960,
              difficulty_level='0easy')
    add_hikes(name='Nehalem Spit Loop Hike',
              trailhead='Nehalem Spit Trailhead',
              hike_type='loop',
              distance=5.2, elevation=25, high_point=20,
              difficulty_level='0easy')
    add_hikes(name='Toleak Point Hike',
              trailhead='Third Beach Trailhead',
              distance=12, elevation=1200,
              difficulty_level='2difficult')
    add_hikes(name='Benson Plateau Loop Hike',
              trailhead='Herman Creek Trailhead',
              hike_type='out_and_back)',
              distance=16.2, elevation=4080,
              difficulty_level='2difficult')
    add_hikes(name='Clatsop Loop Hike',
              trailhead='Indian Beach Trailhead',
              hike_type='loop',
              distance=3, elevation=700,
              difficulty_level='0easy')
    add_hikes(name='Painted Cove Loop Hike',
              trailhead='Painted Cove Trailhead',
              hike_type='loop',
              distance=0.2, elevation=40,
              difficulty_level='0easy')
    add_hikes(name='Hug Point Hike',
              trailhead='Hug Point Trailhead',
              hike_type='out_and_back',
              distance=0.5, elevation=20,
              difficulty_level='0easy')
    add_hikes(name='Russ Lake Loop Hike',
              trailhead='Olallie Meadows Trailhead',
              hike_type='loop',
              distance=2.8, elevation=225, high_point=4640,
              difficulty_level='0easy')
    add_hikes(name='Ape Canyon Hike',
              trailhead='Ape Canyon Trailhead',
              hike_type='out_and_back',
              distance=11.0, elevation=2485, high_point=4315,
              difficulty_level='1moderate')
    add_hikes(name='Lava Canyon from Smith Creek Hike',
              trailhead='Lower Smith Creek Trailhead',
              hike_type='out_and_back',
              distance=6.5, elevation=1500,
              difficulty_level='1moderate')
    add_hikes(name='Tomlike mountain hike',
              trailhead='Wahtum Lake Trailhead',
              hike_type='lollipop',
              distance=6.8, high_point=4555, elevation=1565,
              difficulty_level='1moderate')
    add_hikes(name='Jefferson Park from Whitewater Trailhead Hike',
              trailhead='Whitewater Trailhead',
              hike_type='out_and_back',
              distance=11.0, elevation=1800,
              difficulty_level='1moderate',
              high_point=5880)
    add_hikes(name='Green Lakes via Fall Creek Hike',
              trailhead='Fall Creek Trailhead',
              hike_type='out_and_back',
              distance=8.4, elevation=1150,
              difficulty_level='1moderate')
    add_hikes(name='Cape Foulweather Hike',
              trailhead='Cape Foulweather Trailhead',
              hike_type='out_and_back',
              distance=0.6, elevation=120,
              difficulty_level='0easy')
    add_hikes(name='Nesmith-Tanner Traverse Hike',
              trailhead='John B Yeon Trailhead',
              hike_type='point_to_point',
              distance=16.7, elevation=4350,
              difficulty_level_explanation='elevation',
              difficulty_level='2difficult')
    add_hikes(name='Larch Mountain Hike',
              trailhead='Multnomah Falls Trailhead',
              hike_type='out_and_back',
              distance=14.4, elevation=4010,
              difficulty_level='2difficult')
    add_hikes(name='Crescent Mountain Hike',
              trailhead='Crescent Mountain Trailhead',
              hike_type='out_and_back',
              distance=9, elevation=2200, high_point=5750,
              difficulty_level='2difficult')
    add_hikes(name='East Fork Wallowa River Hike',
              trailhead='Wallowa Lake Trailhead',
              hike_type='out_and_back',
              distance=17.0, elevation=4620, high_point=8500,
              difficulty_level='2difficult')
    add_hikes(name='Columbia Springs Hike',
              trailhead='Columbia Springs Trailhead',
              hike_type='out_and_back',
              distance=3.1, high_point=100, elevation=165,
              difficulty_level='0easy')
    add_hikes(name='Rocky Butte Hike',
              trailhead='The Grotto Trailhead',
              hike_type='out_and_back',
              distance=3.2, elevation=480, high_point=612,
              difficulty_level='0easy')
    add_hikes(name='Sleeping Beauty Hike',
              trailhead='Sleeping Beauty Trailhead',
              hike_type='out_and_back',
              distance=3.0, elevation=1430, high_point=4907,
              difficulty_level='1moderate')
    add_hikes(name='Neahkahnie Mountain Loop Hike',
              trailhead='North Neahkahnie Mountain Trailhead',
              hike_type='loop',
              distance=5.4, elevation=1450,
              difficulty_level='1moderate')
    add_hikes(name='Lewisville Park Loop Hike',
              trailhead='Lewisville Park Entrance Trailhead',
              hike_type='loop',
              distance=2.8, elevation=140, high_point=235,
              difficulty_level='0easy')
    add_hikes(name='Rogue River Hike',
              trailhead='Grave Creek Trailhead',
              distance=39.5, elevation=2000,
              difficulty_level='1moderate')
    add_hikes(name='Tillamook Head Traverse Hike',
              trailhead='Tillamook Head Trailhead',
              hike_type='point_to_point',
              distance=6.3, elevation=1350,
              difficulty_level='1moderate')
    add_hikes(name='Klickitat Trail=Swale Canyon Hike',
              trailhead='Warwick Trailhead',
              hike_type='out_and_back',
              distance=15.0, elevation=1010, high_point=1560,
              difficulty_level='1moderate')
    add_hikes(name='Rowena Plateau Hike',
              trailhead='Rowena Crest Trailhead',
              hike_type='out_and_back',
              distance=1.0, elevation=100,
              difficulty_level='0easy')
    add_hikes(name='Cape Kiwanda Hike',
              trailhead='Pacific Avenue Trailhead',
              hike_type='lollipop',
              distance=2.2, elevation=230, high_point=220,
              difficulty_level='0easy')
    add_hikes(name='Strawberry Mountain Loop Hike',
              trailhead='Strawberry Trailhead',
              distance=17, elevation=4500,
              difficulty_level='2difficult')
    add_hikes(name='Waucoma Lakes Loop Hike',
              trailhead='Rainy Lake Trailhead',
              hike_type='loop',
              distance=16.5, elevation=3170, high_point=4737,
              difficulty_level='2difficult')
    add_hikes(name='Tombstone Lake via the PCT Hike',
              trailhead='Crest Camp Trailhead',
              distance=16.4,
              hike_type='out_and_back',
              elevation=2280, high_point=5005,
              difficulty_level='2difficult')
    add_hikes(name='Whychus Creek Hike',
              trailhead='Alder Springs (Whychus Creek) Trailhead',
              hike_type='out_and_back',
              distance=6.2, elevation=910, high_point=2625,
              difficulty_level='1moderate')
    add_hikes(name='Lyle Cherry Orchard Hike',
              trailhead='Lyle Cherry Orchard Trailhead',
              hike_type='out_and_back',
              distance=5.0, elevation=1160,
              difficulty_level='1moderate')
    add_hikes(name='Mount Hood Meadows via White River Canyon Hike',
              trailhead='Timberline Lodge Trailhead',
              distance=9.0, elevation=2320, high_point=6035,
              difficulty_level='1moderate')
    add_hikes(name='Labyrinth Hike',
              trailhead='Labyrinth Trailhead',
              hike_type='out_and_back',
              distance=2.0, elevation=570,
              difficulty_level='0easy')
    add_hikes(name='Middle Lewis River Falls Loop Hike',
              trailhead='Middle Falls Trailhead',
              hike_type='loop',
              distance=1.1, elevation=190,
              difficulty_level='0easy')
    add_hikes(name='McCall Point Hike',
              trailhead='Rowena Crest Trailhead',
              hike_type='out_and_back',
              distance=3.6, elevation=1070,
              difficulty_level='1moderate')
    add_hikes(name='Stahlman Point Hike',
              trailhead='Stahlman Point Trailhead',
              hike_type='out_and_back',
              distance=5, elevation=1300,
              difficulty_level='1moderate')
    add_hikes(name='Gordon Butte-Douglas Cabin Loop Hike',
              trailhead='Sunset Spring Trailhead',
              hike_type='loop',
              distance=9.5, elevation=2925, high_point=5657,
              difficulty_level='2difficult')
    add_hikes(name='Leaf Hill Loop Hike',
              trailhead='Leaf Hill Trailhead',
              hike_type='loop',
              distance=0.3, elevation=20,
              difficulty_level='0easy')
    add_hikes(name='Cape Lookout Hike',
              trailhead='Cape Lookout Trailhead',
              hike_type='out_and_back',
              distance=5.2, elevation=450,
              difficulty_level='1moderate')
    add_hikes(name='Chinidere Mountain Hike',
              trailhead='Wahtum Lake Trailhead',
              hike_type='loop',
              distance=4.4, elevation=1140, high_point=4673,
              difficulty_level='1moderate')
    add_hikes(name='Little Mount Adams Hike',
              trailhead='Hellroaring Creek Trailhead',
              distance=6.9, elevation=2030, high_point=6821,
              difficulty_level='2difficult')
    add_hikes(name='North Lake Hike',
              trailhead='Wyeth Trailhead',
              hike_type='out_and_back',
              distance=12.8, high_point=3988, elevation=4220,
              difficulty_level='2difficult')
    add_hikes(name='Cape Lookout South Hike',
              trailhead='Cape Lookout Trailhead',
              hike_type='out_and_back',
              distance=3.6, high_point=840, elevation=840,
              difficulty_level='0easy')
    add_hikes(name='Gillette Lake Hike',
              trailhead='Bonneville Trailhead',
              hike_type='out_and_back',
              distance=5.8, elevation=648,
              difficulty_level='0easy')
    add_hikes(name='Hart\'s Cove Hike',
              trailhead="Hart's Cove Trailhead",
              hike_type='out_and_back',
              distance=5.4, elevation=1000,
              difficulty_level='1moderate')
    add_hikes(name='Fossil Trail Loop Hike',
              trailhead='Kalama Horse Camp Trailhead',
              hike_type='loop',
              distance=12.4, elevation=3300, high_point=3600,
              difficulty_level='2difficult')
    add_hikes(name='Rooster Rock via Trout Creek Trail Hike',
              trailhead='Trout Creek Trailhead',
              hike_type='out_and_back',
              distance=7.0, elevation=2200,
              difficulty_level='1moderate')
    add_hikes(name='Cairn Basin via Mazama Trail Hike',
              trailhead='Mazama Trailhead',
              hike_type='out_and_back',
              distance=8.8, elevation=2465, high_point=5745,
              difficulty_level='1moderate')
    add_hikes(name='Horsetail Falls Loop Hike',
              trailhead='Oneonta Gorge Trailhead',
              hike_type='loop',
              distance=2.6, elevation=610,
              difficulty_level='0easy')
    add_hikes(name='Bachelor Mountain Hike',
              trailhead='Bachelor Mountain Trailhead',
              hike_type='out_and_back',
              distance=3.8, elevation=1100,
              difficulty_level='1moderate')
    add_hikes(name='Gee Creek Bottomland Hike',
              trailhead='Ridgefield Trailhead',
              hike_type='out_and_back',
              distance=3.8, elevation=85, high_point=75,
              difficulty_level='0easy')
    add_hikes(name='Divide Lake Hike',
              trailhead='Vivian Lake Trailhead',
              hike_type='out_and_back',
              distance=8, elevation=1200,
              difficulty_level='1moderate')
    add_hikes(name='Silver Star via Bluff Mountain Hike',
              trailhead='Bluff Mountain Trailhead',
              hike_type='out_and_back',
              distance=12.4, elevation=1660,
              difficulty_level='2difficult')
    add_hikes(name='Wahkeena Falls Hike',
              trailhead='Wahkeena Trailhead',
              hike_type='out_and_back',
              distance=1.4, elevation=850,
              difficulty_level='1moderate')
    add_hikes(name='Pine Creek-Badger Butte Loop Hike',
              trailhead='Three Mile Trailhead',
              hike_type='loop',
              distance=9.8, elevation=2180, high_point=5981,
              difficulty_level='1moderate')
    add_hikes(name='Elk Cove from Cloud Cap Hike',
              trailhead='Cloud Cap Trailhead',
              distance=9.6, elevation=1600, high_point=6200,
              difficulty_level_explanation='especially Coe Branch Crossing',
              difficulty_level='2difficult')
    add_hikes(name='Illinois River Hike',
              trailhead='Illinois Southeast Trailhead',
              distance=25, elevation=5000,
              difficulty_level='1moderate')
    add_hikes(name='Eagle Creek to Tunnel Falls Hike',
              trailhead='Eagle Creek Trailhead',
              hike_type='out_and_back',
              distance=12.0, elevation=1640)
    add_hikes(name='Table Mountain from Bonneville Hike',
              trailhead='Bonneville Trailhead',
              hike_type='out_and_back',
              distance=15.8, elevation=3350,
              difficulty_level='2difficult')
    add_hikes(name='Crabtree Valley Hike',
              trailhead='Crabtree Valley Trailhead',
              hike_type='out_and_back',
              distance=3.4, elevation=900,
              difficulty_level='1moderate')
    add_hikes(name='Whitaker Ponds Loop Hike',
              trailhead='Whitaker Ponds Trailhead',
              hike_type='loop',
              distance=0.5, elevation=10, high_point=15,
              difficulty_level='0easy')
    add_hikes(name='Little Beacon Rock Loop Hike',
              trailhead='Hamilton Mountain Trailhead',
              hike_type='loop',
              distance=1.9, elevation=200,
              difficulty_level='0easy')
    add_hikes(name='Cape Lookout North Hike',
              trailhead='Cape Lookout Day Use Trailhead',
              hike_type='out_and_back',
              distance=9.6, elevation=2340,
              difficulty_level='1moderate')
    add_hikes(name='Elk Cove from Vista Ridge Hike',
              trailhead='Vista Ridge Trailhead',
              distance=8.8, elevation=2000, high_point=5800,
              difficulty_level='1moderate')
    add_hikes(name='Catalpa Lake via Bonney Meadows Trail Hike',
              trailhead='Wamic Road Trailhead',
              hike_type='out_and_back',
              distance=9.0, elevation=1750, high_point=4195,
              difficulty_level='1moderate')
    add_hikes(name='Dry Creek Falls Hike',
              trailhead='Bridge of the Gods Trailhead',
              hike_type='out_and_back',
              distance=4.4, elevation=710,
              difficulty_level='0easy')
    add_hikes(name='Cairn Basin from Vista Ridge Hike',
              trailhead='Vista Ridge Trailhead',
              distance=7.6, elevation=1560, high_point=5920,
              difficulty_level='2difficult')
    add_hikes(name='Table Rock Hike',
              trailhead='Table Rock Trailhead',
              hike_type='out_and_back',
              distance=7.2, elevation=1570, high_point=4881,
              difficulty_level='1moderate')
    add_hikes(name='Eagle Creek (Salmon-Huckleberry) Hike',
              trailhead='Harvey Road Trailhead',
              hike_type='out_and_back',
              elevation=1835, high_point=2405,
              difficulty_level='1moderate')
    add_hikes(name='Netul River Hike',
              trailhead='Fort Clatsop Trailhead',
              distance=1.5, elevation=23,
              difficulty_level='0easy')
    add_hikes(name='Eagle Creek to High Bridge Hike',
              trailhead='Eagle Creek Trailhead',
              hike_type='out_and_back',
              distance=6.4, elevation=840,
              difficulty_level='0easy')
    add_hikes(name='McNeil Point Hike',
              trailhead='Top Spur Trailhead',
              distance=10.4, elevation=2200, high_point=6100,
              difficulty_level='2difficult')
    add_hikes(name='Silver Star via Grouse Vista Hike',
              trailhead='Grouse Vista Trailhead',
              hike_type='out_and_back',
              distance=6.0, elevation=2040,
              difficulty_level='1moderate')
    add_hikes(name='Eagle Creek to Punchbowl Falls Hike',
              trailhead='Eagle Creek Trailhead',
              hike_type='out_and_back',
              distance=3.8, elevation=500,
              difficulty_level='0easy')
    add_hikes(name='Twin Lakes from Elk Lake Hike',
              trailhead='Bagby Trailhead',
              hike_type='out_and_back',
              distance=15.6, elevation=3295, high_point=5558,
              difficulty_level='2difficult')
    add_hikes(name='BPA Road-Newton Road Loop Hike',
              trailhead='BPA Road Trailhead',
              hike_type='loop',
              distance=8.1, elevation=2600, high_point=1030,
              difficulty_level='1moderate')
    add_hikes(name='Cannon Beach Hike',
              trailhead='Cannon Beach Trailhead',
              hike_type='out_and_back',
              distance=10.2, elevation=25, high_point=25,
              difficulty_level='1moderate')
    add_hikes(name='Big Huckleberry Mountain Hike',
              trailhead='Grassy Knoll Trailhead',
              hike_type='out_and_back',
              distance=11.8, elevation=2935, high_point=4202,
              difficulty_level='2difficult')
    add_hikes(name='South Molalla River Trails Loop Hike',
              trailhead='Hardy Creek Trailhead',
              hike_type='loop',
              distance=9.9, elevation=1375, high_point=1480,
              difficulty_level='1moderate')
    add_hikes(name='Dog Mountain Hike',
              trailhead='Dog Mountain Trailhead',
              hike_type='loop',
              distance=6.9, elevation=2800,
              difficulty_level='2difficult')
    add_hikes(name='Ruckel Ridge Loop Hike',
              trailhead='Eagle Creek Trailhead',
              hike_type='loop',
              distance=9.0, elevation=3700,
              difficulty_level='2difficult')
    add_hikes(name='Buck Point Hike',
              trailhead='Eagle Creek Trailhead',
              hike_type='out_and_back',
              distance=1.8, elevation=570,
              difficulty_level='1moderate')
    add_hikes(name='Hawk Mountain Lookout Hike',
              trailhead='Rho Ridge Southern Trailhead',
              hike_type='out_and_back',
              distance=4.0, elevation=600,
              difficulty_level='0easy')
    add_hikes(name='Jawbone Flats Hike',
              trailhead='Opal Creek Trailhead',
              hike_type='out_and_back',
              distance=6.25, elevation=200,
              difficulty_level='1moderate')
    add_hikes(name='Cape Horn Loop Hike',
              trailhead='Cape Horn Trailhead',
              hike_type='loop',
              distance=7.1, elevation=1350,
              difficulty_level='1moderate')
    add_hikes(name='Nesmith Point Hike',
              trailhead='John B Yeon Trailhead',
              hike_type='out_and_back',
              distance=10.6, elevation=3800,
              difficulty_level_explanation='elevation',
              difficulty_level='2difficult')
    add_hikes(name='Burnt Granite-Tarzan Springs Hike',
              trailhead='Burnt Granite Trailhead',
              hike_type='out_and_back',
              distance=8.3, elevation=2070, high_point=4850,
              difficulty_level='1moderate')
    add_hikes(name='Shining Lake Hike',
              trailhead='Frazier Trailhead',
              hike_type='out_and_back',
              distance=9.7, elevation=1050, high_point=4780,
              difficulty_level='1moderate')
    add_hikes(name='South Tieton Hike',
              trailhead='Conrad Meadows Trailhead',
              distance=17.6, elevation=1860,
              difficulty_level='2difficult')
    add_hikes(name='Clatsop Spit Loop Hike',
              trailhead='Clatsop Spit Trailhead',
              hike_type='loop',
              distance=4.6, elevation=10, high_point=10,
              difficulty_level='0easy')
    add_hikes(name='Fort Stevens Military Loop Hike',
              trailhead='Military Museum Trailhead',
              hike_type='loop',
              distance=2.6, elevation=20, high_point=25,
              difficulty_level='0easy')
    add_hikes(name='Elk Mountain-Elk Meadows Loop Hike',
              trailhead='Hood River Meadows Trailhead',
              hike_type='lollipop',
              distance=8.2, elevation=1445, high_point=5605,
              difficulty_level='1moderate')
    add_hikes(name='Devil\'s Peak Hike',
              trailhead="Devil's Peak Trailhead",
              distance=3.0, elevation=660, high_point=5045,
              difficulty_level='0easy')
    add_hikes(name='Bell Creek Loop Hike',
              trailhead='Oneonta Trailhead',
              hike_type='out_and_back',
              distance=14.5, elevation=3330,
              difficulty_level='2difficult')
    add_hikes(name='Klickitat Trail=Klickitat Mineral Springs Hike',
              trailhead='Wahkiacus Trailhead',
              hike_type='out_and_back',
              distance=5.2, elevation=50, high_point=545,
              difficulty_level='0easy')
    add_hikes(name='Cape Meares Hike',
              trailhead='Big Spruce Trailhead',
              hike_type='out_and_back',
              distance=5.4, high_point=520, elevation=885,
              difficulty_level='1moderate')
    add_hikes(name='Battle Ax Creek Loop Hike',
              trailhead='Bagby Trailhead',
              hike_type='loop',
              distance=15.4, elevation=4855, high_point=5558,
              difficulty_level='2difficult')
    add_hikes(name='Cascade Head Hike',
              trailhead='Cascade Head Lower Trailhead',
              hike_type='out_and_back',
              distance=6.8, elevation=1310,
              difficulty_level='1moderate')
    add_hikes(name='Pansy Lake Hike',
              trailhead='Pansy Lake Trailhead',
              hike_type='out_and_back',
              elevation=500,
              difficulty_level='0easy')
    add_hikes(name='Tolinda-Ridge Trail Loop Hike',
              trailhead='Tolinda Trailhead',
              hike_type='loop',
              distance=5.9, elevation=1685, high_point=1045,
              difficulty_level='1moderate')
    add_hikes(name='Dry Ridge Hike',
              trailhead='Dry Ridge Trailhead',
              hike_type='out_and_back',
              distance=14.0, elevation=3415, high_point=4488,
              difficulty_level='2difficult')
    add_hikes(name='Steigerwald National Wildlife Refuge Hike',
              trailhead='Steigerwald Lake Trailhead',
              hike_type='loop',
              distance=2.8, elevation=0,
              difficulty_level='0easy')
    add_hikes(name='Tolmie Lookout via Eunice Lake Hike',
              trailhead='Mowich Lake Trailhead',
              hike_type='out_and_back',
              distance=6.6, elevation=1640, high_point=5930,
              difficulty_level='1moderate')
    add_hikes(name='Multorpor Mountain Loop Hike',
              trailhead='Summit Rest Area Trailhead',
              hike_type='loop',
              distance=5.1, elevation=1100, high_point=4656,
              difficulty_level='1moderate')
    add_hikes(name='Horseshoe Meadows-Lookingglass Lake Loop Hike',
              trailhead='Williams Mine Trailhead',
              distance=13.2, elevation=2000,
              difficulty_level='1moderate')
    add_hikes(name='Marquam Nature Park Loop Hike',
              trailhead='Marquam Nature Park Shelter Trailhead',
              hike_type='loop',
              distance=4.1, elevation=400, high_point=790,
              difficulty_level='0easy')
    add_hikes(name='Defiance-Starvation Loop Hike',
              trailhead='Starvation Creek Trailhead',
              hike_type='loop',
              distance=11.6, elevation=4940,
              difficulty_level='2difficult')
    add_hikes(name='Devil\'s Peak from Cool Creek Hike',
              trailhead='Cool Creek Trailhead',
              hike_type='out_and_back',
              distance=7.6, elevation=3200, high_point=5045,
              difficulty_level='2difficult')
    add_hikes(name='Ridgefield Wildlife Refuge Hike',
              trailhead='Ridgefield Trailhead',
              hike_type='loop',
              distance=2.0, elevation=100, high_point=75,
              difficulty_level='0easy')
    add_hikes(name='Munra Point from Wahclella Hike',
              trailhead='Wahclella Falls Trailhead',
              hike_type='out_and_back',
              distance=5.8, elevation=1870,
              difficulty_level='2difficult')
    add_hikes(name='Mount Defiance from Wahtum Lake Road Hike',
              trailhead='Upper Mount Defiance Trailhead',
              hike_type='out_and_back',
              distance=3.2, elevation=1145, high_point=4959,
              difficulty_level='0easy')
    add_hikes(name='Nick Eaton Ridge Loop Hike',
              trailhead='Herman Creek Trailhead',
              hike_type='loop',
              distance=14.0, elevation=3840,
              difficulty_level='2difficult')
    add_hikes(name='Upper Siouxon Creek Loop Hike',
              trailhead='Upper Siouxon Trailhead',
              hike_type='lollipop',
              distance=11.9, elevation=3525, high_point=3485,
              difficulty_level='2difficult')
    add_hikes(name='Timberline Trail around Mount Hood Hike',
              trailhead='Cloud Cap Trailhead',
              distance=38.9, elevation=8000, high_point=7350,
              difficulty_level='2difficult')
    add_hikes(name='Table Mountain Loop Hike',
              trailhead='Aldrich Butte Trailhead',
              hike_type='out_and_back',
              distance=8.0, elevation=3350,
              difficulty_level='2difficult')
    add_hikes(name='Devil\'s Rest via Wahkeena Hike',
              trailhead='Wahkeena Trailhead',
              hike_type='lollipop',
              distance=7.5, elevation=2550,
              difficulty_level='1moderate')
    add_hikes(name='Jefferson Park Ridge Hike',
              trailhead='Breitenbush Trailhead',
              distance=7.4, elevation=1500,
              difficulty_level='1moderate')
    add_hikes(name='Dog River Trail Hike',
              trailhead='Zigzag Trailhead',
              hike_type='point_to_point',
              distance=7.1, elevation=1600,
              difficulty_level='1moderate')
    add_hikes(name='Deschutes River Hike',
              trailhead='Lower Deschutes Trailhead',
              distance=22.6, elevation=400,
              difficulty_level='1moderate')
    add_hikes(name='Pine Creek Hike',
              trailhead='Pine Creek Trailhead',
              hike_type='out_and_back',
              distance=0.8, elevation=90, high_point=3010,
              difficulty_level='0easy')
    add_hikes(name='Mike Miller Park Loop Hike',
              trailhead='Mike Miller Educational Trailhead',
              hike_type='loop',
              distance=1.2, elevation=115, high_point=170,
              difficulty_level='0easy')
    add_hikes(name='Squaw Mountain from Squaw Mountain Road Hike',
              trailhead='Squaw Mountain Road Trailhead',
              hike_type='out_and_back',
              distance=4.2, elevation=700,
              difficulty_level='0easy')
    add_hikes(name='Catalpa Lake Hike',
              trailhead='Catalpa Lake Trailhead',
              hike_type='out_and_back',
              distance=1.4, elevation=150, high_point=4195,
              difficulty_level='0easy')
    add_hikes(name='Angel\'s Rest Hike',
              trailhead="Angel's Rest Trailhead",
              hike_type='out_and_back',
              distance=4.8, elevation=1450,
              difficulty_level='1moderate')
    add_hikes(name='Starvation Ridge Hike',
              trailhead='Starvation Creek Trailhead',
              hike_type='out_and_back',
              distance=6.4, elevation=3800,
              difficulty_level='2difficult')
    add_hikes(name='Paradise Point Loop Hike',
              trailhead='Paradise Point Trailhead',
              hike_type='loop',
              distance=1.8, high_point=170, elevation=240,
              difficulty_level='0easy')
    add_hikes(name='Bald Butte Hike',
              trailhead='Oak Ridge Trailhead',
              hike_type='out_and_back',
              distance=8, elevation=2100,
              difficulty_level='1moderate')
    add_hikes(name='Vancouver Discovery Loop Hike',
              trailhead='Vancouver Quay Trailhead',
              hike_type='loop',
              distance=4.4, high_point=110, elevation=130,
              difficulty_level='0easy')
    add_hikes(name='Table Rock-Image Creek Loop Hike',
              trailhead='Table Rock Trailhead',
              hike_type='loop',
              distance=13.6, elevation=4030, high_point=4881,
              difficulty_level='2difficult')
    add_hikes(name='Goat Marsh Lake Hike',
              trailhead='Goat Marsh Lake Trailhead',
              hike_type='out_and_back',
              distance=1.5, elevation=80, high_point=2915,
              difficulty_level='0easy')
    add_hikes(name='Silver Star Loop Hike',
              trailhead='Silver Star Trailhead',
              hike_type='loop',
              distance=5.7, high_point=4390, elevation=1460,
              difficulty_level='1moderate')
    add_hikes(name='Mud Lake Hike',
              trailhead='Wahtum Lake Trailhead',
              hike_type='out_and_back',
              distance=7.4, elevation=1400, high_point=4480,
              difficulty_level='1moderate')
    add_hikes(name='Elk Meadows Hike',
              trailhead='Hood River Meadows Trailhead',
              distance=5.3, elevation=1200, high_point=5280,
              difficulty_level='1moderate')
    add_hikes(name='Nesmith-Oneonta Traverse Hike',
              trailhead='John B Yeon Trailhead',
              hike_type='point_to_point',
              distance=14.1, elevation=3800,
              difficulty_level_explanation='elevation and length',
              difficulty_level='2difficult')
    add_hikes(name='North and McKenzie Heads Hike',
              trailhead='Beards Hollow Trailhead',
              hike_type='out_and_back',
              distance=6.6, elevation=1175, high_point=310,
              difficulty_level='1moderate')
    add_hikes(name='Lamberson Spur Loop Hike',
              trailhead='Polallie Trailhead',
              hike_type='loop',
              distance=18.3, elevation=5035, high_point=7330,
              difficulty_level='2difficult')
    add_hikes(name='Mother Lode Loop Hike',
              trailhead='Pansy Lake Trailhead',
              hike_type='lollipop',
              distance=13.5, high_point=5150, elevation=3650,
              difficulty_level='2difficult')
    add_hikes(name='Horseshoe Ridge Hike',
              trailhead='Cast Creek Trailhead',
              hike_type='out_and_back',
              distance=10.8, elevation=2700,
              difficulty_level='1moderate')
    add_hikes(name='Thorp Creek Hike',
              trailhead='Hurricane Creek Trailhead',
              hike_type='out_and_back',
              distance=9.9, elevation=2830, high_point=7560,
              difficulty_level='1moderate')
    add_hikes(name='West Zigzag From Devil Canyon Hike',
              trailhead='South Burnt Lake Trailhead',
              hike_type='out_and_back',
              distance=5.4, elevation=1100,
              difficulty_level='2difficult')
    add_hikes(name='Pine Lakes Hike',
              trailhead='Cornucopia Trailhead',
              hike_type='out_and_back',
              distance=15, elevation=2700,
              difficulty_level='2difficult')
    add_hikes(name='Cone Peak Hike',
              trailhead='Tombstone Pass Trailhead',
              hike_type='out_and_back',
              distance=4.8, elevation=820,
              difficulty_level='1moderate')
    add_hikes(name='Coastal Forest Loop Hike',
              trailhead='Coastal Forest Trailhead',
              hike_type='loop',
              distance=1.5, elevation=130, high_point=90,
              difficulty_level='0easy')
    add_hikes(name='Cinnamon Ridge Loop Hike',
              trailhead='Kalama Horse Camp Trailhead',
              hike_type='loop',
              distance=14.1, elevation=2850, high_point=4000,
              difficulty_level='2difficult')
    add_hikes(name='Placid Lake Loop Hike',
              trailhead='Placid Lake Trailhead',
              distance=10.1,
              hike_type='loop',
              elevation=1460, high_point=5120,
              difficulty_level='1moderate')
    add_hikes(name='Cooper Ridge-South Beach Loop Hike',
              trailhead='South Beach Trailhead',
              hike_type='loop',
              distance=3.3, elevation=70, high_point=45,
              difficulty_level='0easy')
    add_hikes(name='North Siouxon Creek Hike',
              trailhead='North Siouxon Trailhead',
              hike_type='out_and_back',
              distance=10.4, elevation=1290, high_point=1815,
              difficulty_level='1moderate')
    add_hikes(name='Tryon Creek State Park Hike',
              trailhead='Tryon Creek State Park Trailhead',
              hike_type='loop',
              distance=2.7, elevation=125,
              difficulty_level='0easy')
    add_hikes(name='Squaw Mountain Hike',
              trailhead='Twin Springs Trailhead',
              hike_type='out_and_back',
              distance=4.4, elevation=1000, high_point=4770,
              difficulty_level='1moderate')
    add_hikes(name='Trail of Two Forests Loop Hike',
              trailhead='Trail of Two Forests Trailhead',
              hike_type='loop',
              distance=0.3, elevation=30, high_point=1895,
              difficulty_level='0easy')
    add_hikes(name='Bells Mountain Hike',
              trailhead='Moulton Falls Lower Trailhead',
              hike_type='out_and_back',
              distance=15.6, elevation=3040, high_point=1690,
              difficulty_level='2difficult')
    add_hikes(name='Lookout Mountain Hike',
              trailhead='Mother Lode Mine Trailhead',
              hike_type='out_and_back',
              distance=3.4, elevation=1045,
              difficulty_level='1moderate')
    add_hikes(name='Cultus Lake from Cultus Creek Campground Hike',
              trailhead='Cultus Creek Campground Trailhead',
              hike_type='out_and_back',
              distance=4.8, elevation=1010,
              difficulty_level='1moderate')
    add_hikes(name='Steins Pillar Hike',
              trailhead='Steins Pillar Trailhead',
              hike_type='out_and_back',
              distance=4, elevation=680,
              difficulty_level='1moderate')
    add_hikes(name='Soda Peaks Lake West Hike',
              trailhead='Soda Peaks Trailhead',
              hike_type='out_and_back',
              distance=4.4, elevation=1270, high_point=4780,
              difficulty_level='1moderate')
    add_hikes(name='Cedar Flats Hike',
              trailhead='Opal Creek Trailhead',
              hike_type='out_and_back',
              distance=10.5, elevation=500,
              difficulty_level='1moderate')
    add_hikes(name='Pilot Rock Hike',
              trailhead='Pilot Rock Trailhead',
              hike_type='out_and_back',
              distance=2.8, elevation=1010,
              difficulty_level='1moderate')
    add_hikes(name='Mirror Lake Hike',
              trailhead='Mirror Lake Trailhead',
              distance=2.9, elevation=780, high_point=4100,
              difficulty_level='0easy')
    add_hikes(name='Rooster Rock via High Ridge Trail Hike',
              trailhead='Old Bridge Trailhead',
              hike_type='out_and_back',
              distance=11.5, elevation=3770, high_point=4600,
              difficulty_level='2difficult')
    add_hikes(name='Blue Horse Loop Hike',
              trailhead='Blue Lake Trailhead',
              hike_type='loop',
              distance=5.2, elevation=560, high_point=3985,
              difficulty_level='0easy')
    add_hikes(name='Junction Lake from Cultus Creek Campground Hike',
              trailhead='Cultus Creek Campground Trailhead',
              hike_type='out_and_back',
              distance=8.4, elevation=1310,
              difficulty_level='1moderate')
    add_hikes(name='Opal Lake Hike',
              trailhead='Opal Lake Trailhead',
              hike_type='out_and_back',
              distance=0.8, elevation=400,
              difficulty_level='0easy')
    add_hikes(name='Echo Basin Hike',
              trailhead='Echo Basin Trailhead',
              hike_type='out_and_back',
              distance=2.0, elevation=400,
              difficulty_level='0easy')
    add_hikes(name='Fairy Falls Hike',
              trailhead='Wahkeena Trailhead',
              distance=2.0, elevation=800,
              difficulty_level='1moderate')
    add_hikes(name='Aldrich Butte Hike',
              trailhead='Aldrich Butte Trailhead',
              hike_type='out_and_back',
              distance=3.2, elevation=1070,
              difficulty_level='1moderate')
    add_hikes(name='Mitchell Point Hike',
              trailhead='Mitchell Point Trailhead',
              hike_type='out_and_back',
              distance=2.6, elevation=1270,
              difficulty_level='1moderate')
    add_hikes(name='Lewis River Waterfall Hike',
              trailhead='Lower Lewis River Falls Trailhead',
              hike_type='out_and_back',
              distance=6.6, elevation=320,
              difficulty_level='1moderate')
    add_hikes(name='Lacamas Park Lily Field Hike',
              trailhead='Lacamas Park Trailhead',
              hike_type='out_and_back',
              distance=2.3, elevation=100,
              difficulty_level='1moderate')
    add_hikes(name='Muddy Fork Hike',
              trailhead='Top Spur Trailhead',
              distance=6.2, elevation=800, high_point=4400,
              difficulty_level='1moderate')
    add_hikes(name='Battle Ground Lake Loop Hike',
              trailhead='Battle Ground Lake Trailhead',
              hike_type='loop',
              distance=0.9, elevation=20,
              difficulty_level='0easy')
    add_hikes(name='Multnomah-Wahkeena Loop Hike',
              trailhead='Multnomah Falls Trailhead',
              distance=4.9, elevation=1600,
              difficulty_level='1moderate')
    add_hikes(name='Wygant Peak Hike',
              trailhead='Mitchell Point Trailhead',
              hike_type='out_and_back',
              distance=6.0, elevation=1200,
              difficulty_level='1moderate')
    add_hikes(name='Kiwa Trail Loop Hike',
              trailhead='Kiwa Trailhead',
              hike_type='loop',
              distance=1.2, elevation=0, high_point=15,
              difficulty_level='0easy')
    add_hikes(name='East Zigzag from Devil Canyon Hike',
              trailhead='South Burnt Lake Trailhead',
              hike_type='out_and_back',
              distance=8.0, elevation=1670,
              difficulty_level='2difficult')
    add_hikes(name='Twin Lakes via Whetstone Ridge Hike',
              trailhead='Whetstone Trailhead',
              hike_type='out_and_back',
              distance=15.8, high_point=4535, elevation=2595,
              difficulty_level='2difficult')
    add_hikes(name='Flag Point via Lookout Mountain Hike',
              trailhead='High Prairie Trailhead',
              hike_type='out_and_back',
              distance=11.4, elevation=2340, high_point=6525,
              difficulty_level='1moderate')
    add_hikes(name='Olallie Meadows-Olallie Lake Loop Hike',
              trailhead='Olallie Meadows Trailhead',
              hike_type='loop',
              distance=11.9, elevation=1895, high_point=5395,
              difficulty_level='1moderate')
    add_hikes(name='Table Mountain from Aldrich Butte Trailhead Hike',
              trailhead='Aldrich Butte Trailhead',
              hike_type='out_and_back',
              distance=8.0, elevation=3350,
              difficulty_level='2difficult')
    add_hikes(name='Olallie North Loop Hike',
              trailhead='Lower Lake Trailhead',
              hike_type='loop',
              distance=5.6, elevation=955, high_point=5395,
              difficulty_level='1moderate')
    add_hikes(name='Gnarl Ridge from Hood River Meadows Hike',
              trailhead='Hood River Meadows Trailhead',
              distance=8.9, elevation=2460, high_point=6860,
              difficulty_level='2difficult')
    add_hikes(name='Catherine Creek Universal Access Hike',
              trailhead='Catherine Creek Trailhead',
              hike_type='loop',
              distance=1.2, elevation=100,
              difficulty_level='0easy')
    add_hikes(name='Huffman Peak Loop Hike',
              trailhead='Siouxon Trailhead',
              hike_type='loop',
              distance=13.3, elevation=4205, high_point=4106,
              difficulty_level='2difficult')
    add_hikes(name='Powell Butte Perimeter Loop Hike',
              trailhead='Powell Butte Main Trailhead',
              hike_type='loop',
              distance=3.3, elevation=500,
              difficulty_level='1moderate')
    add_hikes(name='Junction Lake Hike',
              trailhead='East Crater Trailhead',
              distance=5.0,
              hike_type='out_and_back',
              elevation=725, high_point=4780,
              difficulty_level='0easy')
    add_hikes(name='Sheepshead Rock Hike',
              trailhead='Twin Springs Trailhead',
              hike_type='out_and_back',
              distance=3.2, elevation=840, high_point=4484,
              difficulty_level='0easy')
    add_hikes(name='Plaza Lake Hike',
              trailhead='Plaza Lake Trailhead',
              hike_type='out_and_back',
              distance=1.4, elevation=560, high_point=4225,
              difficulty_level='0easy')
    add_hikes(name='Indian Point Loop Hike',
              trailhead='Herman Creek Trailhead',
              hike_type='loop',
              distance=7.6, elevation=2800)
    add_hikes(name='Discovery Trail Traverse Hike',
              trailhead='Ilwaco Waterfront Trailhead',
              hike_type='out_and_back',
              distance=8.2, elevation=280, high_point=175,
              difficulty_level='1moderate')
    add_hikes(name='Gumjuwac-Badger Lake Loop Hike',
              trailhead='Gumjuwac Trailhead',
              hike_type='lollipop',
              distance=11.8, elevation=3155, high_point=5345,
              difficulty_level='1moderate')
    add_hikes(name='Spray Park Hike',
              trailhead='Mowich Lake Trailhead',
              hike_type='out_and_back',
              distance=7.4, elevation=2610, high_point=6340,
              difficulty_level='1moderate')
    add_hikes(name='Rooster Rock via Table Rock Hike',
              trailhead='Table Rock Trailhead',
              hike_type='out_and_back',
              distance=10.1, elevation=2780, high_point=4881,
              difficulty_level='1moderate')
    add_hikes(name='Old Holgate Hike',
              trailhead='Powell Butte Main Trailhead',
              hike_type='out_and_back',
              distance=2.5, elevation=310,
              difficulty_level='0easy')
    add_hikes(name='Paradise Park via Burnt Lake Hike',
              trailhead='North Burnt Lake Trailhead',
              hike_type='out_and_back',
              distance=15.6, elevation=3400,
              difficulty_level='2difficult')
    add_hikes(name='Arch Cape to Short Sand Beach Hike',
              trailhead='Shingle Mill Trailhead',
              hike_type='out_and_back',
              distance=15.9, elevation=2750, high_point=990,
              difficulty_level='2difficult')
    add_hikes(name='Oaks Bottom Loop Hike',
              trailhead='Sellwood Park Trailhead',
              hike_type='loop',
              distance=2.3, elevation=125, high_point=130,
              difficulty_level='0easy')
    add_hikes(name='Grizzly Peak Hike',
              trailhead='Grizzly Peak Trailhead',
              hike_type='loop',
              distance=5.4,
              difficulty_level='1moderate')
    add_hikes(name='Willard Springs Loop Hike',
              trailhead='Willard Springs Trailhead',
              hike_type='loop',
              distance=2.3, elevation=55, high_point=1865,
              difficulty_level='0easy')
    add_hikes(name='Big Tree Loop Hike',
              trailhead='Oregon Caves Trailhead',
              hike_type='loop',
              distance=3.7, elevation=1380, high_point=5160,
              difficulty_level='1moderate')
    add_hikes(name='Yaquina Head Hike',
              trailhead='Yaquina Head Interpretive Center Trailhead',
              hike_type='out_and_back',
              distance=3.4, elevation=490, high_point=380,
              difficulty_level='0easy')
    add_hikes(name='Castle Canyon Hike',
              trailhead='West Zigzag Trailhead',
              hike_type='out_and_back',
              distance=2.2, elevation=840, high_point=2440,
              difficulty_level='0easy')
    add_hikes(name='Neahkahnie Mountain from South Hike',
              trailhead='South Neahkahnie Mountain Trailhead',
              hike_type='out_and_back',
              distance=3.0, elevation=840,
              difficulty_level='1moderate')
    add_hikes(name='Welcome Lakes Loop Hike',
              trailhead='Elk Lake Creek Trail Northern Trailhead',
              hike_type='lollipop',
              distance=13.8, high_point=5190, elevation=3440,
              difficulty_level='2difficult')
    add_hikes(name='Columbia River Dike Hike',
              trailhead='Steamboat Landing Trailhead',
              hike_type='out_and_back',
              distance=6.4, elevation=30, high_point=20,
              difficulty_level='0easy')
    add_hikes(name='Serene Lake Hike',
              trailhead='Frazier Trailhead',
              hike_type='out_and_back',
              distance=6.6, elevation=900,
              difficulty_level='1moderate')
    add_hikes(name='Pool of the Winds Hike',
              trailhead='Hamilton Mountain Trailhead',
              hike_type='out_and_back',
              distance=2.2, elevation=700)
    add_hikes(name='Council Crest Hike',
              trailhead='Marquam Nature Park Shelter Trailhead',
              hike_type='out_and_back',
              distance=3.3, elevation=820,
              difficulty_level='1moderate')
    add_hikes(name='Adams Glacier Meadows Hike',
              trailhead='Killen Creek Trailhead',
              distance=8.2, elevation=2250,
              difficulty_level='1moderate')
    add_hikes(name='Woodburn Falls Hike',
              trailhead='Lacamas Park Trailhead',
              hike_type='out_and_back',
              distance=2, elevation=200,
              difficulty_level='0easy')
    add_hikes(name='Hummocks Loop Hike',
              trailhead='Hummocks Trailhead',
              hike_type='loop',
              distance=2.7, elevation=100, high_point=2540,
              difficulty_level='0easy')
    add_hikes(name='Wahtum Lake via Ruckel Creek Hike',
              trailhead='Eagle Creek Trailhead',
              hike_type='out_and_back',
              distance=29.8, elevation=6270,
              difficulty_level='2difficult')
    add_hikes(name='Neskowin Beach to Porter Point Hike',
              trailhead='Neskowin Beach Trailhead',
              hike_type='out_and_back',
              distance=9.6, elevation=15, high_point=15,
              difficulty_level='1moderate')
    add_hikes(name='Powell Butte Universal Access Hike',
              trailhead='Powell Butte Main Trailhead',
              hike_type='out_and_back',
              distance=1.6, elevation=200,
              difficulty_level='1moderate')
    add_hikes(name='Lookout Mountain-Gumjuwac Creek Loop Hike',
              trailhead='High Prairie Trailhead',
              hike_type='loop',
              distance=14.2, elevation=3835, high_point=6525,
              difficulty_level='2difficult')
    add_hikes(name='Deschutes River from Macks Canyon Hike',
              trailhead='Macks Canyon Trailhead',
              distance=23.6, elevation=350,
              difficulty_level='2difficult')
    add_hikes(name='Round Lake Loop Hike',
              trailhead='Lacamas Park Trailhead',
              hike_type='loop',
              distance=1.5, elevation=100,
              difficulty_level='0easy')
    add_hikes(name='Beacon Rock Hike',
              trailhead='Beacon Rock Trailhead',
              hike_type='out_and_back',
              distance=1.8, elevation=680,
              difficulty_level='1moderate')
    add_hikes(name='Coyote Wall Hike',
              trailhead='Coyote Wall Trailhead',
              hike_type='lollipop',
              distance=7.8, high_point=1895, elevation=1775,
              difficulty_level='1moderate')
    add_hikes(name='Cache Meadows via Cripple Creek Loop Hike',
              trailhead='Cripple Creek Trailhead',
              hike_type='lollipop',
              distance=11.6, elevation=2845, high_point=4395,
              difficulty_level='1moderate')
    add_hikes(name='Square Lake Hike',
              trailhead='Santiam Pass Trailhead',
              hike_type='out_and_back',
              distance=4.4,
              difficulty_level='0easy')
    add_hikes(name='Scout Camp Trail Loop Hike',
              trailhead='Scout Camp Trailhead',
              hike_type='loop',
              distance=2.3, elevation=700,
              difficulty_level='1moderate')
    add_hikes(name='Foggy Flat Hike',
              trailhead='Killen Creek Trailhead',
              distance=22.2, elevation=1550,
              difficulty_level='1moderate')
    add_hikes(name='Devil\'s Punchbowl Hike',
              trailhead="Devil's Punchbowl Trailhead",
              hike_type='out_and_back',
              distance=0.6, elevation=50,
              difficulty_level='0easy')
    add_hikes(name='Painted Hills Overlook Hike',
              trailhead='Painted Hills Trailhead',
              hike_type='out_and_back',
              distance=1.0, elevation=140,
              difficulty_level='0easy')
    add_hikes(name='Natural Arch Hike',
              trailhead='Natural Arch Trailhead',
              hike_type='out_and_back',
              distance=1.0, high_point=3860, elevation=460,
              difficulty_level='0easy')
    add_hikes(name='Bonney Butte Hike',
              trailhead='Bonney Butte Trailhead',
              hike_type='out_and_back',
              distance=1.2, elevation=220, high_point=5580,
              difficulty_level='0easy')
    add_hikes(name='Herman Creek-Wyeth Hike',
              trailhead='Herman Creek Trailhead',
              hike_type='out_and_back',
              distance=10.8, high_point=960, elevation=2175,
              difficulty_level='1moderate')
    add_hikes(name='Basin Lakes Loop Hike',
              trailhead='Falls Creek Horse Camp Trailhead',
              distance=9.1,
              hike_type='loop',
              elevation=1795, high_point=5005,
              difficulty_level='1moderate')
    add_hikes(name='Paradise Park from Timberline Lodge Hike',
              trailhead='Timberline Lodge Trailhead',
              distance=12.1, elevation=2300, high_point=6080,
              difficulty_level='2difficult')
    add_hikes(name='Tanner Cutoff Loop Hike',
              trailhead='Tooth Rock Trailhead',
              hike_type='out_and_back',
              distance=14.4, elevation=3700,
              difficulty_level='2difficult')
    add_hikes(name='Columbian White-tailed Deer Refuge Loop Hike',
              trailhead='Indian Jack Slough Trailhead',
              hike_type='loop',
              distance=6.1, elevation=10, high_point=20,
              difficulty_level='0easy')
    add_hikes(name='Battle Ax Loop Hike',
              trailhead='Bagby Trailhead',
              hike_type='loop',
              distance=6.0, elevation=1765, high_point=5558,
              difficulty_level='1moderate')
    add_hikes(name='Rock of Ages Loop Hike',
              trailhead='Horsetail Falls Trailhead',
              hike_type='loop',
              distance=10.0, elevation=3000,
              difficulty_level='2difficult')
    add_hikes(name='Fort to Sea Hike',
              trailhead='Sunset Beach Trailhead',
              distance=5, elevation=160,
              difficulty_level='1moderate')
    add_hikes(name='Cape Disappointment Hike',
              trailhead='Waikiki Beach Trailhead',
              hike_type='out_and_back',
              distance=2.9, elevation=385, high_point=170,
              difficulty_level='0easy')
    add_hikes(name='Ozette to Rialto Beach Hike',
              trailhead='Ozette Trailhead',
              distance=20, elevation=200,
              difficulty_level='2difficult')
    add_hikes(name='Paradise Park from Ramona Falls Hike',
              trailhead='Ramona Falls Trailhead',
              distance=14.4,
              hike_type='out_and_back',
              elevation=3400,
              difficulty_level='2difficult')
    add_hikes(name='Kinzel Lake Hike',
              trailhead='Salmon River Trailhead',
              hike_type='out_and_back',
              distance=17.2, elevation=3455, high_point=4315,
              difficulty_level='2difficult')
    add_hikes(name='Washington Park Loop Hike',
              trailhead='Sacajawea Statue Trailhead',
              hike_type='loop',
              distance=3.9, elevation=585, high_point=850,
              difficulty_level='0easy')
    add_hikes(name='Cape Falcon Hike',
              trailhead='Cape Falcon Trailhead',
              hike_type='out_and_back',
              distance=4.8, elevation=160,
              difficulty_level='0easy')
    add_hikes(name='Netarts Spit Hike',
              trailhead='Cape Lookout Day Use Trailhead',
              hike_type='out_and_back',
              distance=11.2, elevation=60, high_point=35,
              difficulty_level='1moderate')
    add_hikes(name='Jefferson Park via Park Ridge Hike',
              trailhead='Breitenbush Trailhead',
              distance=11.2, elevation=2500,
              difficulty_level='1moderate')
    add_hikes(name='Zigzag Overlook from Timberline Lodge Hike',
              trailhead='Timberline Lodge Trailhead',
              distance=4.4, elevation=400, high_point=6000,
              difficulty_level='0easy')
    add_hikes(name='Wind Mountain Hike',
              trailhead='Wind Mountain Trailhead',
              hike_type='out_and_back',
              distance=2.5, elevation=1171,
              difficulty_level='1moderate')
    add_hikes(name='Firelane 15 Hike',
              trailhead='Firelane 15 Gate Trailhead',
              hike_type='loop',
              distance=4.2,
              difficulty_level='1moderate')
    add_hikes(name='Tanner-Eagle Traverse Hike',
              trailhead='Tooth Rock Trailhead',
              hike_type='point_to_point',
              distance=23.6, elevation=4500,
              difficulty_level='2difficult')
    add_hikes(name='Trillium Lake Loop Hike',
              trailhead='Trillium Lake Trailhead',
              hike_type='loop',
              distance=1.9, elevation=10, high_point=3610,
              difficulty_level='0easy')
    add_hikes(name='Angel\'s Rest-Devil\'s Rest Loop Hike',
              trailhead="Angel's Rest Trailhead",
              hike_type='loop',
              distance=10.9, elevation=2770,
              difficulty_level='1moderate')
    add_hikes(name='Trail around Three Sisters Hike',
              trailhead='Lava Lake Trailhead',
              distance=48.1, elevation=5800, high_point=7000,
              difficulty_level='2difficult')
    add_hikes(name='Hardy Ridge Loop Hike',
              trailhead='Hardy Ridge Equestrian Trailhead',
              hike_type='loop',
              distance=8.1, elevation=2200,
              difficulty_level='1moderate')
    add_hikes(name='Mount Hood Trail Loop Hike',
              trailhead='Ellis Street Trailhead',
              hike_type='loop',
              distance=2.0, elevation=340,
              difficulty_level='0easy')
    add_hikes(name='Yocum Ridge Hike',
              trailhead='Ramona Falls Trailhead',
              distance=16, elevation=3600,
              difficulty_level='2difficult')
    add_hikes(name='Abiqua Falls Hike',
              trailhead='Abiqua Falls Trailhead',
              hike_type='out_and_back',
              distance=0.8, elevation=180,
              difficulty_level='1moderate')
    add_hikes(name='Linnton Loop Hike',
              trailhead='Linnton Trailhead',
              hike_type='loop',
              distance=5.2, elevation=930, high_point=880,
              difficulty_level='1moderate')
    add_hikes(name='Laurel Hill Chute Loop Hike',
              trailhead='Laurel Hill Chute Trailhead',
              hike_type='loop',
              distance=0.6, elevation=230, high_point=3380,
              difficulty_level='0easy')
    add_hikes(name='Klickitat Trail=Lyle to Klickitat Hike',
              trailhead='Lyle Trailhead',
              hike_type='out_and_back',
              distance=13.0, elevation=340, high_point=465,
              difficulty_level='1moderate')
    add_hikes(name='Lemei Rock via Lemei Trail Hike',
              trailhead='Lemei Trailhead',
              hike_type='out_and_back',
              distance=9.2, elevation=2285, high_point=5925,
              difficulty_level='1moderate')
    add_hikes(name='Buck Peak Hike',
              trailhead='Lost Lake Trailhead',
              hike_type='out_and_back',
              distance=15.8, elevation=2500,
              difficulty_level='1moderate')
    add_hikes(name='Hunchback Mountain Hike',
              trailhead='Hunchback Mountain Trailhead',
              hike_type='out_and_back',
              distance=9.0, elevation=3270, high_point=4033,
              difficulty_level='1moderate')
    add_hikes(name='Old Salmon River Hike',
              trailhead='Salmon River Trailhead',
              hike_type='out_and_back',
              distance=5.0, elevation=200, high_point=1640,
              difficulty_level='0easy')
    add_hikes(name='Veda Lake Hike',
              trailhead='Fir Tree Trailhead',
              hike_type='out_and_back',
              distance=2.8, elevation=660, high_point=4680,
              difficulty_level='0easy')
    add_hikes(name='Gnarl Ridge from Cloud Cap Hike',
              trailhead='Cloud Cap Trailhead',
              hike_type='out_and_back',
              distance=8.4, elevation=2420, high_point=7300,
              difficulty_level='2difficult')
    add_hikes(name='Wahclella Falls Hike',
              trailhead='Wahclella Falls Trailhead',
              hike_type='out_and_back',
              distance=2.0, elevation=0,
              difficulty_level='0easy')
    add_hikes(name='La Center Bottoms Hike',
              trailhead='La Center Trailhead',
              hike_type='out_and_back',
              distance=2.2, elevation=10,
              difficulty_level='0easy')
    add_hikes(name='Neahkahnie Mountain from North Hike',
              trailhead='North Neahkahnie Mountain Trailhead',
              hike_type='out_and_back',
              distance=5.0, elevation=1450,
              difficulty_level='1moderate')
    add_hikes(name='Sand Point Cape Alava Hike',
              trailhead='Ozette Trailhead',
              distance=9, elevation=400,
              difficulty_level='1moderate')
    add_hikes(name='Owl Point from Vista Ridge Hike',
              trailhead='Vista Ridge Trailhead',
              hike_type='out_and_back',
              distance=4.0, elevation=500,
              difficulty_level='1moderate')
    add_hikes(name='Washougal River Greenway Loop Hike',
              trailhead='Baz Riverfront Park Trailhead',
              hike_type='out_and_back',
              distance=2.6, elevation=70, high_point=50,
              difficulty_level='0easy')
    add_hikes(name='Heart Lake Hike',
              trailhead='Hellroaring Meadows Trailhead',
              hike_type='out_and_back',
              distance=2.0, elevation=150, high_point=5380,
              difficulty_level='0easy')
    add_hikes(name='Upper McCord Creek Falls Hike',
              trailhead='John B Yeon Trailhead',
              hike_type='out_and_back',
              distance=2.2, elevation=400,
              difficulty_level='0easy')
    add_hikes(name='Goat Lake Loop Hike',
              trailhead='Berry Patch Trailhead',
              distance=12.8, elevation=2590,
              difficulty_level='2difficult')
    add_hikes(name='Cast Creek Hike',
              trailhead='Cast Creek Trailhead',
              hike_type='out_and_back',
              distance=12.4, elevation=2970,
              difficulty_level='1moderate')
    add_hikes(name='Marquam Trail to Council Crest Hike',
              trailhead='Terwilliger Trailhead',
              hike_type='out_and_back',
              distance=5.8, elevation=1100,
              difficulty_level='1moderate')
    add_hikes(name='Lower Starvation Loop Hike',
              trailhead='Starvation Creek Trailhead',
              hike_type='loop',
              distance=3.0, elevation=1280,
              difficulty_level='1moderate')
    add_hikes(name='Munra Point from Yeon Trailhead Hike',
              trailhead='John B Yeon Trailhead',
              hike_type='out_and_back',
              distance=7.4, elevation=2270,
              difficulty_level='2difficult')
    add_hikes(name='Tilly Jane Hike',
              trailhead='Cloud Cap Trailhead',
              hike_type='loop',
              distance=3.0, elevation=1100, high_point=6800,
              difficulty_level='1moderate')
    add_hikes(name='Sand Lake-Cape Kiwanda Hike',
              trailhead='Tierra del Mar Trailhead',
              hike_type='out_and_back',
              distance=8.2, elevation=240, high_point=220,
              difficulty_level='1moderate')
    add_hikes(name='Fort Rains Hike',
              trailhead='Icehouse Lake Trailhead',
              hike_type='out_and_back',
              distance=1.6, elevation=40,
              difficulty_level='0easy')
    add_hikes(name='Ice Lake Hike',
              trailhead='Wallowa Lake Trailhead',
              hike_type='out_and_back',
              distance=15.4, elevation=3380, high_point=7900,
              difficulty_level='2difficult')
    add_hikes(name='Catherine Creek West Loop Hike',
              trailhead='Catherine Creek Trailhead',
              hike_type='loop',
              distance=2.5, elevation=700,
              difficulty_level='1moderate')
    add_hikes(name='Burnt Bridge Creek Hike',
              trailhead='Stewart Glen Trailhead',
              hike_type='out_and_back',
              distance=8.1, high_point=310, elevation=180,
              difficulty_level='0easy')
    add_hikes(name='Horsethief Butte Hike',
              trailhead='Horsethief Butte Trailhead',
              hike_type='out_and_back',
              distance=2.1, high_point=498, elevation=250,
              difficulty_level='0easy')
    add_hikes(name='Mount Adams Summit Hike',
              trailhead='South Climb Trailhead',
              distance=12.4, elevation=6740, high_point=12276,
              difficulty_level='2difficult')
    add_hikes(name='Boulder Ridge to Huckleberry Mountain Hike',
              trailhead='Wildwood Recreation Area Winter Trailhead',
              hike_type='out_and_back',
              distance=10.6, high_point=4300, elevation=3450,
              difficulty_level='2difficult')
    add_hikes(name='Enid Lake via Pioneer Bridle Trail Hike',
              trailhead='Pioneer Bridle Laurel Hill Trailhead',
              hike_type='out_and_back',
              distance=9.5, elevation=1570, high_point=3695,
              difficulty_level='1moderate')
    add_hikes(name='Devil\'s Peak from Hunchback Mountain Hike',
              trailhead='Hunchback Mountain Trailhead',
              hike_type='out_and_back',
              distance=15.4, elevation=5940, high_point=5045,
              difficulty_level='2difficult')
    add_hikes(name='Sheppard\'s Dell Hike',
              trailhead="Sheppard's Dell Trailhead",
              hike_type='out_and_back',
              distance=0.2, elevation=50,
              difficulty_level='0easy')
    add_hikes(name='Ferry Springs Hike',
              trailhead='Lower Deschutes Trailhead',
              distance=4.4, elevation=560,
              difficulty_level='1moderate')
    add_hikes(name='Catherine Creek Arch Loop Hike',
              trailhead='Catherine Creek Trailhead',
              hike_type='loop',
              distance=2, elevation=500,
              difficulty_level='0easy')
    add_hikes(name='Gold Butte Lookout Hike',
              trailhead='Gold Butte Trailhead',
              hike_type='out_and_back',
              distance=3.2, elevation=800,
              difficulty_level='1moderate')
    add_hikes(name='Silver Star via Starway Trail Hike',
              trailhead='Starway Trailhead',
              hike_type='out_and_back',
              distance=9.8, elevation=2790,
              difficulty_level='2difficult')
    add_hikes(name='Two Chiefs Trail Hike',
              trailhead='Aldrich Butte Trailhead',
              hike_type='out_and_back',
              distance=7.8, elevation=1270,
              difficulty_level='1moderate')
    add_hikes(name='Silver Star via Sturgeon Rock Loop Hike',
              trailhead='Grouse Vista Trailhead',
              hike_type='loop',
              distance=8.5, elevation=2040,
              difficulty_level='1moderate')
    add_hikes(name='East Zigzag from Lost Creek Hike',
              trailhead='North Burnt Lake Trailhead',
              distance=9.4, elevation=2300,
              difficulty_level='2difficult')
    add_hikes(name='Larch Mountain via Oneonta Trail Hike',
              trailhead='Upper Oneonta Trailhead',
              hike_type='out_and_back',
              distance=17.2, elevation=4400,
              difficulty_level='2difficult')
    add_hikes(name='Salmon Mountain Hike',
              trailhead='Twin Springs Trailhead',
              hike_type='out_and_back',
              distance=10.0, elevation=1960, high_point=4484,
              difficulty_level='1moderate')
    add_hikes(name='Green Point Mountain Loop Hike',
              trailhead='Rainy Lake Trailhead',
              hike_type='loop',
              distance=8.0, high_point=4737, elevation=1275,
              difficulty_level='1moderate')
    add_hikes(name='Wizard Falls Loop Hike',
              trailhead='Lower Bridge Trailhead',
              distance=6, elevation=300, high_point=2900,
              difficulty_level='1moderate')
    add_hikes(name='Lake Sacajawea Loop Hike',
              trailhead='Nichols Boulevard Trailhead',
              hike_type='loop',
              distance=3.6, elevation=35, high_point=15,
              difficulty_level='0easy')
    add_hikes(name='Wahtum Lake via Herman Creek Hike',
              trailhead='Herman Creek Trailhead',
              hike_type='out_and_back',
              distance=22.2, elevation=5070,
              difficulty_level='2difficult')
    add_hikes(name='Whipple Creek Loop Hike',
              trailhead='Whipple Creek Trailhead',
              hike_type='loop',
              distance=3.1, high_point=195, elevation=300,
              difficulty_level='0easy')
    add_hikes(name='Jean Lake Hike',
              trailhead='Jean Lake Trailhead',
              hike_type='out_and_back',
              distance=0.8, elevation=240, high_point=5560,
              difficulty_level='0easy')
    add_hikes(name='Grassy Knoll Hike',
              trailhead='Grassy Knoll Trailhead',
              hike_type='out_and_back',
              distance=4.2, elevation=1280, high_point=3648,
              difficulty_level='1moderate')
    add_hikes(name='Dog Mountain Loop Hike',
              trailhead='Dog Mountain Trailhead',
              hike_type='loop',
              distance=7.4, elevation=2800,
              difficulty_level='2difficult')
    add_hikes(name='Mount Beachie Hike',
              trailhead='Bagby Trailhead',
              hike_type='loop',
              distance=5.6, elevation=1350, high_point=5185,
              difficulty_level='1moderate')
    add_hikes(name='Indian Racetrack via the PCT Hike',
              trailhead='Crest Camp Trailhead',
              distance=8.0,
              hike_type='out_and_back',
              elevation=850, high_point=4285,
              difficulty_level='1moderate')
    add_hikes(name='Blue Lake Hike',
              trailhead='Thomas Lake Trailhead',
              hike_type='out_and_back',
              distance=6.6, elevation=700,
              difficulty_level='1moderate')
    add_hikes(name='Wauna Viewpoint from Eagle Creek Hike',
              trailhead='Eagle Creek Trailhead',
              hike_type='out_and_back',
              distance=3.6, elevation=1050,
              difficulty_level='1moderate')
    add_hikes(name='Bridal Veil Loop Hike',
              trailhead='Bridal Veil Trailhead',
              hike_type='loop',
              distance=0.5, elevation=0,
              difficulty_level='0easy')
    add_hikes(name='Soda Peaks Lake via Trapper Creek Hike',
              trailhead='Trapper Creek Trailhead',
              hike_type='out_and_back',
              distance=10.2, elevation=3110, high_point=3785,
              difficulty_level='2difficult')
    add_hikes(name='Ramona Falls Hike',
              trailhead='Ramona Falls Trailhead',
              distance=7.0,
              hike_type='loop',
              elevation=1100,
              difficulty_level='1moderate')
    add_hikes(name='Crystal Springs-Reed Canyon Hike',
              trailhead='Crystal Springs Trailhead',
              hike_type='out_and_back',
              distance=2.4, elevation=145, high_point=125,
              difficulty_level='0easy')
    add_hikes(name='Silver Star Hike',
              trailhead='Silver Star Trailhead',
              hike_type='loop',
              distance=5.6, high_point=4360, elevation=1240,
              difficulty_level='1moderate')
    add_hikes(name='Tanner Butte Hike',
              trailhead='Tooth Rock Trailhead',
              hike_type='out_and_back',
              distance=18.0, elevation=4450,
              difficulty_level='2difficult')
    add_hikes(name='Elk Cove from Pinnacle Ridge Hike',
              trailhead='Pinnacle Ridge Trailhead',
              distance=8.4, elevation=2490, high_point=5800,
              difficulty_level='1moderate')
    add_hikes(name='Cannery Hill Hike',
              trailhead='Cannery Hill Trailhead',
              hike_type='out_and_back',
              distance=1.4, elevation=230, high_point=290,
              difficulty_level='0easy')
    add_hikes(name='Eightmile Creek Loop Hike',
              trailhead='Bottle Prairie Trailhead',
              hike_type='loop',
              distance=6.2, elevation=1985, high_point=4915,
              difficulty_level='1moderate')
    add_hikes(name='Pittock Mansion Hike',
              trailhead='Lower Macleay Park Trailhead',
              hike_type='out_and_back',
              distance=5, elevation=900,
              difficulty_level='1moderate')
    add_hikes(name='Umbrella Falls Loop Hike',
              trailhead='Hood River Meadows Trailhead',
              hike_type='out_and_back',
              distance=4.6, elevation=820, high_point=5240,
              difficulty_level='0easy')
    add_hikes(name='Rooster Rock Loop Hike',
              trailhead='Rooster Rock Trailhead',
              hike_type='loop',
              distance=2.7, elevation=240,
              difficulty_level='0easy')
    add_hikes(name='Mount Saint Helens via Butte Camp Hike',
              trailhead='Red Rock Pass Trailhead',
              hike_type='out_and_back',
              distance=13.2, high_point=8365, elevation=5305,
              difficulty_level='2difficult')
    add_hikes(name='Rocky Top Hike',
              trailhead='Rocky Top Trailhead',
              hike_type='out_and_back',
              distance=1.0, high_point=5014, elevation=705,
              difficulty_level='0easy')
    add_hikes(name='Zigzag Overlook from Hidden Lake Hike',
              trailhead='Hidden Lake Trailhead',
              distance=12, elevation=2800, high_point=5850,
              difficulty_level='2difficult')
    add_hikes(name='Horseshoe Ridge Loop Hike',
              trailhead='Siouxon Trailhead',
              hike_type='loop',
              distance=10.9, elevation=3405, high_point=3480,
              difficulty_level='2difficult')
    add_hikes(name='Labyrinth Loop Hike',
              trailhead='Coyote Wall Trailhead',
              hike_type='loop',
              distance=5.8, elevation=1200,
              difficulty_level='1moderate')
    add_hikes(name='Lucia Falls Loop Hike',
              trailhead='Lucia Falls Trailhead',
              hike_type='loop',
              distance=1.1, elevation=20,
              difficulty_level='0easy')
    add_hikes(name='Augspurger Mountain Hike',
              trailhead='Dog Mountain Trailhead',
              hike_type='out_and_back',
              distance=12.6, elevation=4767,
              difficulty_level='2difficult')
    add_hikes(name='Tamanawas Falls Hike',
              trailhead='Polallie Trailhead',
              hike_type='out_and_back',
              distance=3.6, elevation=590,
              difficulty_level='0easy')
    add_hikes(name='Battle Creek Shelter Hike',
              trailhead='Elk Lake Creek Trail Northern Trailhead',
              hike_type='out_and_back',
              distance=9.8, elevation=500,
              difficulty_level='1moderate')
    add_hikes(name='Bald Mountain from Top Spur Hike',
              trailhead='Top Spur Trailhead',
              distance=2.0, elevation=550, high_point=4591,
              difficulty_level='0easy')
    add_hikes(name='Canyon Creek Meadow Hike',
              trailhead='Jack Lake Trailhead',
              distance=6.5, elevation=900,
              difficulty_level='1moderate')
    add_hikes(name='McCully Basin Hike',
              trailhead='McCully Trailhead',
              hike_type='out_and_back',
              distance=15.2, elevation=2360, high_point=8705,
              difficulty_level='1moderate')
    add_hikes(name='Lost Lake Butte Hike',
              trailhead='Lost Lake Trailhead',
              hike_type='out_and_back',
              distance=4.6, elevation=1270, high_point=4468,
              difficulty_level='1moderate')
    add_hikes(name='Lacamas Heritage Trail Hike',
              trailhead='Goodwin Road Trailhead',
              hike_type='out_and_back',
              distance=7.0, elevation=30, high_point=210,
              difficulty_level='0easy')
    add_hikes(name='West Zigzag Hike',
              trailhead='West Zigzag Trailhead',
              hike_type='out_and_back',
              distance=11, elevation=2900,
              difficulty_level='2difficult')
    add_hikes(name='Lancaster Falls Hike',
              trailhead='Starvation Creek Trailhead',
              hike_type='out_and_back',
              distance=1.8, elevation=160,
              difficulty_level='0easy')
    add_hikes(name='Short Beach Hike',
              trailhead='Short Beach Trailhead',
              hike_type='out_and_back',
              distance=1.4, high_point=95, elevation=95,
              difficulty_level='0easy')
    add_hikes(name='Nestucca Spit Loop Hike',
              trailhead='Bob Straub State Park Trailhead',
              hike_type='loop',
              distance=7.5, elevation=60, high_point=40,
              difficulty_level='1moderate')
    add_hikes(name='Aldrich Butte-Cedar Falls Loop Hike',
              trailhead='Dick Thomas Trailhead',
              hike_type='lollipop',
              distance=5.8, elevation=1770,
              difficulty_level='1moderate')
    add_hikes(name='Ape Cave Hike',
              trailhead='Ape Cave Trailhead',
              hike_type='out_and_back',
              distance=2.0, elevation=180, high_point=2485,
              difficulty_level='0easy')
    add_hikes(name='Paradise Park Hike',
              trailhead='Paradise Park Trailhead',
              distance=12.4, elevation=3000, high_point=5800,
              difficulty_level='2difficult')
    add_hikes(name='Boulder Lakes Hike',
              trailhead='Boulder Lake Trailhead',
              hike_type='loop',
              distance=6.3, elevation=1070, high_point=5409,
              difficulty_level='1moderate')
    add_hikes(name='Little Zigzag Falls Hike',
              trailhead='Little Zigzag Falls Trailhead',
              distance=0.6, elevation=50, high_point=3150,
              difficulty_level='0easy')
    add_hikes(name='Crane Prairie-Boulder Lakes Loop Hike',
              trailhead='Boulder Lake Trailhead',
              hike_type='loop',
              distance=8.7, elevation=1280, high_point=5485,
              difficulty_level='1moderate')
    add_hikes(name='Lost Lake Loop Hike',
              trailhead='Lost Lake Trailhead',
              hike_type='loop',
              distance=3.2, elevation=0,
              difficulty_level='0easy')
    add_hikes(name='Curly Creek Falls Hike',
              trailhead='Curly Creek Falls Trailhead',
              hike_type='out_and_back',
              distance=0.4, elevation=10,
              difficulty_level='0easy')
    add_hikes(name='Elk Lake Hike',
              trailhead='Elk Lake Creek Trail Northern Trailhead',
              hike_type='out_and_back',
              distance=17.8, elevation=1300,
              difficulty_level='2difficult')
    add_hikes(name='Mount Beachie via French Creek Ridge Hike',
              trailhead='French Creek Ridge Trailhead',
              hike_type='out_and_back',
              distance=8.2, elevation=2115, high_point=5190,
              difficulty_level='1moderate')
    add_hikes(name='Bull of the Woods via Pansy Lake Loop Hike',
              trailhead='Pansy Lake Trailhead',
              hike_type='loop',
              distance=7.5, high_point=5523, elevation=2100,
              difficulty_level='1moderate')
    add_hikes(name='Bear Lake Hike',
              trailhead='Upper Mount Defiance Trailhead',
              hike_type='out_and_back',
              distance=2.6, elevation=480, high_point=4100,
              difficulty_level='0easy')
    add_hikes(name='Whetstone Mountain Hike',
              trailhead='Whetstone Trailhead',
              hike_type='out_and_back',
              distance=4.8, high_point=4969, elevation=1360,
              difficulty_level='1moderate')
    add_hikes(name='Olallie and Monon Lakes Loop Hike',
              trailhead='Monon Lake Trailhead',
              hike_type='loop',
              distance=7.5, elevation=150, high_point=4970,
              difficulty_level='1moderate')
    add_hikes(name='Breitenbush Cascades Hike',
              trailhead='Breitenbush Cascades Trailhead',
              hike_type='out_and_back',
              distance=0.4, elevation=200,
              difficulty_level='0easy')
    add_hikes(name='Barlow Butte Hike',
              trailhead='Barlow Pass Trailhead',
              hike_type='out_and_back',
              distance=4, elevation=1100,
              difficulty_level='1moderate')
    add_hikes(name='Ponytail Falls Hike',
              trailhead='Horsetail Falls Trailhead',
              hike_type='out_and_back',
              distance=0.8, elevation=360,
              difficulty_level='0easy')
    add_hikes(name='Huckleberry Mountain via Bonanza Trail Hike',
              trailhead='Bonanza Trailhead',
              hike_type='out_and_back',
              distance=11.8, elevation=3485, high_point=4378,
              difficulty_level='2difficult')
    add_hikes(name='Salmon River Hike',
              trailhead='Salmon River Trailhead',
              hike_type='out_and_back)',
              distance=7.8, elevation=950, high_point=2490,
              difficulty_level='1moderate')
    add_hikes(name='Wauna Point Hike',
              trailhead='Tooth Rock Trailhead',
              hike_type='out_and_back',
              distance=9.4, elevation=3380,
              difficulty_level='1moderate')
    add_hikes(name='Wauna Viewpoint from Tooth Rock Hike',
              trailhead='Tooth Rock Trailhead',
              hike_type='out_and_back',
              distance=4, elevation=1050,
              difficulty_level='1moderate')
    add_hikes(name='Bonney Meadows to Boulder Lakes Hike',
              trailhead='Bonney Meadows Trailhead',
              hike_type='loop',
              distance=6.1, elevation=910, high_point=5409,
              difficulty_level='1moderate')
    add_hikes(name='Woods Park Loop Hike',
              trailhead='Woods Park Trailhead',
              hike_type='loop',
              distance=2.1, elevation=210, high_point=610,
              difficulty_level='0easy')
    add_hikes(name='A.G. Aiken Lava Bed Loop Hike',
              trailhead='Gotchen Creek South Trailhead',
              distance=14.7, elevation=3235, high_point=6440,
              difficulty_level='2difficult')
    add_hikes(name='Elk Cove Hike',
              trailhead='Elk Cove Trailhead',
              distance=10.2, elevation=2200, high_point=5460,
              difficulty_level='1moderate')
    add_hikes(name='Little North Fork Hike',
              trailhead='Little North Fork Trailhead',
              hike_type='out_and_back',
              distance=9, elevation=400,
              difficulty_level='1moderate')
    add_hikes(name='Big Creek-Forest Park Hike',
              trailhead='Fogarty Street Trailhead',
              hike_type='out_and_back',
              distance=3.6, elevation=560, high_point=265,
              difficulty_level='0easy')
    add_hikes(name='Phantom Natural Bridge Hike',
              trailhead='French Creek Ridge Trailhead',
              hike_type='out_and_back',
              distance=4.6, elevation=1540, high_point=4535,
              difficulty_level='1moderate')
    add_hikes(name='Oregon Caves Loop Hike',
              trailhead='Oregon Caves Trailhead',
              hike_type='loop',
              distance=1.2, elevation=300, high_point=4260,
              difficulty_level='0easy')
    add_hikes(name='Lacamas Creek Hike',
              trailhead='Lacamas Creek Trailhead',
              hike_type='out_and_back',
              distance=4.3, elevation=300,
              difficulty_level='0easy')
    add_hikes(name='Clackamas River Trail Hike',
              trailhead='Fish Creek Trailhead',
              hike_type='point_to_point',
              distance=7.8, elevation=450,
              difficulty_level='1moderate')
    add_hikes(name='Mist Falls Hike',
              trailhead='Mist Falls Trailhead',
              hike_type='out_and_back',
              distance=0.6, elevation=200,
              difficulty_level='1moderate')
    add_hikes(name='Indian Racetrack Hike',
              trailhead='Falls Creek Horse Camp Trailhead',
              distance=4.6,
              hike_type='out_and_back',
              elevation=760, high_point=4350,
              difficulty_level='0easy')
    add_hikes(name='Stacker Butte-Oak Spring Hike',
              trailhead='Stacker Butte Trailhead',
              hike_type='out_and_back',
              distance=7.8, high_point=3220, elevation=1535,
              difficulty_level='1moderate')
    add_hikes(name='Mosier Twin Tunnels Hike',
              trailhead='Mark Hatfield East Trailhead',
              hike_type='out_and_back',
              distance=8.5, high_point=530, elevation=1000,
              difficulty_level='1moderate')
    add_hikes(name='Sandy River Delta Hike',
              trailhead='Sandy River Delta Trailhead',
              hike_type='out_and_back',
              distance=4.2, elevation=100,
              difficulty_level='1moderate')
    add_hikes(name='Bonney Butte via Bonney Meadows Trail Hike',
              trailhead='Bonney Meadows Trailhead',
              hike_type='out_and_back',
              distance=7.1, elevation=2070, high_point=5580,
              difficulty_level='1moderate')
    add_hikes(name='West Fork Falls Hike',
              trailhead='Eastleg Road Trailhead',
              hike_type='out_and_back',
              distance=2.6, elevation=405, high_point=4800,
              difficulty_level='0easy')
    add_hikes(name='Bull of the Woods Lookout Hike',
              trailhead='Bull of the Woods Trailhead',
              hike_type='out_and_back',
              distance=6.4, high_point=5523, elevation=1250,
              difficulty_level='1moderate')
    add_hikes(name='Green Canyon-Salmon River Loop Hike',
              trailhead='Salmon River Trailhead',
              hike_type='loop',
              distance=15.6, elevation=4355, high_point=5045,
              difficulty_level='2difficult')
    add_hikes(name='Mill Creek Wilderness Loop Hike',
              trailhead='South Twin Pillars Trailhead',
              distance=26.9, elevation=3500,
              difficulty_level='2difficult')
    add_hikes(name='Moulton Falls Hike',
              trailhead='Hantwick Road Trailhead',
              hike_type='out_and_back',
              distance=5.9, elevation=260, high_point=595,
              difficulty_level='0easy')
    add_hikes(name='Oneonta Gorge Hike',
              trailhead='Oneonta Gorge Trailhead',
              hike_type='out_and_back',
              distance=1.0, elevation=0,
              difficulty_level_explanation='due to climbing over logs '
                                           'and deep wading',
              difficulty_level='2difficult')
    add_hikes(name='North Molalla River Trails Loop Hike',
              trailhead='Amanda\'s Trailhead',
              hike_type='loop',
              distance=5.8, elevation=1140, high_point=1200,
              difficulty_level='1moderate')
    add_hikes(name='Gunsight Butte-Badger Lake Loop Hike',
              trailhead='Badger Creek Upper Trailhead',
              hike_type='loop',
              distance=8.5, elevation=2025, high_point=5916,
              difficulty_level='1moderate')
    add_hikes(name='Lookout Mountain Loop Hike',
              trailhead='High Prairie Trailhead',
              hike_type='loop',
              distance=2.9, elevation=565, high_point=6525,
              difficulty_level='0easy')
    add_hikes(name='Smith and Bybee Lakes Hike',
              trailhead='Smith and Bybee Trailhead',
              hike_type='out_and_back',
              distance=2.1, elevation=10, high_point=25,
              difficulty_level='0easy')
    add_hikes(name='Bald Mountain from Lolo Pass Hike',
              trailhead='Lolo Pass Trailhead',
              distance=6.6, elevation=1400, high_point=4591,
              difficulty_level='1moderate')
    add_hikes(name='Wood Lake via Sawtooth Mountain Hike',
              trailhead='Sawtooth Trailhead',
              distance=9.2,
              hike_type='out_and_back',
              elevation=2190, high_point=5250,
              difficulty_level='1moderate')
    add_hikes(name='Elowah Falls Hike',
              trailhead='John B Yeon Trailhead',
              hike_type='out_and_back',
              distance=1.4, elevation=280,
              difficulty_level='0easy')
    add_hikes(name='Lake Wapiki Hike',
              trailhead='Filloon Trailhead',
              distance=7.0,
              hike_type='out_and_back',
              elevation=1625, high_point=5241,
              difficulty_level='1moderate')
    add_hikes(name='Silver King Lake via Whetstone Ridge Hike',
              trailhead='Whetstone Trailhead',
              hike_type='out_and_back',
              distance=10.2, high_point=4535, elevation=2215,
              difficulty_level='1moderate')
    add_hikes(name='Cougar Rock via Elevator Shaft Hike',
              trailhead='Multnomah Falls Trailhead',
              hike_type='loop',
              distance=6.7, elevation=1860,
              difficulty_level='2difficult')
    add_hikes(name='Gorton Creek Falls Hike',
              trailhead='Wyeth Trailhead',
              hike_type='out_and_back',
              distance=1.2, elevation=150,
              difficulty_level='1moderate')
    add_hikes(name='Balfour-Klickitat Loop Hike',
              trailhead='Balfour-Klickitat Trailhead',
              hike_type='loop',
              distance=0.7, elevation=115, high_point=220,
              difficulty_level='0easy')
    add_hikes(name='Bayocean Spit Loop Hike',
              trailhead='Bayocean Spit Trailhead',
              hike_type='loop',
              distance=7.6, elevation=50,
              difficulty_level='1moderate')
    add_hikes(name='Thomas Lake Hike',
              trailhead='Thomas Lake Trailhead',
              hike_type='out_and_back',
              distance=1.8, elevation=200,
              difficulty_level='0easy')
    add_hikes(name='Mount Saint Helens Hike',
              trailhead='Climber\'s Bivouac Trailhead',
              hike_type='out_and_back',
              distance=9.6, high_point=8280, elevation=4665,
              difficulty_level='2difficult')
    add_hikes(name='Mount Mitchell-Cottonwood Meadows Hike',
              trailhead='Rimrock Trailhead',
              hike_type='out_and_back',
              distance=5.0, elevation=830, high_point=5015,
              difficulty_level='1moderate')
    add_hikes(name='Tooth Rock Loop Hike',
              trailhead='Tooth Rock Trailhead',
              hike_type='loop',
              distance=1.8, elevation=220,
              difficulty_level='0easy')
    add_hikes(name='Falls Creek Falls Loop Hike',
              trailhead='Falls Creek Falls Lower Trailhead',
              hike_type='loop',
              distance=6.2, elevation=1150,
              difficulty_level='1moderate')
    add_hikes(name='Rudolph Spur Loop Hike',
              trailhead='Bridge of the Gods Trailhead',
              hike_type='loop',
              distance=10.4, elevation=3700,
              difficulty_level='2difficult')
    add_hikes(name='Tom Dick and Harry Mountain Hike',
              trailhead='Mirror Lake Trailhead',
              distance=5.8, elevation=1710, high_point=4920,
              difficulty_level='1moderate')
    add_hikes(name='Chenamus Lake Hike',
              trailhead='Placid Lake Trailhead',
              distance=4.1,
              hike_type='out_and_back',
              elevation=485, high_point=4245,
              difficulty_level='0easy')
    add_hikes(name='Bluegrass Ridge-Cold Spring Creek Loop Hike',
              trailhead='Polallie Trailhead',
              hike_type='loop',
              distance=15.5, elevation=3580, high_point=5605,
              difficulty_level='2difficult')
    add_hikes(name='Fort Stevens Loop Hike',
              trailhead='Military Museum Trailhead',
              hike_type='loop',
              distance=10.0, elevation=40, high_point=30,
              difficulty_level='1moderate')
    add_hikes(name='Misery Ridge Loop Hike',
              trailhead='Smith Rock Trailhead',
              hike_type='loop',
              distance=3.8, elevation=1000,
              difficulty_level='1moderate')
    add_hikes(name='Eliot Moraine Hike',
              trailhead='Cloud Cap Trailhead',
              distance=2.1, elevation=870,
              difficulty_level='1moderate')
    add_hikes(name='Elk Lake Creek Hike',
              trailhead='Elk Lake Creek Trail Northern Trailhead',
              hike_type='out_and_back',
              distance=4.4, elevation=400,
              difficulty_level='0easy')
    add_hikes(name='Cascade Streamwatch Loop Hike',
              trailhead='Wildwood Recreation Area Winter Trailhead',
              hike_type='loop',
              distance=4.4, elevation=40, high_point=1235,
              difficulty_level='0easy')
    add_hikes(name='Iron Mountain Hike',
              trailhead='Iron Mountain Trailhead',
              hike_type='out_and_back',
              distance=2.4, elevation=650,
              difficulty_level='1moderate')
    add_hikes(name='Weldon Wagon Road Hike',
              trailhead='Sanborn Road Trailhead',
              hike_type='out_and_back',
              distance=5.2, high_point=1845, elevation=1240,
              difficulty_level='1moderate')
    add_hikes(name='Sheep Canyon Loop Hike',
              trailhead='Blue Lake Trailhead',
              hike_type='lollipop',
              distance=11.3, elevation=2535, high_point=4700,
              difficulty_level='1moderate')

    add_trailhead(trailhead='Black Lake Trailhead',
                  region=wa_coast_region,
                  latitude=46.31401, longitude=-124.04256)
    add_hikes(name='Black Lake Loop Hike',
              trailhead='Black Lake Trailhead',
              hike_type='loop',
              distance=2.6, elevation=150, high_point=135,
              difficulty_level='0easy')

    add_trailhead(trailhead='Obstruction Point Trailhead',
                  region=wa_coast_region,
                  latitude=47.91829, longitude=-123.38287)
    add_hikes(name='Grand Valley Badger Valley Loop Hike',
              trailhead='Obstruction Point Trailhead',
              hike_type='loop',
              distance=14, elevation=4250,
              difficulty_level='2difficult')
    add_trailhead(trailhead='Dosewallips Trailhead',
                  region=wa_coast_region,
                  latitude=47.7392, longitude=-123.0725)
    add_hikes(name='Dosewallips River Hike',
              trailhead='Dosewallips Trailhead',
              hike_type='point_to_point',
              distance=9, elevation=1600,
              difficulty_level='1moderate')

    # for r in Region.objects.all():
    #     for l in Trailhead.objects.filter( region=r):
    #         print("- {0} - {1}".format(str(r), str(l)))

    # update_count()


def add_region(region):
    r = Region.objects.get_or_create(name=region)[0]
    return r


def add_trailhead(region, trailhead, latitude, longitude):
    # print(region)
    l = Trailhead.objects.get_or_create(region=region,
                                        name=trailhead,
                                        latitude=latitude,
                                        longitude=longitude)[0]
    return l


def add_hikes(name, trailhead, hike_type="out_and_back", distance=0.0,
              elevation=0, difficulty_level="0easy",
              difficulty_level_explanation='', high_point=0):
    try:
        this_trailhead = Trailhead.objects.get(name=trailhead)
    except Trailhead.DoesNotExist:
        region = Region.objects.get_or_create(name='Unknown')[0]
        this_trailhead = Trailhead.objects.create(name=trailhead,
                                                  region=region)
    return Hike.objects.get_or_create(
        name=name,
        trailhead=this_trailhead,
        hike_type=hike_type,
        distance=distance, elevation=elevation,
        difficulty_level=difficulty_level,
        difficulty_level_explanation=difficulty_level_explanation,
        high_point=high_point)[0]


if __name__ == '__main__':
    print('Starting Hike the World Population script...')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hiking.settings.dev')
    django.setup()
    from hikes.models import Region, Trailhead, Hike
    from django.apps import apps
    populate()
    print('Regions: {}'.format(Region.objects.all().count()))
    print('Trailheads: {}'.format(Trailhead.objects.all().count()))
    print('Hikes: {}'.format(Hike.objects.all().count()))
