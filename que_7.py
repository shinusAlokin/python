
def map_two_dict():
    list_dict = {}
    list_one = input("Enter list one: ").split()
    list_two = input("Enter list two: ").split()
    if len(list_one) != len(list_two):
        print("Both list should have same length")
        return
    for i, j in zip(list_one, list_two):
        list_dict[i] = j
            
    print(list_dict)
    return list_dict
    
        
if __name__ == "__main__":                 
    map_two_dict()

        