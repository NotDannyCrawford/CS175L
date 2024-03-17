def calculate_average(file_name):
    total = 0
    count = 0
    
    with open(file_name, 'r') as file:
        for line in file:
            current_number = float(line)
            count += 1
            total += current_number
            print(f"I read in {count} number(s) Current number is: {current_number:8.2f} Total is: {total:8.2f}")
    
    average = total / count
    print(f"Average: {average}")

if __name__ == "__main__":
    calculate_average("numbers.txt")
