def lst_to_flat(n_list):
   for item in n_list:
       if isinstance(item, list):
           for i in item:
               yield i

if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None]
    ]

    for item in lst_to_flat(nested_list):
        print(item)