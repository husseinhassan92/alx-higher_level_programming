#!/usr/bin/python
def multiple_returns(sentence):
    len_ = len(sentence)
    chr_ = sentence[0] if len_ > 0 else None
    return (len_, chr_)
