
def arithmetic_arranger(problems):
  
  arranged_problems = ""
  cursor_pos=[0,0,0,0]
  problem_number = 0  # the index of current problem
  number_of_problems = len(problems)
  if number_of_problems > 4:
    print("Error: Too many problems.")
  
  else:
    for problem in problems:
      if problem.find("*")!=-1:
        print("Error: Operator must be '+' or '-'.")
        raise SystemExit(0)
      elif problem.find("/")!=-1:
        print("Error: Operator must be '+' or '-'.")
        raise SystemExit(0)
      arranged_problem = ""
      for letter in problem:
        cursor_pos[problem_number]=cursor_pos[problem_number]+1
        if letter != " ":
          arranged_problem = arranged_problem + letter
        else:
          arranged_problem=arranged_problem.rjust(8)
          break
      arranged_problems = arranged_problems + arranged_problem
      
      problem_number = problem_number+1
    arranged_problems = arranged_problems + "\n"
    
    problem_number=0
    arranged_problem=arranged_problem.rjust(8)
    for problem in problems:
      arranged_problem=""
      
      problem = problem[cursor_pos[problem_number]:len(problem)]
      
      for letter in problem:
        
        arranged_problem = arranged_problem + letter
        
      arranged_problem=arranged_problem.rjust(8)  
      arranged_problems = arranged_problems + arranged_problem 
      problem_number = problem_number+1
    arranged_problems = arranged_problems + "\n   -----   -----   -----   -----"
    return arranged_problems
