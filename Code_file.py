def missing_number(array):
    array = [1, 2, 3, 4, 5, 7, 8, 9]
    m = len(array) + 1
    total = (m*(m+1))/2
    print(total)
    return (total - sum(array))

def pair_array(sum):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0
    n = len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count

def check_fibo(num):
    first = 0
    second = 1
    third = 0
    while(third< num):
        third = first + second
        first = second
        second = third
    if(third == num):
        print("yes it is there")
    else:
        print("Not found")

def rev_word(string_text):
    empty_list = []
    for i in range(0,len(string_text)):
        if(string_text[i]!=" "):
            empty_list.append(string_text[i])
        else:
            while len(empty_list)>0:
                print(empty_list[-1], end = "")
                empty_list.pop()
            print(end = " ")

def check_num(num):
    new_num = num*2
    list_new = []
    res = [int(x) for x in str(num)]
    res2 = [int(x) for x in str(new_num)]
    res.sort()
    res2.sort()
    if(res== res2):
        print("both are equal")


check_num(34875)

