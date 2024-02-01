from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://www.coursera.org/courses")
html_soup = BeautifulSoup(response.content, 'html.parser')
url = html_soup.find_all(href=True)
course_title = []
course_organization = []
course_URL =[]
course_Certificate_type = []
course_rating = []
course_difficulty = []
course_students_enrolled = []
course_image_URL = []
course_image_name=[]
#to scrape all pages loop the variable at page =1 as page =i
url = "https://www.coursera.org/courses?page=1&index=prod_all_products_term_optimization"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


for j in range(0,10):
    ct = soup.find_all('h2', class_ ="color-primary-text card-title headline-1-text")[j].get_text()
    course_title.append(ct)
    co = soup.find_all('span', class_ = 'partner-name m-b-1s')[j].get_text()
    course_organization.append(co)
    cu= soup.find_all("a", class_='rc-DesktopSearchCard anchor-wrapper')[j]
    course_URL.append("https://www.coursera.org"+ cu.get('href'))
    cc= soup.find_all('div', class_='_jen3vs _1d8rgfy3')[j].get_text()
    course_Certificate_type.append(cc)
    cr=soup.find_all('span', class_ = 'ratings-text')[j]
    course_rating.append(cr)
    cd= soup.find_all('span',class_='difficulty')[j].get_text()
    course_difficulty.append(cd)
    ce= soup.find_all('span',class_='enrollment-number')[j].get_text()
    course_students_enrolled.append(ce)
    x_div = soup.find_all('img', class_ ="product-photo")[j]
    course_image_URL.append(x_div.get('src'))
    course_image_name.append(x_div.get('alt'))

courses_df = pd.DataFrame({'course_title': course_title,
                           'course_URL':course_URL,
                          'course_organization': course_organization,
                          'course_Certificate_type': course_Certificate_type,
                          'course_rating':course_rating,
                           'course_difficulty':course_difficulty,
                           'course_students_enrolled':course_students_enrolled,
                            'course_icon':course_image_URL,
                          'image_name':course_image_name})

# courses_df = courses_df.sort_values('course_title')

courses_df.to_csv('Coursera_Courses_test.csv')
course_title = []
course_organization = []
course_URL =[]
course_Certificate_type = []
course_rating = []
course_difficulty = []
course_students_enrolled = []
course_image_URL = []
course_image_name=[]

def auto_scrape(j,html_tag,class_tag,course_item):
    bsoup = soup.find_all(html_tag, class_ = class_tag)[j].get_text()
    course_item.append(bsoup)
def auto_scrape_imgURL(j,html_tag,class_tag,course_url_item,course_url_name):
    x_div = soup.find_all('img', class_ ="product-photo")[j]
    course_url_item.append(x_div.get('src'))
    course_url_name.append(x_div.get('alt'))
def auto_scrape_URL(j,html_tag,class_tag,course_item):
    cu= soup.find_all("a", class_='rc-DesktopSearchCard anchor-wrapper')[j]
    course_URL.append("https:/www.coursera.org"+ cu.get('href'))
    
for j in range(0,10):
    auto_scrape(j,'h2',"color-primary-text card-title headline-1-text",course_title)
    auto_scrape(j,'span', 'partner-name m-b-1s',course_organization)
    auto_scrape_URL(j,"a",'rc-DesktopSearchCard anchor-wrapper',course_URL)
    auto_scrape(j,'div','_jen3vs _1d8rgfy3',course_Certificate_type)
    auto_scrape(j,'span', 'ratings-text',course_rating)
    auto_scrape(j,'span','difficulty',course_difficulty)
    auto_scrape(j,'span','enrollment-number',course_students_enrolled)
    auto_scrape_imgURL(j,'img', "product-photo",course_image_URL,course_image_name)
    
import pandas as pd
coursesf_df = pd.DataFrame({'course_title': course_title,
                           'course_URL':course_URL,
                          'course_organization': course_organization,
                          'course_Certificate_type': course_Certificate_type,
                          'course_rating':course_rating,
                           'course_difficulty':course_difficulty,
                           'course_students_enrolled':course_students_enrolled,
                            'course_icon':course_image_URL,
                          'image_name':course_image_name})

# courses_df = courses_df.sort_values('course_title')

coursesf_df.to_csv('Coursera_Courses_test_function.csv')
df = pd.DataFrame() 
# course title
count1=[]
for page in range(1,100):
    print(page,end=' ')
    url = "https://www.coursera.org/courses?page="+str(page)+"&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for j in range(0,10):
        ct = soup.find_all('h2', class_ ="color-primary-text card-title headline-1-text")[j].get_text()
        count1.append(ct)
    print(len(count1),end="\t|\t")
