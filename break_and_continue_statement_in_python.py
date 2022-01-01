fruits=["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        continue            # output:   apple
                            #           cherry
    print(x)


    for y in fruits:
        if y=="banana":
            break
        print(y)