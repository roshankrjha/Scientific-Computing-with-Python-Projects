def arithmetic_arranger(problems,bool=False):
    try:
        # Check number of arguments and throw exception if the problems are more then 5
        if len(problems) > 5:
            raise Exception("Error: Too many Problems")

        # Check operators and throw exception if the problems contains operators other then + or -
        operators = list(map(lambda x : x.split()[1], problems))
        if set(operators) != {'+','-'} and len(set(operators)) != 2:
            raise Exception("Error: Operators must be '+' or '-'")

        # Get the numbers from the problems
        numbers = []
        for i in problems:
            p = i.split()
            numbers.extend([p[0],p[2]])
        
        # Check number (operand) and throw exception if number (operand) not only contain digits
        if not all(map(lambda x : x.isdigit(), numbers)):
            raise Exception("Error: Number must be only contain digits")

        # Check number (operand) and throw exception if number (operand) is more then four digits
        if not all(map(lambda x : len(x) < 4, numbers)):
            raise Exception("Error: Number cannot be more than four digits")

        # formated Solution
        top_row = ''
        dashes = ''
        values = list(map( lambda x : eval(x), problems))
        solutions = ''
        for i in range(0, len(numbers),2):
            space_width = max(len(numbers[i]), len(numbers[i+1])) + 2
            top_row += numbers[i].rjust(space_width)
            dashes += '-' * space_width
            solutions += str(values[i//2]).rjust(space_width)
            if i != len(numbers)-2:
                top_row += ' ' * 4
                dashes += ' ' * 4
                solutions += ' ' * 4

        bottom_row = ''
        for i in range(1, len(numbers), 2):
            space_width = max(len(numbers[i-1]), len(numbers[i])) + 1
            bottom_row += operators[i//2]
            bottom_row += numbers[i].rjust(space_width)
            if i != len(numbers)-1:
                bottom_row += ' ' * 4
        
        arranged_problem = ''
        if bool:
            arranged_problem = '\n'.join((top_row,bottom_row,dashes,solutions))
        else:
            arranged_problem = '\n'.join((top_row,bottom_row,dashes))

        return arranged_problem

    except Exception as e:
        return e   

arithmetic_arranger(["32 + 8", "1 - 381", "999 + 999", "523 - 49"],True)