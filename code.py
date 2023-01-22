1. #WAP to find largest elt in an array and replace it with a string/number.
def entry(number_of_elts, array):
    for elts in range(number_of_elts):
        num = int(input(f"Enter the {elts + 1} number: "))
        array.append(num)
    return array
def max_num(array):
    max = 0
    for each in range(len(array)):
        if array[each] > max:
            max = array[each]
            index = each
    return index
def replace():
    array = []
    number_of_elts = int(input("Enter how many numbers do you want to enter into the array: "))
    entered_array = entry(number_of_elts, array)
    index = max_num(entered_array)
    choice = input("Do you want to replace the largest number with a string or a number?: ").lower()
    if choice == "number":
        number = int(input("Enter the number: "))
        entered_array[index] = number
    else:
        user_string = input("Enter the string of your choice: ")
        entered_array[index] = user_string
    print(f"The updated array is: {entered_array}")
replace()
