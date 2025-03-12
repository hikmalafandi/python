if __name__ == '__main__':
    n = int(input())
    i = 1
    number = []
    while(i <= n):
        number.append(i)
        i+=1
    num_string = map(str, number)
    print("".join(num_string))