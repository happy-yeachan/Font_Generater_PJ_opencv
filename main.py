from yeachan_font_PJ import *
from J_M_gather import *
from h_to_e import *
import sys
import cv2
import numpy as np

print("자음 모음을 적은 파일이 저장된 폴더명을 입력하세요.\n ->", end=" ")
filename = str(input())

ja_list = ['r', 's', 'e', 'f', 'a', 'q', 't', 'd', 'w', 'c', 'z', 'x', 'v', 'g', 'rr', 'ee', 'qq', 'tt', 'ww']
mo_list = ['k', 'i', 'j', 'u', 'h', 'y', 'n', 'b', 'm', 'l', 'o', 'oo', 'p', 'pp']


gather('ja_list', ja_list, filename) # 자음 인식 및 저장
gather('mo_list', mo_list, filename) # 모음 인식 및 저장


print("출력을 원하는 문장을 입력하세요.\n ->", end=" ")
src = []
word = sys.stdin.readline()

word = list(h_to_e.kor2eng(word)) # 한타 -> 영타 변환

li = tr(word) # 문자별로 슬라이싱

src = merge(li, filename) # 문자 생성 및 병합

cv2.imshow('last',  src)
cv2.waitKey()
cv2.destroyAllWindows()