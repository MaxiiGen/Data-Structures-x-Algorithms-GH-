import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos

# Define a function to evaluate the problem expression for a given x
def evaluate_problem(problem, x):
    try:
        result = eval(problem.replace('x', str(x)))
        return result
    except Exception as e:
        return f"Error: {e}"

# Function to read the problems from the text file
def read_problems_from_file(file_name):
    with open(file_name, 'r') as file:
        problems = [line.strip() for line in file.readlines() if line.strip()]
    return problems

# Function to plot the graph for a given problem
def plot_graph(problem, x_values, y_values):
    plt.plot(x_values, y_values, label=problem)

# Function to plot all problems in one graph
def plot_all_problems(problems, x_values):
    for problem in problems:
        y_values = [evaluate_problem(problem, x) for x in x_values]
        plot_graph(problem, x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of All Problems')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function
def main():
    file_name = "maa.txt"  # Modified file name
    
    while True:
        problems = read_problems_from_file(file_name)
        
        if not problems:
            print("No problems found in the file.")
            return
        
        x_values = np.linspace(1, 50, 100)  # Generate x values from 1 to 50
        
        print("Choose an option:")
        print("1. Plot x**2 + 7*x + 2")
        print("2. Plot 3*x + 2")
        print("3. Plot x**2")
        print("4. Plot x**3")
        print("5. Plot x**5")
        print("6. Plot x**3 + 2*x**2 + x + 10")
        print("7. Plot x**4 - 3*x**3 + 2*x**2 - x + 11")
        print("8. Plot sin(x)")
        print("9. Plot cos (x)")
        print("10. Plot x**5 + 4*x**4 + x**3 - 2*x**2 + 100")
        print("11. Plot all problems in one graph")
        
        choice = input("Enter your choice (1-11): ")
        
        if choice == '11':
            plot_all_problems(problems, x_values)
        elif choice.isdigit() and 1 <= int(choice) <= 10:
            problem_index = int(choice) - 1
            problem = problems[problem_index]
            y_values = [evaluate_problem(problem, x) for x in x_values]
            plot_graph(problem, x_values, y_values)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title(f'Graph of Problem {choice}')
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            print("Invalid choice.")
        
        run_again = input("Do you want to run the program again? (yes/no): ")
        if run_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
