sequence,word=input().split()
def maxRepeating(sequence: str, word: str) -> int:
    k=1
    while word * k in sequence:
        k+=1
    return k-1

