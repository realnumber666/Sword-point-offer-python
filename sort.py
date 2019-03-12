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

'''
归并排序
'''
def merge_sort(seq):
    n = len(seq)
    if(n <= 1):
        return seq
    else:
        left_half = seq[:n//2]
        right_half = seq[n//2:]
        new_seq = merge_sort_core(left_half, right_half)
        return new_seq

def merge_sort_core(left, right):
    seq = []
    i = j = 0
    while(i < len(left) and j < len(right)):
        if(left[i] > right[j]):
            seq.append(left[i])
            i += 1
        else:
            seq.append(right[j])
            j += 1
    if(i < len(left)):
        seq += left[i:]
    else:
        seq += right[j:]
    return seq


'''
快排 no in place法
以数组第一个元素为pivot，按元素大小将数组拆分为两组
对拆分后的数组再进行该操作
最后数组被分成只剩一个或零个元素时，合并时会自动变成有序的
'''
def quick_sort(seq):
    n = len(seq)
    if(n <= 1):
        return seq
    pivot = seq[0]
    left = []
    right = []
    for i in range(1, n):    
        if(seq[i] < pivot):
            left.append(seq[i])
        else:
            right.append(seq[i])
    return quick_sort(left) + [pivot] + quick_sort(right)