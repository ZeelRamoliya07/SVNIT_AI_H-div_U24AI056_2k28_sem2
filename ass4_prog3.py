def pan_gram(a):
    b=set(a.lower())
    if " " in b:
        if len(b)==27:
            return 'pangram'
        else:
            return 'not pangram'
    else:
        if len(b)==26:
            return 'pangram'
        else:
            return 'not pangram'
sent=input()
print(pan_gram(sent))