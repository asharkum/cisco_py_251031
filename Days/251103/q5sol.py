nums_str = input("Enter numbers = ")
nums_str_list = nums_str.split()
nums = [] 

for num in nums_str_list:
    nums.append(int(num))

min =  max = nums[0]

for num in nums:
    if num < min:
        min = num
    if num > max:
        max = num

with open("minmaxdata.txt", "w") as file:
    file.write(f"Maximum = {max}\n")
    file.write(f"Minimum = {min}\n")

with open("minmaxdata.txt", "r") as file:
    content = file.read()
    print(content)