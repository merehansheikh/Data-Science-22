def next_vowel(ch):
    ch=ord(ch)
    for i in range (26):
        if ch>=97 and ch<101:
            return chr(101)
        elif ch>=101 and ch<105:
            return chr(105)
        elif ch>=105 and ch<111:
            return chr(111)
        elif ch>=111 and ch<117:
            return chr(117)
        elif ch>=117:
            return chr(97)
print (next_vowel('u'))
