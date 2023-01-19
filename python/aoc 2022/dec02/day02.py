def solutionA(lines):
  total = 0
  for line in lines:
    if line == 'A X':
      total += 4
    
    if line == 'A Y':
      total += 8
    
    if line == 'A Z':
      total += 3

    if line == 'B X':
      total += 1

    if line == 'B Y':
      total += 5
    
    if line == 'B Z':
      total += 9

    if line == 'C X':
      total += 7
    
    if line == 'C Y':
      total += 2

    if line == 'C Z':
      total += 6

        
  return total


def solutionB(lines):
  total = 0
  for line in lines:
    if line == 'A X':
      total += 0+3
    
    if line == 'A Y':
      total += 2+2
    
    if line == 'A Z':
      total += 8

    if line == 'B X':
      total += 1

    if line == 'B Y':
      total += 5
    
    if line == 'B Z':
      total += 9

    if line == 'C X':
      total += 2
    
    if line == 'C Y':
      total += 6

    if line == 'C Z':
      total += 7

        
  return total
  
    



# Helper function for loading the problem data
def load_data(fileName):
  with open(fileName, "r") as input_data:
    lines = input_data.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  return lines


if __name__ == "__main__":
  input_file_name = "dummyinput2.txt"

  input_file_name = "day2input.txt" 

  print(f"Loading data from: {input_file_name}")
  lines = load_data(input_file_name)


  resultA = solutionA(lines)
  print(f"Solution for part A: {resultA}")

  resultB = solutionB(lines)
  print(f"Solution for part B: {resultB}")