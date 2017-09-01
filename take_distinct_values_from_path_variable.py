a = "take path variables in a variable. it should be C:\\abc\\def and not single slashes"
a_split = a.split(';')
len(a_split)
a_split_set = set(a_split) # to convert the list to a set, during the conversion it will automatically take only the distinct values in the list
len(a_split_set)
a_split_list = list(a_split_set) # to covert the set to list
a_split_list_path = ';'.join(a_split_list)
a_split_list_path
