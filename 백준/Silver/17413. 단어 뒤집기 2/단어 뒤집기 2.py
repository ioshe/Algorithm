# https://www.acmicpc.net/problem/17413

import re

def reverse_words(s):
    # 태그 또는 단어에 대응되는 정규 표현식
    pattern = re.compile(r'<.+?>|[a-zA-Z0-9]+')

    # 주어진 문자열에서 패턴과 일치하는 모든 부분을 찾아서 처리
    def replace_func(match):
        text = match.group(0)
        # 태그는 그대로 반환하고, 단어는 뒤집어서 반환
        return text[::-1] if text[0] != '<' else text

    # 패턴에 일치하는 모든 부분에 대해 replace_func 함수를 적용
    return pattern.sub(replace_func, s)

print(reverse_words(input()))