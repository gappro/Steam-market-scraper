from bs4 import BeautifulSoup
import time
import requests
import json


FINAL_TAG = ["_price_desc","_price_asc",""]
data = open(r"Data.json", "r")

def GetValues(allposts):
    f = open(r"Data.json", "r+")
    f.seek(0)
    f.truncate()
    f.close()
    array = []

    # In charge of getting every stat from each post
    for i, post in enumerate(allposts):
        postTitle = post.find("span","market_listing_item_name").get_text()
        postPrice = post.find("span","normal_price").get_text()
        postQuantity = post.find("span","market_listing_num_listings_qty").get_text()
        Splitting = postPrice.split("$")
        Price = Splitting[1:3]
        Priceformat = "$", Price[0].split(" ")[0], "$",Price[1].split(" ")[0], "USD"
        Priceformat = str(Priceformat).split("'")
        Full_phrase = Priceformat[1]+Priceformat[3]+" "+Priceformat[9]
        postIVA = round(float(Priceformat[3])/1.15-0.01, 2)
        postIVA = postIVA

        images = {
                "index": i+1,
                "name": postTitle.split("(")[0],
                "state": postTitle.split("(")[1].split(")")[0],
                "quantity" : postQuantity,
                "price": float(Priceformat[3]),
                "taxprice": postIVA
            }
        json_data = json.dumps(images, indent = 2)
        array.append(images)
        
            

        print(f"{i+1}: {postTitle} {postQuantity} {str(Full_phrase)} | After tax: ${postIVA}")
    with open(r"Data.json", "w") as json_file:
        json.dump(array, json_file, indent=6)

# In charge of getting the page cache
def stepThroughPages(posts, pageNumber, selpages, tag, url):
    soup = BeautifulSoup(requests.get(url+str(pageNumber)+FINAL_TAG[tag]).text, "html5lib")
    time.sleep(3)
    
    posts.extend(soup.find_all("div","market_listing_row market_recent_listing_row market_listing_searchresult"))
    
    if pageNumber >= selpages: 
        return posts
    
    pageNumber += 1
    print("Turning to page " + str(pageNumber))
    
    return stepThroughPages(posts, pageNumber, selpages, tag, url)

def main():
    
    print("Enter Steam market game url  <<Ex. https://steamcommunity.com/market/search?appid=322330#p>>")
    url = input()
        
    print("Enter desired page number")
    Selected_Pagenumb = input()
    
    print("Enter 0 or 1 for price descendant or ascendant, alternatively 2 for none")
    pageorder = input()
    while(FINAL_TAG.__contains__(pageorder)):
        print("Input valid page number")
        pageorder = input()
    
    
    totalPosts = stepThroughPages([], 1, int(Selected_Pagenumb), int(pageorder), url)

    # Reality check
    print(str(len(totalPosts))+" items displayed")
    GetValues(totalPosts)


if __name__ == "__main__":
    main()
