# pylint: disable=C0103
"""
    Google CodeJam 2010 Qualification Round
    @ Date   : 2016.03.30
    @ Author : lulalachen
"""
PROBLEM_COUNTS = int(raw_input())  # read a line with a single integer
for i in xrange(0, PROBLEM_COUNTS):
    CREDIT = int(raw_input())
    ITEM_COUNT = int(raw_input())
    raw_price_list = [int(price) for price in raw_input().split(" ")]
    inverse_price_list = [CREDIT - price for price in raw_price_list if CREDIT - price > 0]

    ANSWER_LIST = list(set(raw_price_list) & set(inverse_price_list))
    if len(ANSWER_LIST) == 1:
        ANSWER_LIST.append(ANSWER_LIST[0])
    print 'Case #%s: %s %s' % (i+1, ANSWER_LIST[0], ANSWER_LIST[1])
