import scrapy
import json

class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['loopnet.com']

    url = "https://www.loopnet.com/services/search"

    payload = {
    "pageguid": "969e314e-4b32-42bc-a4c1-4b763e53a5b8",
    "criteria": {
        "LNPropertyTypes": 1,
        "LNIndustrialSubtypes": 0,
        "LNRetailSubtypes": 0,
        "LNShoppingCenterSubtypes": 0,
        "LNMultiFamilySubtypes": 0,
        "LNSpecialtySubtypes": 0,
        "LNOfficeSubtypes": 0,
        "LNHealthCareSubtypes": 0,
        "LNHospitalitySubtypes": 0,
        "LNSportsAndEntertainmentSubtypes": 0,
        "LNLandSubtypes": 0,
        "PropertyTypes": 34,
        "HospitalitySubtypes": 0,
        "IndustrialSubtypes": 0,
        "LandTypes": 0,
        "OfficeSubtypes": 0,
        "GeneralRetailSubtypes": 0,
        "FlexSubtypes": 0,
        "SportsAndEntertainmentSubtypes": 0,
        "SpecialtySubtypes": 0,
        "MultifamilySubtypes": 0,
        "HealthcareSubtypes": 0,
        "ShoppingCenterTypes": 0,
        "ApartmentStyleTypes": 0,
        "Country": "US",
        "State": "TX",
        "Market": None,
        "MSA": None,
        "County": None,
        "City": "Austin",
        "PostalCode": None,
        "GeographyFilters": [
            {
                "ID": None,
                "BoundingBox": [-98.0855561, 30.068439, -97.5413171, 30.51943],
                "Centroid": [-97.8134366, 30.2939345],
                "Display": "Austin",
                "GeographyId": 6062,
                "Code": " TX",
                "GeographyType": 2,
                "Radius": 0,
                "RadiusLengthMeasure": 0,
                "SubmarketPropertyType": 0,
                "Address": None,
                "MatchType": 3
            }
        ],
        "PageLocationLabel": "Austin, TX",
        "IncludeProximityCities": False,
        "AddressLine": None,
        "Distance": 0,
        "Radius": None,
        "CoordinateBounds": None,
        "Polygon": None,
        "HasValidCoordinates": None,
        "BuildingClass": 0,
        "BuildingSizeUom": "SquareFeet",
        "LotSizeUom": "Acres",
        "SubCategoryList": [402, 403, 405, 406, 413, 415, 4151, 4153, 401, 408, 807],
        "Editor": "Universal",
        "PreserveAddressForRadiusSavedSearch": False,
        "ListingSearchType": 2,
        "OnMarketDateRange": None,
        "Keywords": None,
        "Sorting": [],
        "LoopLinkForLeaseDefaultSorting": [],
        "LoopLinkForSaleDefaultSorting": [],
        "LoopLinkForSaleAndLeaseDefaultSorting": [],
        "PropertyGroupId": None,
        "HasMultipleLocations": False,
        "IsForSale": True,
        "PriceRangeMin": None,
        "PriceRangeMax": None,
        "BuildingSizeRangeMin": None,
        "BuildingSizeRangeMax": None,
        "PriceRangeCurrency": "CAD",
        "PriceRangeRateType": "Total",
        "LotSizeRangeMin": None,
        "LotSizeRangeMax": None,
        "UnitCountRangeMin": None,
        "UnitCountRangeMax": None,
        "CapRateRangeMin": None,
        "CapRateRangeMax": None,
        "YearBuiltRangeMin": None,
        "YearBuiltRangeMax": None,
        "TermLengthRangeMin": None,
        "TermLengthRangeMax": None,
        "NetLeased": False,
        "InContract": True,
        "Distressed": False,
        "Auction": False,
        "IsTenXAuctions": False,
        "AuctionIds": None,
        "Single": False,
        "Multiple": False,
        "InvestmentTypeCore": False,
        "InvestmentTypeValueAdd": False,
        "InvestmentTypeOpportunistic": False,
        "InvestmentTypeTripleNet": False,
        "InvestmentTypeOpportunityZone": False,
        "AuctionAssetTypeProperties": False,
        "AuctionAssetTypeNotes": False,
        "AuctionFinanceTypeFinancing": None,
        "AuctionFinanceTypeBrokerCoOp": None,
        "BusinessForSale": True,
        "VacantOwner": True,
        "Investment": True,
        "InOpportunityZone": None,
        "CondosFilter": 0,
        "PortfoliosFilter": 0,
        "ShoppingCenterFilter": 0,
        "BuildingParkFilter": 0,
        "IsForLease": False,
        "LeaseRateRangeMin": None,
        "LeaseRateRangeMax": None,
        "SpaceAvailableRangeMin": None,
        "SpaceAvailableRangeMax": None,
        "LeaseRateTerm": None,
        "SpaceAvailableUom": None,
        "LeaseRateCurrency": None,
        "LeaseRatePerSizeUom": None,
        "SubLease": False,
        "RegionalMarket": None,
        "SubMarket": None,
        "MoveInDateIndicator": 0,
        "MoveInDateEnteredType": None,
        "MoveInDateEnteredRangeMin": None,
        "MoveInDateEnteredRangeMax": None,
        "ListingId": None,
        "DateIndicator": 0,
        "DateEnteredRangeMin": "",
        "DateEnteredRangeMax": "",
        "MinimumDate": "01/01/0001",
        "DateEnteredType": "RT",
        "DateFormat": "MM/dd/yyyy",
        "ViewMode": "None",
        "ListingIdPinClick": None,
        "IsUserFromUS": False,
        "ForceRemoveBoundary": False,
        "AgentFirstName": None,
        "AgentLastName": None,
        "Currency": None,
        "ListingType": 1,
        "ResultLimit": 500,
        "PageNumber": 2,
        "PageSize": 20,
        "Timeout": 0,
        "Origin": 1,
        "StateKey": "d2f023796fcd285d3b7d7061f8d05a42"
        }
    }
    headers = {
    "authority": "www.loopnet.ca",
    "requestverificationtoken": "Qj4yPqNw1bhi_4gGTygRfkVQTFKRNR6GRCCaUhuRLcmArjiEDz5sRNc7jbNp_p3SHPm4kTwn7cPxPTEAK7Uvq_VHWjE1",
    "traceparent": "00-aa77fc6b4c73154b8b95e006f73055bb-a0bd35b8ecee2e70-00",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
    "content-type": "application/json;charset=UTF-8",
    "accept": "application/json, text/plain, */*",
    "x-page-language": "en-CA;q=0.8",
    "origin": "https://www.loopnet.ca",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.loopnet.ca/search/industrial-properties/austin-tx/for-sale/?sk=2147682fb0bc8f4d7cb54ad566ebda77&e=u",
    "accept-language": "en-US,en;q=0.9"
    }
    
    def start_requests(self):
        yield scrapy.Request(
            url=self.url,
            method='POST',
            body=json.dumps(self.payload),
            headers=self.headers,
            callback=self.parse_listings
        )
    def parse_listings(self, response):
        resp_dict = json.loads(response.body)
        with open('listings.json', 'w') as f:
            json.dump(resp_dict, f)
        ids = resp_dict.get('AllListingIds')
        ids = [id for id in ids.split(',')]
        for id in ids:
            url = f"https://www.loopnet.com/Listing/{id}"
            yield scrapy.Request(url=url, 
                                meta={'id': id,
                                        'url': url},
                                callback=self.parse_details)

    def parse_details(self, response):
        d = {}
        d['id'] = response.request.meta['id']
        d['url'] = response.request.meta['url']
        address = response.xpath("//div[@class='profile-hero-wrapper']//h1[@class='profile-hero-title']//span")
        if(len(address) == 1):
            d['address'] = address.xpath(".//text()").get()
        else:
            d['address'] = response.xpath("//div[@class='profile-hero-wrapper']//h1[@class='profile-hero-title']/span[2]//text()").get()
        if not d['address']:
            d['address'] = response.xpath("//div[@class='profile-hero-wrapper']//h1[@class='profile-hero-title']/text()").get()

        d['date_created'] = response.xpath("//ul[@class='property-timestamp']/li[2]/h4/text()").get()
        table = response.xpath("//table[@class='property-data featured-grid']//tr//td")
        for i, row in enumerate(table):
            if(i % 2 == 0): # even
                k = row.xpath("normalize-space(.//text())").get()
            else: # odd
                v = row.xpath("normalize-space(.//span/text())").get()
                d[k] = v
        yield d

if __name__ == '__main__':
    import os
    from scrapy.cmdline import execute

    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    SPIDER_NAME = ListingsSpider.name
    try:
        execute(
            [
                'scrapy',
                'crawl',
                SPIDER_NAME,
                '-s',
                'FEED_EXPORT_ENCODING=utf-8',
            ]
        )
    except SystemExit:
        pass