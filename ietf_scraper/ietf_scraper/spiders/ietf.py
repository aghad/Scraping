import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        return{
            'number': response.xpath('//span[@class="rfc-no"]/text()').get(),
            'title': response.xpath('//meta[@name="DC.Title"]/@content').get(),
            'date': response.xpath('//span[@class="date"]/text()').get(),
            'description': response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get(),
            'author': response.xpath('//span[@class="author-name"]/text()').get(),
            'company': response.xpath('//span[@class="author-company"]/text()').get(),
            'address': response.xpath('//span[@class="address"]/text()').get(),
            'phone': response.xpath('//span[@class="phone"]/text()').get(),
            'email': response.xpath('//span[@class="email"]/text()').get(),
        }

# /html/body/div/h1 We can do this if you're trying to go into a particular tag, but would
# go to a title b/c we need to pass each tag
# //h1 //Allows you to choose which tags you would liek to go to
# //div/h1 //Chooses only the h1 tag that are immiedate children of the div tag
# //div//h1  //Throwing another backslash allows you to get those tags even if they are not an immediate children
# //span[@class="title"]  #this would select any span tags that have the class title, where the attribute of the span tag
# is equal to the string title

# //span[@class= "title"]/@id    //allows us to seelct the id attribute, gives us the value of the id attribute
# however, we don't need the value, we nede the actual text
# instead, we could do this.
# //span[@class="title"]/text()
# Elements are selected by attributes
