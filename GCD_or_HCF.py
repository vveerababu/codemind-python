def hcf(N,M):
  if M == 0:
    return N
  return hcf(M, N%M)
N,M=map(int,input().split())
print(hcf(N,M))