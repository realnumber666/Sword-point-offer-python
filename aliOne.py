input_arr = [{"name": "a", "birth": 1}]

def sort_birth(input_arr):
  length = len(input_arr)
  i = 0
  birth_set = {}

  # 初始化set
  for i in range(length):
    birth = input_arr[i].birth
    # key中还未放入元素
    if (!birth_set[birth].value):
      birth_set[birth] = [input_arr[i]]
    else:
      birth_set[birth].append(input_arr[i])

  # 获得所有key的数组
  key_arr = birth_set.keys()
  key_arr = key_arr.sort()
  #def quick_sort(arr):
  #	n = len(arr)
   #   # 递归出口
    #  if (n <= 1):
     #   return arr
      #pivot = arr[0]
      #for i in 

  tol_arr = []
  for key in key_arr:
      arr = birth_set[key]
      tol_arr += arr

  return tol_arr