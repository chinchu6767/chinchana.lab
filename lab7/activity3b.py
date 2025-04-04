def merge_dictionaries():
    dict1 = {}
    dict2 = {}
    
    n1 = int(input("Enter the number of elements for the first dictionary: "))
    for _ in range(n1):
        key = input("Enter key: ")
        value = int(input("Enter value: "))  
        dict1[key] = value
    
    n2 = int(input("Enter the number of elements for the second dictionary: "))
    for _ in range(n2):
        key = input("Enter key: ")
        value = int(input("Enter value: "))  
        dict2[key] = value
    
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  
        else:
            merged_dict[key] = value
    
    print("Merged Dictionary:", merged_dict)

merge_dictionaries()
