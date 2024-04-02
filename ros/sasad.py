import sys
from math import sin, cos

# Define a function to read the problems from the text file
def read_problems_from_file(file_name):
    with open(file_name, 'r') as file:
        problems = [line.strip() for line in file.readlines() if line.strip()]
    return problems

# Function to process each problem for x values from 1 to 50
def process_problems(problems):
    results = [[] for _ in range(50)]  # List of 50 lists to store results for each x value
    
    for x in range(1, 51):  # x values from 1 to 50
        for index, problem in enumerate(problems):
            try:
                # Evaluating the expression for the current x value
                result = eval(problem.replace('x', str(x)))
                results[x-1].append(result)
            except Exception as e:
                results[x-1].append(f"Error: {e}")
    
    return results

# Main function
def main():
    file_name = "maa.txt"  # Modified file name
    problems = read_problems_from_file(file_name)
    if problems:
        results = process_problems(problems)
        with open("maad.txt", 'w') as output_file:
            original_stdout = sys.stdout
            sys.stdout = output_file  # Redirect stdout to the file
            for x in range(50):
                print(f"For x = {x+1}: {results[x]}")
            sys.stdout = original_stdout  # Reset stdout
        print("Output has been saved to 'maad.txt'.")

if __name__ == "__main__":
    main()
