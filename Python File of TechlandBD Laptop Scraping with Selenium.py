# loading the pakages
import pandas as pd
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class LaptopScrpaer():

    def __init__(self):
        self.scrape()

    def scrape(self):
        self.data = []
        driver = webdriver.Chrome(ChromeDriverManager().install())        
        page_input = int(input("Enter the number of pages: "))
        for page in range(1,page_input + 1):
            url = f'https://www.techlandbd.com/shop-laptop-computer?limit=100&page={page}'
            driver.get(url)
            sleep(2)         
            product_lenth = driver.find_elements('xpath','(//div[@class="main-products product-grid"]/div/div/div[@class="caption"]/div[@class="name"]/a)')
            for product in range(1,len(product_lenth)+ 1):
                try:
                    xpath_model = f'(//div[@class="main-products product-grid"]/div/div/div[@class="caption"]/div[@class="name"]/a)[{product}]'
                    xpath_price = f'(//div[@class="price"]/div/span[@class="price-normal" or@class="price-new"])[{product}]'
                    products ={
                        'product_name' : driver.find_element('xpath',xpath_model).text,
                        'product_url' : driver.find_element('xpath',xpath_model).get_attribute('href'),
                        'product_price' : driver.find_element('xpath',xpath_price).text
                    }
                    self.data.append(products)
                except:
                      pass
        self.export_to_csv()

    def export_to_csv(self):
        df = pd.DataFrame(self.data)
        df.to_csv('TechlandBDLaptop.csv', index=False)


if __name__ == '__main__':
    scrape =  LaptopScrpaer()



        



 
    



                