df['course_title'] = count1
#course URL
count=[]
for page in range(1,100):
    print(page,end=' ')
    url = "https://www.coursera.org/courses?page="+str(page)+"&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for j in range(0,10):
        cu= soup.find_all("a", class_='rc-DesktopSearchCard anchor-wrapper')[j]
        count.append("https://www.coursera.org"+ cu.get('href'))
    print(len(count),end="\t|\t")
df['course_URL']=count

count=[]
for page in range(1,100):
    print(page,end=' ')
    url = "https://www.coursera.org/courses?page="+str(page)+"&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for j in range(0,10):
        co = soup.find_all('span', class_ = 'partner-name m-b-1s')[j].get_text()
        count.append(co)
    print(len(count),end="\t|\t")  
    df['course_organization']= count
    # course certificate type
count=[]
for page in range(1,100):
    print(page,end=' ')
    url = "https://www.coursera.org/courses?page="+str(page)+"&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for j in range(0,10):
        cc= soup.find_all('div', class_='_jen3vs _1d8rgfy3')[j].get_text()
        count.append(cc)
    print(len(count),end="\t|\t")  

# course-rating
count=[]
for page in range(1,100):
    print(page,end=' ')
    url = "https://www.coursera.org/courses?page="+str(page)+"&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
for j in range(0,10):
    cr=soup.find_all('div', class_ = "rating-enroll-wrapper")[j]
    x_div=cr.find('span',class_="ratings-text")
    if x_div is None:
            print("None",end=' ')
            count.append("None")
    else:        
            print(x_div.get_text(),end=' ')
            count.append(x_div.get_text())
print(len(count),end="  |  ")  

df['course_rating']= count
# course difficulty type
count=[]
for page in range(1,100):
    print(page,end=' ')
    url = "https://www.coursera.org/courses?page="+str(page)+"&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for j in range(0,10):
        cd= soup.find_all('span',class_='difficulty')[j].get_text()
        count.append(cd)
    print(len(count), end='\t|\t') 

#course enrollment number
count=[]
for page in range(1,100):
    print(page,end=' ')
    url = "https://www.coursera.org/courses?page="+str(page)+"&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for j in range(0,10):
        ce=soup.find_all('div', class_ = "rating-enroll-wrapper")[j]
        xe_div=ce.find('span',class_='enrollment-number')
        if xe_div is None:
            print("None",end=' ')
            count.append("None")
        else:        
            print(xe_div.get_text(),end=' ')
            count.append(xe_div.get_text())
    print(len(count))  
    df['course_enrolled']= count
# course image URL and Name
count1=[]
count2=[]
for page in range(1,100):
    print(page,end=' ')
    url = "https://www.coursera.org/courses?page="+str(page)+"&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for j in range(0,10):
        x_div = soup.find_all('img', class_ ="product-photo")[j]
        count1.append(x_div.get('src'))
        count2.append(x_div.get('alt'))
    print(len(count1),end='  ')
    print(len(count2),end='   |   ')
    
    df['course_imageURL']=count1
df['course_imagename']=count2

        
print(df.head())
for i in range(0,10):
    cu= soup.find_all("a", class_='rc-DesktopSearchCard anchor-wrapper')[i]
    course_URL.append("https://www.coursera.org/"+ cu.get('href'))
           
print(course_URL)
course_Certificate_type = []
for j in range(0,10):
    cc= soup.find_all('div', class_='_jen3vs _1d8rgfy3')[j].get_text()
    course_Certificate_type.append(cc)
    
print(course_Certificate_type)
for j in range(0,10):
    cr=soup.find_all('span', class_ = 'ratings-text')[j].get_text()
    course_rating.append(cr)
print(course_rating)
course_difficulty = []
for j in range(0,10):
    x= soup.find_all('span',class_='difficulty')[j].get_text()
    course_difficulty.append(x)
print(course_difficulty)
course_students_enrolled = []
for j in range(0,10):
    x= soup.find_all('span',class_='enrollment-number')[j].get_text()
    course_students_enrolled.append(x)
print(course_students_enrolled)

course_image_URL = []
course_image_name=[]
for j in range(0,10):
    x_div = soup.find_all('img', class_ ="product-photo")[j]
#div class="image-wrapper"
    print(x_div.get('src'))
    print(x_div.get('alt'))
    course_image_URL.append(x_div.get('src'))
    course_image_name.append(x_div.get('alt'))
print(course_image_URL,course_image_name)