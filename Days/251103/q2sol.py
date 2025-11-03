nums_str = input("Enter numbers separated by spaces: ")
nums_str = nums_str.split()
nums = []

for num in nums_str:
    nums.append(int(num))

sum = 0
for num in nums:
    sum += num

avg = sum / len(nums)

with open('numbers_data.txt', 'w') as output_file:
    output_file.write(f'Numbers: {nums}\n')
    output_file.write(f'Sum: {sum}\n')
    output_file.write(f'Average: {avg}\n')

with open('numbers_data.txt', 'r') as output_file:
    content = output_file.read()
    print(content)
