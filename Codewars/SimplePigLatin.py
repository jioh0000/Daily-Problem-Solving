def pig_it(text):
    arr = text.split()
    ans = ""
    for i in arr:
        if i == '!' or i == '?' or i == ".":
            val = i
        else:
            val = i[1:] + i[0] + "ay"
        ans += (val + " ")
    
    text = ans[0:-1]
    return text