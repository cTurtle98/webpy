"""

ace_outs.py

by Ciaran Farley (ciaran@cturtle98.com)

ace_outs is a program for tracking the outs products at ace hardware on teh west side of santa cruz where I work

I wrote this because I was annoyed at how I did my job before

"""

#for parsing scraped pages
from bs4 import BeautifulSoup

# for downloading pages to scrape
import requests

# for saving and loading dictionaries
import json

# for outs list
from datetime import datetime

class Products:
  """ data struct for a dataset of products that ace hardware carries """

  PRODUCTS_JSON = "/array/www/webpy/webpy/data/ace_products.json"
  products_dict = None
  OUTS_JSON = "/array/www/webpy/webpy/data/ace_outs.json"
  outs_dict = None

  def __init__(self):
    
    #load the products dict
    try:
      # try to load from file
      self.products_dict = self.__load_json(self.PRODUCTS_JSON)
    # if file failes use default dict
    except:
      self.products_dict = {
        'upc' : "sku"
      }
    
    #load the outs dict
    try:
      self.outs_dict = self.__load_json(self.OUTS_JSON)
    except:
      self.outs_dict = {
        'date' : {
          'isle': ['sku1', 'sku2']
        }
      }
    
  def __load_json(self, json_file):
    """ helper function to load json files into dictionaries """
    # open the json file
    f = open(json_file, encoding='utf-8')
    # set the dict
    dictionary = json.load(f)
    # close the file
    f.close
    # return the dict
    return dictionary
  
  def __save_json(self, dictionary, json_file):
    """helper function to save the dicts to json files"""
    #fancier try except for file open
    with open(json_file, 'w') as f:
      # translate dict to json and write file
      json.dump(dictionary, f, indent=2)
      # will hit this return if able to open file
      return("success")
    # will hit this return if unable to open file
    return("failure")

  def _scrape(self, upc):
    """
    this function recieves the SKU for ace products from an input of the UPC code
    usage is to update the internal database when a new product is found
    """
    #download the page for the product
    soup = BeautifulSoup(requests.get("https://www.acehardware.com/search?query=" + upc).text, "html.parser")
    #search the product page for the sku code
    sku = soup.find('dd', attrs={'class':'mz-productcodes-productcode','itemprop':'sku'}).text
    #return the sku
    return(sku)

  def add_product(self, upc):
    """ add a product to the data set"""
    #scrape the ace website for the SKU
    self.products_dict[upc] = self._scrape(upc)
    # save out the dict to file for the next session
    self.__save_json(self.products_dict, self.PRODUCTS_JSON)
    # return to complete the function
    return()
  
  def get_product(self, upc):
    """ retrieve product from data set"""
    # check if its in the data set and return that
    try: 
      return(self.products_dict[upc])
    # if it throws a key error (not in data set) add it to the set
    except:
      self.add_product(upc)
      return(self.get_product(upc))

  def set_out(self, upc, isle):
    # get the sku of the out product
    sku = self.get_product(upc)
    # get the date
    date = datetime.date(datetime.now())
    # add to outs list for today in selected isle
    try: 
      # try to append sku directly
      self.outs_dict[str(date)][isle].append(sku)
    except: 
      # if todays date isnt there add it
      self.outs_dict[str(date)] = {}
      try: 
        # try to append sku again
        self.outs_dict[str(date)][isle].append(sku)
      except: 
        # add the isle
        self.outs_dict[str(date)][isle] = []
        # now everything is here for sure so append the sku
        self.outs_dict[str(date)][isle].append(sku)
    #remve duplicates
    self.outs_dict[str(date)][isle] = list(set(self.outs_dict[str(date)][isle]))
    # save outs to disk
    self.__save_json(self.outs_dict, self.OUTS_JSON)
    # return to complete the function
    return()

prod = Products()

# import flaks enviroment
from webpy import app
import flask

outs = prod.outs_dict

@app.route('/ace_outs/')
def ace_outs_route():
  return flask.render_template('ace_outs.jinja2', outs=outs)

@app.route('/ace_outs/scan/')
def ace_outs_scan():
  
  '''
  isle = flask.request.args.get('isle')
  upcs = flask.request.args.get('UPCs')
  
  if (upcs != None):  
    for upc in upcs.splitlines():
      prod.set_out(upc, isle)
  '''
  
  return """
  <h3> ace outs scan page </h3>
  <form action="/ace_outs/scan/">
    <label for="isle"> Isle: </label>
    <select id="isle" name="isle">
      <option value="01L">01L</option>
      <option value="01R">01R</option>
      <option value="02L">02L</option>
      <option value="02R">02R</option>
      <option value="03L">03L</option>
      <option value="03R">03R</option>
      <option value="04L">04L</option>
      <option value="04R">04R</option>
      <option value="05L">05L</option>
      <option value="05R">05R</option>
      <option value="06L">06L</option>
      <option value="06R">06R</option>
      <option value="07L">07L</option>
      <option value="07R">07R</option>
      <option value="08L">08L</option>
      <option value="08R">08R</option>
      <option value="09L">09L</option>
      <option value="09R">09R</option>
      <option value="10L">10L</option>
      <option value="10R">10R</option>
      <option value="11L">11L</option>
      <option value="11R">11R</option>
      <option value="12L">12L</option>
      <option value="12R">12R</option>
      <option value="13L">13L</option>
      <option value="13R">13R</option>
      <option value="14L">14L</option>
      <option value="14R">14R</option>
      <option value="15L">15L</option>
      <option value="15R">15R</option>
      <option value="16L">16L</option>
      <option value="16R">16R</option>
      <option value="17L">17L</option>
      <option value="17R">17R</option>
      <option value="18L">18L</option>
      <option value="18R">18R</option>
      <option value="19L">19L</option>
      <option value="19R">19R</option>
      <option value="WALL01">WALL01</option>
      <option value="REG">REG</option>
    </select><br>
    <label for="UPCs"> UPCs: </isle><br>
    <textarea id="UPCs" name="UPCs" rows="20" cols="13"></textarea><br>
    <input type="submit" value="Submit">
  </form>
  """
