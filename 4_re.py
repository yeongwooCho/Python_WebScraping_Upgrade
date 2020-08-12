# 정규식이란 : 정해진 형태를 의미하는 식
# 이메일 주소는 asdfj@nav.com 이고, 주민등록번호는 900101-1234567 이라는 정해진 형태의 식을 가진다.
# 굉장히 많지만 웹스크래핑에서 필요한 부분만 배우자

import re
# 4가지 문자를 외워야하는데 3개만 기억난다
# ca?e --> caae, cabe, ... 는 너무 많으니 정규식을 이용해보자
# p는 패턴을 의미한다고 하자

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > care, cage, case | caffe는 안됨
# ^ (^de) : 문자열의 시작 > desk, destination | dat 는 안됨
# $ (se$) : 문자열의 끝 > case, base | face 는 안됨

# p를 설정했으니 실제 matching 되는 지를 살펴봐야지
m = p.match('case')
print(m.group())
# 정상적으로 출력이 되었다는 것은, 정상적으로 매칭이 되었다는 것을 의미한다.

m = p.match('caffe')
# print(m.group()) # 매칭되지 않으면 에러가 발생한다.


def print_match(m):
    if m:  # 정상적으로 매칭이 되었다면
        print('m.group() :', m.group())  # 일치하는 문자열을 반환
        print('m.string :', m.string)  # 입력받은 문자열을 반환
        print('m.start() :', m.start())  # 일치하는 문자열의 시작 index
        print('m.end() :', m.end())  # 일치하는 문자열의 끝 index (일치하지 않는 부분의 시작)
        print('m.span() :', m.span())  # 일치하는 문자열의 시작 / 끝 index를 함께
    else:
        print('매칭되지않음')


print('\n----------\n')
m = p.match("good cafe")
print_match(m)
m = p.match("cafemachine")  # match : 주어진 문자열의 처음부터 일치하는지 확인(뒷부분은 상관없다.)
print_match(m)  # 정상적으로 출력이 된다. 단, 매칭되는 부분까지만 출력된다.!!!!!

print('\n----------\n')
m = p.search("good care")  # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

print('\n----------\n')
# findall : 일치하는 모든 것을 리스트 형태로 반환
lst = p.findall("carelesscare care ajsdlkfja;sldkjvacate")
print(lst)


# 정리
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식을 쓰는 건데
# . (ca.e) : 하나의 문자를 의미 > care, cage, case | caffe는 안됨
# ^ (^de) : 문자열의 시작 > desk, destination | dat 는 안됨
# $ (se$) : 문자열의 끝 > case, base | face 는 안됨

# 정규식은 w3schools.com 의 밑의 python -> learn python에서 RegEx 에서 볼수 있다.
# python re 구글링해도 참고할 수 있다.
