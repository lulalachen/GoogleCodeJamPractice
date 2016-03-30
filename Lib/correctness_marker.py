"""
    Correctness Marker Library
    @ Date   : 2016.03.30
    @ Author : lulalachen
"""
OKGREEN = '\033[92m'
WARNING = '\033[93m'
END = '\033[0m'
CORRECT = OKGREEN + u'\u2714' + END
WRONG = WARNING + u'\u2717' + END

def get_marker(boolean):
    """ return green check or orange cross by boolean """
    return CORRECT if boolean else WRONG
