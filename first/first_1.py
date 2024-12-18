def radix_sort(arr):

    # Find the maximum value in the array to determine the number of digits
    # for this case, it is 5
    max_value = max(arr)
    num_digits = len(str(max_value))

    # Perform counting sort for each digit, starting from the least significant digit
    for exp in range(num_digits):
        arr = counting_sort(arr, exp)

    return arr

def counting_sort(arr, exp):
    """
    Sorts an array of integers using counting sort based on the digit at the given exponent.
    """

    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Assuming base 10

    # Count the occurrences of each digit
    for i in range(n):
        index = (int(arr[i]) // (10 ** exp)) % 10
        count[index] += 1

    # Calculate the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (int(arr[i]) // (10 ** exp)) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    return output

if __name__ == '__main__':

    leftArray = []
    rightArray = []
    count = 0

    with open('input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            temp = line.strip().split()
            leftArray.append(temp[0])
            rightArray.append(temp[1])
            count += 1

    leftArray = radix_sort(leftArray)
    rightArray = radix_sort(rightArray)

    sum = 0
    for i in range(count):
        sum += abs(int(leftArray[i]) - int(rightArray[i]))

    print(sum)



