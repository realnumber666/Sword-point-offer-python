def bubble_sort(seq):
    '''
    n-1-i轮小循环，每次完成一个数的冒泡,把最大的数放在最后
    n-1轮大循环，冒泡n-1个数
    '''
    n = len(seq)
    for i in range(n-1):
        for j in range(n-1-i):
            if(seq[j] < seq[j+1]):
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq

def select_sort(seq):
    '''
    每次从数组中找出最小的数，放在第i位
    '''
    n = len(seq)
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if(seq[j] < seq[min_idx]):
                min_idx = j
        seq[i], seq[min_idx] = seq[min_idx], seq[i]
    return seq

def insertion_sort(seq):
    '''
    每次把第i个数放到前面已排序的数组的合适位置
    通过不断往前移动来实现
    '''
    n = len(seq)
    for i in range(1, n):
        pos = i
        while pos > 0 and seq[pos] < seq[pos-1]:
            seq[pos], seq[pos-1] = seq[pos-1], seq[pos]
            pos -= 1
    return seq
        
