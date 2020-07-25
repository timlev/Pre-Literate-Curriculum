import os, glob
from bs4 import BeautifulSoup

food_unit_files = glob.glob("../6 - Food and Health/*.html")

correct_imgs = {} # {filename : [generated_output , correct_output]}

def orig_output(img):
    img_ext = img.rsplit(".")[1]
    orig = img.replace(img_ext,"jpg")
    return orig


#THIS WAS USED TO GENERATE FROM KNOWN GOOD FILES
# ~ for f in food_unit_files:
    # ~ correct_imgs[f] = []
    # ~ soup = BeautifulSoup(open(f),"html5lib")
    # ~ imgs = soup.find_all("img")
    # ~ current_imgs = [x["src"] for x in imgs if x.get("class") == None and x["src"] != '../images/back_button.png' and not x["src"].endswith(".jpg")]
    # ~ for i in current_imgs:
        # ~ correct_imgs[f].append([orig_output(i),i]) # {filename : [generated_output , correct_output]}


correct_imgs = {'../6 - Food and Health/6 Cooking.html': [[u'imgs/cook.jpg', u'imgs/cook.gif'], [u'imgs/open.jpg', u'imgs/open.gif'], [u'imgs/cut.jpg', u'imgs/cut.gif'], [u'imgs/mix.jpg', u'imgs/mix.gif'], [u'imgs/peel.jpg', u'imgs/peel.gif'], [u'imgs/boil.jpg', u'imgs/boil.gif'], [u'imgs/wash.jpg', u'imgs/wash.gif']], '../6 - Food and Health/5 Healthy.html': [], '../6 - Food and Health/1 Food.html': [], '../6 - Food and Health/3 Restaurant.html': [], '../6 - Food and Health/2 More Food.html': [], '../6 - Food and Health/4 Cake.html': []}


for k in [x for x in correct_imgs.keys() if correct_imgs[x] != []]:
    print(k)
    fileblob = ""
    with open(k,"r") as fp:
        fileblob = fp.read()
    for generated_output, correct_output in tuple(correct_imgs[k]):
        fileblob = fileblob.replace(generated_output, correct_output)
        print(generated_output, correct_output)
    with open(k,"w") as fp:
        fp.write(fileblob)
    