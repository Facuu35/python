def freq_words():
    arr=[2,3,4,1,1,2,3,4,5,4]
    d={}

    for i in arr:
        if i not in d:
            d[i]=0
        d[i]+=1
    print(arr)
freq_words()