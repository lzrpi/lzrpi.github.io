def solutionA(lines):
    facit = 0
    highest_number = 0
    for line in lines:
        if line == '':
            facit = 0
        else:
            facit = facit+int(line)
            if facit > highest_number:
                highest_number = facit


    return highest_number


def solutionB(lines):
    elf1=0
    elf2=0
    elf3=0
    count=0
    for line in lines:
        if line == '':
            if count > elf3:
              elf3 = count

            if  elf3 > elf2:
              hold2 = elf2
              elf2 = elf3
              elf3 = hold2
            
            if elf2 > elf1:
              hold3 = elf1
              elf1 = elf2
              elf2 = hold3
            count = 0
        else:
            count = count+int(line)
        
        print(line,elf1,elf2,elf3)

    if count > elf3:
      elf3 = count

    if  elf3 > elf2:
      elf3,elf2=elf2,elf3
      # hold2 = elf2
      # elf2 = elf3
      # elf3 = hold2
    
    if elf2 > elf1:
      elf2,elf1=elf1,elf2
      # hold3 = elf1
      # elf1 = elf2
      # elf2 = hold3

  
    print(line,elf1,elf2,elf3)

    return elf3 + elf2 + elf1
    



# Helper function for loading the problem data
def load_data(fileName):
  with open(fileName, "r") as input_data:
    lines = input_data.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  return lines


if __name__ == "__main__":
  input_file_name = "dummy_input.txt"
  # TODO: Uncomment line below to use real input
 # input_file_name = "number_input.txt" 

  print(f"Loading data from: {input_file_name}")
  lines = load_data(input_file_name)


  resultA = solutionA(lines)
  print(f"Solution for part A: {resultA}")

  resultB = solutionB(lines)
  print(f"Solution for part B: {resultB}")