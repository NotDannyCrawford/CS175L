# Danny Crawford
# CS 175L
# 4-16-2024


# CLASS EXAMPLE I USED FOR REFERENCE (thank)
'''import matplotlib.pyplot as plt

def main():
    # Create a list of sales amounts.
    sales = [100, 400, 300, 600]

    # Create a list of labels for the slices.
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']

    # Create a pie chart from the values.
    plt.pie(sales, labels=slice_labels)

    # Add a title.
    plt.title('Sales by Quarter')
    
    # Display the pie chart.
    plt.show()

# Call the main function.
if __name__ == '__main__':
    main()'''

import matplotlib.pyplot as plt

def main():
    try:
        with open('expenses.txt', 'r') as file:
            expenses = []
            labels = []
            

            for line in file:
                try:
                    category, amount = line.split('\t')
                    amount = int(amount)
                    labels.append(category)
                    expenses.append(amount)
                except ValueError:
                    print(f"Error converting amount to integer for category {category.strip()}. Skipping.")
                    
        plt.pie(expenses, labels=labels)
        plt.title('Monthly Expenses')
        plt.show()
    
    except IOError:
        print("Error opening or reading from the file.")

if __name__ == '__main__':
    main()
