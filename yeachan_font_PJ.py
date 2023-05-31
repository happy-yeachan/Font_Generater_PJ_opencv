import sys
import cv2
import numpy as np
import h_to_e

def Make_chosung(chosung): # 초성 생성
    if len(chosung) == 1:
        if str(chosung[0]) == 'R':
            tmp = cv2.imread('./yeachan_pont/rr.jpg')
            src = cv2.resize(tmp, (50,50))
        elif str(chosung[0]) == 'E':
            tmp = cv2.imread('./yeachan_pont/ee.jpg')
            src = cv2.resize(tmp, (50,50))
        elif str(chosung[0]) == 'Q':
            tmp = cv2.imread('./yeachan_pont/qq.jpg')
            src = cv2.resize(tmp, (50,50))
        elif str(chosung[0]) == 'T':
            tmp = cv2.imread('./yeachan_pont/tt.jpg')
            src = cv2.resize(tmp, (50,50))
        elif str(chosung[0]) == 'W':
            tmp = cv2.imread('./yeachan_pont/ww.jpg')
            src = cv2.resize(tmp, (50,50))
        else:
            tmp = cv2.imread('./yeachan_pont/'+ str(chosung[0]) +'.jpg')
            src = cv2.resize(tmp, (50,50))
    else:
        src1 = cv2.imread('./yeachan_pont/'+ str(chosung[0]) +'.jpg')
        src2 = cv2.imread('./yeachan_pont/'+ str(chosung[1]) +'.jpg')
        tmp = cv2.hconcat([src1, src2])
        src = cv2.resize(tmp, (50,50))
    return src

def Make_jungsung(jungsung): # 중성 생성
    if str(jungsung[0]) == 'O':
        tmp = cv2.imread('./yeachan_pont/oo.jpg')
        src = cv2.resize(tmp, (50,50))
    elif str(jungsung[0]) == 'P':
        tmp = cv2.imread('./yeachan_pont/pp.jpg')
        src = cv2.resize(tmp, (50,50))
    else:
        if len(jungsung) == 1:
            tmp = cv2.imread('./yeachan_pont/'+ str(jungsung[0]) +'.jpg')
            src = cv2.resize(tmp, (50,50))
        elif len(jungsung) == 2:
            src =[]
            tmp = cv2.imread('./yeachan_pont/'+ str(jungsung[0]) +'.jpg')
            src.append(cv2.resize(tmp, (50,50)))
            tmp2 = cv2.imread('./yeachan_pont/'+ str(jungsung[1]) +'.jpg')
            src.append(cv2.resize(tmp2, (50,50)))
    return src

def Make_jongsung(jongsung): # 종성 생성
    if len(jongsung) == 1:
        if str(jongsung[0]) == 'R':
                tmp = cv2.imread('./yeachan_pont/rr.jpg')
                src = cv2.resize(tmp, (50,50))
        elif str(jongsung[0]) == 'E':
            tmp = cv2.imread('./yeachan_pont/ee.jpg')
            src = cv2.resize(tmp, (50,50))
        elif str(jongsung[0]) == 'Q':
            tmp = cv2.imread('./yeachan_pont/qq.jpg')
            src = cv2.resize(tmp, (50,50))
        elif str(jongsung[0]) == 'T':
            tmp = cv2.imread('./yeachan_pont/tt.jpg')
            src = cv2.resize(tmp, (50,50))
        elif str(jongsung[0]) == 'W':
            tmp = cv2.imread('./yeachan_pont/ww.jpg')
            src = cv2.resize(tmp, (50,50))
        else:
            tmp = cv2.imread('./yeachan_pont/'+ str(jongsung[0]) +'.jpg')
            src = cv2.resize(tmp, (50,50))
    else:
        src1 = cv2.imread('./yeachan_pont/'+ str(jongsung[0]) +'.jpg')
        src1 = cv2.resize(src1, (50,50))
        src2 = cv2.imread('./yeachan_pont/'+ str(jongsung[1]) +'.jpg')
        src2 = cv2.resize(src2, (50,50))
        tmp = cv2.hconcat([src1, src2])
        src = cv2.resize(tmp, (50,50))
    return src

