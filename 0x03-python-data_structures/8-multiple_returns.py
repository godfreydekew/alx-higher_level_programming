#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence):
        return len(sentence), sentence[0]
    else:
        return 0, None
