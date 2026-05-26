import random
def main():
    range_of_lst = int(input("Enter an integer number for the range: "))
    lst = generate_list(range_of_lst)
    list_of_peaks = peak_finder(lst)
    maximum = max_element(lst)
    print(lst)
    print(list_of_peaks)
    print(maximum)
        
        
"""
   Naive function for finding the peaks
   Takes as input a list of numbers and
   gives us output all the local peaks in
   that list
   Edit - This is not naive if we need to find all the local peaks
   and if we need to find the maximum element,this method works 
   and not the divide and conquer O(log(n)) one which just finds
   one peak so this is not naive
"""
def peak_finder(lst):
    #Checking for the case if a list with single element
    if len(lst) == 1:
        return lst
    #initializing an empty list which
    # .. will catch all the local
    #.. peaks
    peaks = []
    for i in range(len(lst)):
        element_at_i = lst[i]
        # Edge case when the first
        #..element of the list is being checked
        if i == 0 :
            if element_at_i >= lst[i+1]:
                peaks.append(element_at_i)
        # Edge case when the last element of the list checked
        elif i == len(lst) - 1 :
            if element_at_i >= lst[i - 1]:
                peaks.append(element_at_i)
        # Logic for checking the rest of the list except
        #.. the edge cases
        elif  lst[i - 1] <= element_at_i >= lst[i + 1]:
            peaks.append(element_at_i)
    return peaks
"""
   Function for finding the maximum element in that list
   Input - A list of which the maximum we need to find
   Output - The max element in that list
   We keep iterating until we reach a single element
   To avoid getting stuck in local maximums,we check if the 
   length of the new lists of the peaks after every iteration
   is changing or not.If the length is not changing then this
   implies that all the elements in this new peak list are eq
   ual,ie,the numbers are the peak and we just get the first
   element from the list which is the maximum
"""
   
def max_element(lst):
    while len(lst) > 1:
        new_peaks = peak_finder(lst)
        if len(new_peaks) == len(lst):
            break
        lst = new_peaks
    max_element = lst[0]
    return max_element

"""
   Function for generating a list of random numbers 
   within a specified range by the user
"""
def generate_list(num_range):
    rand_lst=[]
    for i in range(num_range):
        element_to_be_added = random.randint(1,10)
        rand_lst.append(element_to_be_added)
    return rand_lst

        


if __name__ == "__main__":
    main()