def hangul_test(chosung, jungsung, jongsung): # 올바른 글자를 입력했는지 판별
    if len(chosung) > 1:
        print("제대로된 한글을 입력해 주세요.\n (초성에 자음이 2개 이상 존재할 수 없어요..!)")
        exit()
    elif len(jungsung) > 2:
        print("제대로된 한글을 입력해 주세요.\n (중성에 모음이 3개 이상 존재할 수 없어요..!)")
        exit()
    elif len(jongsung) >2:
        print("제대로된 한글을 입력해 주세요.\n (종성에 자음이 3개 이상 존재할 수 없어요..!)")
        exit()

def make_hangul(word): # 글자 생성 함수
    jaum = ['r','s','e','f','a','q','t','d','w','c','z','x','v','g','R','E','Q','T','W']
    moum1 = ['k','i','j','u','l', 'o', 'p', 'O', 'P']
    moum2 = ['h','y','n','b','m']
    if word[0] in moum1 or word[0] in moum2:
        print("제대로된 한글을 입력해 주세요.\n (모음이 먼저 오는 한글은 존재하지 않습니다..!)")
        exit()
    flag = False
    chosung = []
    jungsung = []
    jongsung = []
    # 초성 중성 종성 저장
    for i in word:
        if i in jaum and flag == False:
            chosung.append(i)
        elif i in moum1 or i in moum2:
            flag = 1
            jungsung.append(i)
        elif i in jaum and flag == True:
            jongsung.append(i)

    hangul_test(chosung, jungsung, jongsung)

    c = Make_chosung(chosung)
    ju = Make_jungsung(jungsung)
    if len(jungsung) == 1:
        if jungsung[0] in moum1:
            if len(jongsung) != 0:
                jo = Make_jongsung(jongsung)
                tmp = cv2.hconcat([c, ju])
                tmp = cv2.resize(tmp, (50,50))
                tmp2 = cv2.vconcat([tmp, jo])
                src = cv2.resize(tmp2, (50,50))
            else:
                tmp = cv2.hconcat([c, ju])
                src = cv2.resize(tmp, (50,50))
        elif jungsung[0] in moum2:
            if len(jongsung) != 0:
                jo = Make_jongsung(jongsung)
                tmp = cv2.vconcat([c, ju])
                tmp2 = cv2.vconcat([tmp, jo])
                src = cv2.resize(tmp2, (50,50))
            else:
                tmp = cv2.vconcat([c, ju])
                src = cv2.resize(tmp, (50,50))
    elif len(jungsung) == 2:
        tmp = cv2.vconcat([c, ju[0]])
        src = cv2.resize(tmp, (50,50))
        tmp2 = cv2.hconcat([src, ju[1]])
        src = cv2.resize(tmp2, (50,50))
        if len(jongsung) != 0:
            jo = Make_jongsung(jongsung)
            tmp3 = cv2.vconcat([src, jo])
            src = cv2.resize(tmp3, (50,50))
    return src

def tr(word):
    jaum = ['r','s','e','f','a','q','t','d','w','c','z','x','v','g','R','E','Q','T','W']
    moum = ['k','i','j','u','l', 'o', 'p', 'O', 'P', 'h','y','n','b','m']
    word.pop()
    flag = False
    tmp = ''
    collec = []
    for i in reversed(word):
        tmp = tmp + str(i)
        if flag == True and i in jaum:
            tmp = ''.join(reversed(tmp))
            collec.append(tmp)
            tmp = ''
            flag = False
        elif i in moum:
            flag = True
        elif i == ' ':
            collec.append(i)
    return list(reversed(collec))

black_canvas = np.zeros((500, 500, 3), dtype="uint8")
black_canvas = cv2.resize(black_canvas, (25,50))

print("출력을 원하는 문장을 입력하세요.\n ->", end=" ")
src = []
word = sys.stdin.readline()

word = list(h_to_e.kor2eng(word)) # 한타 영타 변환
li = tr(word)
for i in li:
    if i != ' ':
        src.append(make_hangul(i))
    else:
        src.append(black_canvas)

k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
tmp = cv2.hconcat(src)
last = cv2.erode(tmp, k)

cv2.imshow('last',  last)
cv2.waitKey()
cv2.destroyAllWindows()