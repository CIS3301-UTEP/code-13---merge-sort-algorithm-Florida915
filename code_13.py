def get_merge_sorted_list(unsorted_list):
    if len(unsorted_list)==1:
        return unsorted_list

unsorted_list= [2,3,4,5,6,1,7]
mid_point = int((len(unsorted_list))//2)

first_part = unsorted_list[:mid_point]
second_part =unsorted_list[mid_point:]

half_a = get_merge_sorted_list(first_part)
half_b = get_merge_sorted_list(second_part)

    

if __name__ == "__main__":

    print(get_merge_sorted_list(unsorted_list))