# Boyer-Moore string search algorithm implemented in Python.

# search pattern in string s
def bm_search(s, pattern):
    s_len = len(s)
    pat_len = len(pattern)
    pos = preprocess(pattern)

    offset = 0
    while offset + pat_len <= s_len:
        j = pat_len - 1
        while j >= 0 and pattern[j] == s[offset + j]:
            j -= 1
        if j < 0: # find the match
            return offset
        else:
            offset += max(1, j - pos[ord(s[offset+j])])
    return -1

def preprocess(pattern):
    pos = [-1] * 256
    for index, c in enumerate(pattern):
        pos[ord(c)] = index
    return pos

print bm_search("this is a test example", "test")
