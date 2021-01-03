
def arithmetic_arranger(problems, compute=False):
  
  arranged_problems = ""
  cursor_pos=[0,0,0,0,0]
  first_operand=[0,0,0,0,0]
  second_operand=[0,0,0,0,0]
  answer=[0,0,0,0,0]
  problem_number = 0  # the index number of current problem
  number_of_problems = len(problems)
  if number_of_problems > 5:
    return("Error: Too many problems.")
  
  else:
    for problem in problems:
      if problem.find("*")!=-1:
        return("Error: Operator must be '+' or '-'.")
        #raise SystemExit(0)
      elif problem.find("/")!=-1:
        return("Error: Operator must be '+' or '-'.")
        #raise SystemExit(0)
      arranged_problem = ""
      for letter in problem:
        cursor_pos[problem_number]=cursor_pos[problem_number]+1
        if letter != " ":
          arranged_problem = arranged_problem + letter
        else:
          if len(arranged_problem) > 4:
            return("Error: Numbers cannot be more than four digits.")
            #raise SystemExit(0)
          elif not arranged_problem.isdigit():
            return("Error: Numbers must only contain digits.")
            #raise SystemExit(0)
          
          break
      first_operand[problem_number]=arranged_problem
      arranged_problem=arranged_problem.rjust(8)
      arranged_problems = arranged_problems + arranged_problem
      
      problem_number = problem_number+1
    arranged_problems = arranged_problems + "\n"
    
    problem_number=0
    arranged_problem=arranged_problem.rjust(8)
    for problem in problems:
      arranged_problem=""
      
      problem = problem[cursor_pos[problem_number]:len(problem)]
      if len(problem[2:len(problem)].lstrip()) > 4:
        return("Error: Numbers cannot be more than four digits.")
        #raise SystemExit(0)
      elif not problem[2:len(problem)].lstrip().isdigit():
        return("Error: Numbers must only contain digits.")
        #raise SystemExit(0)
      for letter in problem:
        
        arranged_problem = arranged_problem + letter
        
      
      second_operand[problem_number]=arranged_problem
      while len(second_operand[problem_number]) < len(first_operand[problem_number])+2:
        second_operand[problem_number] =second_operand[problem_number][0:1]+" "+second_operand[problem_number][1:len(second_operand[problem_number])]
      #while len(first_operand[problem_number]) < len(second_operand[problem_number])-1:
      #  first_operand[problem_number] =first_operand[problem_number][0:1]+" "+first_operand[problem_number][1:len(first_operand[problem_number])]
      second_operand[problem_number]=second_operand[problem_number].rjust(8)  
      arranged_problems = arranged_problems + second_operand[problem_number]
      problem_number = problem_number+1
    arranged_problems = arranged_problems + "\n   -----   -----   -----   -----"
  
    if (compute):
      arranged_problems = arranged_problems + "\n"
      i=0
      while i<number_of_problems:
        answer[i]=(eval(first_operand[i] + second_operand[i]))
        arranged_problems = arranged_problems + str(answer[i]).rjust(8) 
        i=i+1
        
    return arranged_problems
