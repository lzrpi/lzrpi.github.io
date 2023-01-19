def load_data(fileName):
  with open(fileName, "r") as dummy_input:
    lines = dummy_input.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  return lines

print(lines)

