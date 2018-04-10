t=int(input())
for i in range(t):
    a=[]
    count=0

    m=int(input())
    n=input()
    times=m//3
    last=m%3

    for i in range(times):
        a.append(n[3*i:3*(i+1)])


    if last!= 0:
        a.append(n[3*times:3*times+last])
    if len(a[-1])==2:
        a[-1]=a[-1][0:1]+"#"
    elif len(a[-1])==1:
        a[-1]=a[-1][0]+"##"

    #   把Ａ分成三個一組

    for i in range(times):
        if "." in a[i]:
            count+=1
        if i<times-1:
            if a[i]=="##.":
                a[i+1]="##"+a[i+1][2]
            elif a[i]=="#..":
                a[i+1]="#"+a[i+1][1:2]
    # 把有可能影響的全部弄掉
    print(count)