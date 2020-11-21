from collections import defaultdict
import sys
S = input()
dist_cnt = len(set(list(S)))
n = len(S)
freq = defaultdict(int)
start_idx = 0
min_len = sys.maxsize
dist = 0 
for j in range(n):
    freq[S[j]] += 1
    if freq[S[j]] == 1:
      dist += 1    
    if dist_cnt == dist:
      while freq[S[start_idx]] > 1:
        if freq[S[start_idx]] > 1:
          freq[S[start_idx]] -= 1
        start_idx += 1      
      curr_len = j - start_idx + 1
      min_len = min(min_len, curr_len)
print(min_len)
