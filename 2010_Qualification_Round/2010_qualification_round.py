# pylint: disable=C0103,E0401
"""
    Google CodeJam 2010 Qualification Round
    @ Date   : 2016.03.30
    @ Author : lulalachen
"""
# import sys
# sys.path.append('../Lib')
# from correctness_marker import get_marker

PROBLEM_COUNTS = int(raw_input())  # read a line with a single integer
for i in xrange(0, PROBLEM_COUNTS):
    CREDIT = int(raw_input())
    ITEM_COUNT = int(raw_input())
    raw_price_list = [int(price) for price in raw_input().split(" ")]
    reverse_price_list = [CREDIT - price for price in raw_price_list if CREDIT - price > 0]

    ANSWER_LIST = list(set(raw_price_list) & set(reverse_price_list))
    LENGTH_OF_ANSWER_LIST = len(ANSWER_LIST)
    if LENGTH_OF_ANSWER_LIST != 2:
        if LENGTH_OF_ANSWER_LIST == 1:
            ANSWER_LIST.append(ANSWER_LIST[0])
        if LENGTH_OF_ANSWER_LIST == 3:
            ANSWER_LIST = [price for price in ANSWER_LIST if price != CREDIT / 2]

    print 'Case #%s: %s %s' % (i+1, ANSWER_LIST[0], ANSWER_LIST[1])

    # CORRECTNESS_MARKER = get_marker(CREDIT == ANSWER_LIST[0] + ANSWER_LIST[1])
    # print 'Case #%s: %s %s %s' % (i+1, ANSWER_LIST[0], ANSWER_LIST[1], CORRECTNESS_MARKER)
