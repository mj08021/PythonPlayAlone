# f = open("test.txt", "w", encoding="utf-8")
# f.write("안녕, 스파르타!\n")
# for i in [1,2,3,4,5]:
#     f.write(f"{i}번째 줄이에요\n")
#
# f.close()

#----------------------------------

# text = ''
# with open("test.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     for line in lines:
#         # print(line)
#         text += line
#
# print(text)

#----------------------------------

# import matplotlib.font_manager as fm
#
# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)

#----------------------------------

from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ''
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ', '').replace('ㅠ', '').replace('ㅜ', '').replace('이모티콘\n', '').replace('사진\n', '').replace('삭제된 메시지입니다', '').replace('근데', '').replace('지금', '').replace('진짜', '').replace('너무', '').replace('나도', '').replace('그거', '').replace('그리고', '').replace('ㅇㅇ', '').replace('ㄹㅇ', '').replace('아니', '').replace('내가', '').replace('나는', '').replace('민지', '').replace('그럼', '').replace('있어', '').replace('아직', '').replace('맞아', '').replace('많이', '').replace('이제', '').replace('오늘', '').replace('좋아', '').replace('하고', '').replace('아냐', '')

print(text)

# wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result.png")


mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")