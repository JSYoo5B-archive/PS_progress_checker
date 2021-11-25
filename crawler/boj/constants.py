#!/usr/bin/env python3

# BOJ result codes
AC = 4          # 맞았습니다
PAC = -4        # (부분 점수)
PE = 5          # 출력 형식이 잘못되었습니다
WA = 6          # 틀렸습니다
TLE = 7         # 시간 초과
MLE = 8         # 메모리 초과
OLE = 9         # 출력 초과
RTE = 10        # 런타임 에러
CE = 11         # 컴파일 에러
DEL = 12        # 채점 불가
WAIT = 0        # 기다리는 중
# 1             # 재채점을 기다리는 중
# 2             # 채점 준비 중
JUDGING = 3     # 채점 중
UNKNOWN = -1    # (이외 결과 코드 값)

_RESULT_DICT = {
        'ac': AC, 'pac': PAC, \
        'pe': PE, 'wa': WA, 'tle': TLE, 'mle': MLE, 'ole': OLE, \
        'rte': RTE, 'ce': CE, 'del': DEL, \
        'wait': WAIT, 'judging': JUDGING
}


def get_result_code(code:str) -> int:
    return _RESULT_DICT.get(code.lower(), UNKNOWN)


