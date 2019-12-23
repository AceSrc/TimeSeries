import haar
import trie
import d


class WAT:
    def __init__(self):
        pass 

    def calc(self, s, order, D=d.Euclid):
        self.trie = trie.Trie()
        m = len(s)
        n = 2 ** order
        for i in range(0, m - n + 1):
            word = haar.HAAR2CHAR(s[i:i+n], order)
            self.trie.add(i, word)
        

        cur_best_answer = float('-inf')
        cur_best_index = -1
        for (i, cnt, leaf) in self.trie.get_outter_order():
            cur_min_dist = float('inf')
            for j in self.trie.get_inner_order(leaf):
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
    print(WAT().calc(s, 2))