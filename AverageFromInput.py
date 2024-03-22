def calculate_average(file_name):
    total = 0
    count = 0
    
    try:
        with open(file_name, 'r') as file:
            for line in file:
                try:
                    current_number = float(line)
                    count += 1
                    total += current_number
                    print(f"I read in {count} number(s) Current number is: {current_number:8.2f} Total is: {total:8.2f}")
                except ValueError:
                    print(f"Bad data: {line.strip()} skipping")
        
        if count > 0:
            average = total / count
            print(f"Average: {average}")
        else:
            print("No valid numbers were read from the file.")
    except IOError:
        print(f"SystemExit: File not found: {file_name} – exiting")

if __name__ == "__main__":
    calculate_average("numbers.txt")
