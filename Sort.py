def sortAndFindMedian(numbers):
    numbers = sort(numbers)
    n = len(numbers)

    if n % 2 == 0:
        return numbers[n/2-1] + numbers[n/2]/2
    else:
        return numbers[n//2]

def sort(numbers):
    i = 0

    while i < len(numbers)-1:                                                                                           # loop from the first character to the second to last
        j = i + 1                                                                                                       # get the next character to the right
        while j < len(numbers):                                                                                         # loop till the last character
            if numbers[i] > numbers[j]:                                                                                 # if the next character is greater than the current char
                temp = numbers[i]                                                                                       # save a copy of the current char before overwriting
                numbers[i] = numbers[j]                                                                                 # swap the current character and the next character
                numbers[j] = temp
            j += 1
        i += 1

    return numbers