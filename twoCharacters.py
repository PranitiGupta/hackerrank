import sys
def validate(string):
    for i in range(1, len(string)):
        if string[i]==string[i-1]:
            return False
    return True
    
def unique_letters(s):
    ul= list()
    for i in sorted(s):
        if not ul or i!= ul[-1]:
            ul.append(i)
    return ul

if __name__ == '__main__':
    s_len = int(raw_input().strip())
    s = raw_input().strip()
    maxLength= 0
    ul= unique_letters(s)
    for i in range(len(ul)):
        for j in range(i+1, len(ul)):
            string= ''.join([c for c in s if c==ul[i] or c==ul[j]])
            if string.isalpha() and validate(string):
                mylength= len(string)
                if mylength> maxLength:
                    maxLength= mylength
    print maxLength
    
