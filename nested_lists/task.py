result =[]
score_list = []


if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result +=[[name,score]]
        score_list+=[score]
    b = sorted(list(set(score_list)))[1]

    for a,c in sorted(result):
        if c==b:
            print(a)