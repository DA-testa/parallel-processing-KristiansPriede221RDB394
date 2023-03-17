# python3
import heapq
def main():
    info=[]
    i=0
    while i<2:
        inpt=input()
        info.append(inpt)
        i=i+1
    f=info[0].split(' ')
    n=int(f[0])
    m=int(f[1])

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data=list(map(int,info[1].split(' ')))
    output = []
    for i in range(n):
        heapq.heappush(output,(0,i))
    for i in range(m):
        f,s= heapq.heappop(output)
        print(s,f)
        heapq.heappush(output,(data[i]+f,s))  
if __name__ == "__main__":
    main()
