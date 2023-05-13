#!/usr/bin/python3
def multiple_returns(sentence):

    len_ = len(sentence)
    chr = sentence[0] if len_ > 0 else None

    return (len_, chr)
