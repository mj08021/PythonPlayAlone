
# print('hello sparta')

#----------------------------------

# a = 2
# b = 3

# print(a + b)

#----------------------------------

# first_name = 'minji'
# last_name = 'kim'

# print(first_name + last_name)

#----------------------------------

# a = '2'
# first_name = 'minji'

# print(a + first_name)

#----------------------------------

# a = 2
# first_name = 'minji'

# print(str(a) + first_name)

#----------------------------------

# a_list = ['사과', '감', '배']
# b_list = ['영희', '철수', ['사과', '감']]

# a_list.append('수박')

# print(a_list)

#----------------------------------

# a_dict = {'name':'bob', 'age':24}
# a_list = ['수박', '참외', '배']

# a_dict['height'] = 178

# a_dict['fruits'] = a_list

# print(a_dict)
# print(a_dict['fruits'][0])

#----------------------------------

# age = 24
#
# if age > 20:
#     print('성인입니다')
# else:
#     print('청소년입니다')

#----------------------------------

# fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
#
# count = 0
# for fruit in fruits:
#     if fruit == '배':
#         count += 1
#
# print(count)

#----------------------------------

# people = [{'name': 'bob', 'age': 20},
#           {'name': 'carry', 'age': 38},
#           {'name': 'john', 'age': 7},
#           {'name': 'smith', 'age': 17},
#           {'name': 'ben', 'age': 27}]
#
#
# for person in people:
#     if person['age'] > 20:
#         print(person['name'])

#----------------------------------

# myemail = 'sparta@naver.com'
#
# # result = myemail.split('@')[1].split('.')[0]
#
# result = myemail.replace('naver', 'gmail')
#
# print(result)

#----------------------------------

# import dload
#
# dload.save("https://spartacodingclub.kr/static/css/images/ogimage.png")

#----------------------------------

# from selenium import webdriver
# driver = webdriver.Chrome('chromedriver')
#
# driver.get("http://www.naver.com")

#----------------------------------

# import dload
#
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
# driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")
# time.sleep(5) # 5초 동안 페이지 로딩 기다리기
#
# req = driver.page_source
# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# # 이제 코딩을 통해 필요한 부분을 추출하면 된다.
# soup = BeautifulSoup(req, 'html.parser')
#
# thumbnails = soup.select('#imgList > div > a > img')
#
# i = 1
# for thumbnail in thumbnails:
#     img = thumbnail['src']
#     dload.save(img, f'img/{i}.jpg')
#     i += 1
#
#
# driver.quit() # 끝나면 닫아주기

#----------------------------------

