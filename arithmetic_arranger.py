def arithmetic_arranger(problems, compute=False):
  arranged_problems = ""
  cursor_pos=[0,0,0,0,0]
  first_operand=[0,0,0,0,0]
  first_operand_length=[0,0,0,0,0]
  second_operand=[0,0,0,0,0]
  second_operand_length=[0,0,0,0,0]
  answer=[0,0,0,0,0]
  problem_number = 0  # the index number of current problem
  number_of_problems = len(problems)
  if number_of_problems > 5:
    return("Error: Too many problems.")
  
  for problem in problems:
    if problem.find("*")!=-1:
      return("Error: Operator must be '+' or '-'.")
    elif problem.find("/")!=-1:
      return("Error: Operator must be '+' or '-'.")
    first_operand[problem_number] = ""
    for letter in problem:
      cursor_pos[problem_number]=cursor_pos[problem_number]+1
      if letter != " ":
        first_operand[problem_number] = first_operand[problem_number] + letter
      else:
        if len(first_operand[problem_number]) > 4:
          return("Error: Numbers cannot be more than four digits.")
        elif not first_operand[problem_number].isdigit():
          return("Error: Numbers must only contain digits.")
        break
    problem_number = problem_number+1
  problem_number=0
    
  for problem in problems:
    second_operand[problem_number]=""
    problem = problem[cursor_pos[problem_number]:len(problem)]
      
    if len(problem[2:len(problem)].lstrip()) > 4:
      return("Error: Numbers cannot be more than four digits.")
        
    elif not problem[2:len(problem)].lstrip().isdigit():
      return("Error: Numbers must only contain digits.")
    for letter in problem:
       second_operand[problem_number] = second_operand[problem_number] + letter
    while len(second_operand[problem_number]) < len(first_operand[problem_number])+2:
      second_operand[problem_number] =second_operand[problem_number][0:1]+" "+second_operand[problem_number][1:len(second_operand[problem_number])]
    second_operand_length[problem_number]=len(second_operand[problem_number])
    problem_number = problem_number+1
  
  problem_number = 0
  for problem in problems:
    if problem_number < len(problems)-1:
      first_operand[problem_number] = first_operand[problem_number].rjust(len(second_operand[problem_number])) + "    "
    else:
      first_operand[problem_number] = first_operand[problem_number].rjust(len(second_operand[problem_number]))
    arranged_problems = arranged_problems + first_operand[problem_number]
    problem_number = problem_number+1

  arranged_problems = arranged_problems +"\n"
  problem_number = 0
    
  for problem in problems:
    if problem_number < len(problems)-1:
      second_operand[problem_number]=second_operand[problem_number].rjust(len(second_operand[problem_number])) + "    "
    else:
      second_operand[problem_number]=second_operand[problem_number].rjust(len(second_operand[problem_number]))

    arranged_problems = arranged_problems + second_operand[problem_number]
    problem_number = problem_number+1
  arranged_problems = arranged_problems +"\n"
  
  # add the 'sum' dotted lines
  for i in range(number_of_problems):
    line=""
    y = second_operand_length[i]
    while y>0:
      line = line + "-"
      y=y-1
    
    if i < number_of_problems-1:
      
      arranged_problems = arranged_problems + line + "    "
    else:
      arranged_problems = arranged_problems + line
  
  # optionally evaluate the sum 
  if (compute):
    arranged_problems = arranged_problems + "\n"  
    i=0
    while i<number_of_problems:
      answer[i]= str(eval(first_operand[i] + second_operand[i]))
        
      
      answer[i] = answer[i].rjust(second_operand_length[i])
      arranged_problems = arranged_problems + answer[i] + "    "
        
      i=i+1
    arranged_problems = arranged_problems.rstrip()
  return arranged_problems
