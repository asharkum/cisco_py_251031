salaries = []

salaries.append(1000)
salaries.append(1500)
salaries.append(2000)


search = 1500

for index, salary in enumerate(salaries):
    if salary == search:
        print(f"Salary found at index: {index}")
        break

