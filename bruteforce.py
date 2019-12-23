import paa
import trie
import d


class BRUTEFORCE:
    def __init__(self):
        pass 

    def calc(self, s, n, D=d.Euclid):
        cur_best_answer = float('-inf')
        cur_best_index = -1
        m = len(s)
        for i in range(m - n + 1):
            cur_min_dist = float('inf')
            for j in range(m - n + 1):
                if abs(i - j) >= n:
                    cur_dist = D(s[i:i+n], s[j:j+n])
                    cur_min_dist = min(cur_min_dist, cur_dist)
                    if cur_dist < cur_best_answer:
                        break
                    
            if cur_best_answer < cur_min_dist:
                cur_best_answer = cur_min_dist
                cur_best_index = i
        
        return (cur_best_index, cur_best_answer)

if __name__ == '__main__':
    s = [1.1, 1.1, 1.1, 2.2, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1]
    print(BRUTEFORCE().calc(s, 4, 2))