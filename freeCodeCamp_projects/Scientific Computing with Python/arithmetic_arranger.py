def arithmetic_arranger(maths_problems, answers):
    '''
    input a list of arithmetic problems and then have the option to produce the answers
    '''
    
    list = []

    for i in maths:
        list.append(i.split())

    # store the answers in a list
    answer_list = []

    for i in list:
        first_number = float(i[0])
        second_number = float(i[2])
        if i[1] == "+":
             answer_list.append(first_number+second_number)
        else:
             answer_list.append(first_number-second_number)

    # create the formatting to display the arithmetic problems
    count = 0
    for i in list:
          print(i[0], end ="\n")
          print(i[1])
          print(i[2], end="\n-----\n")
          if answers == True:
              print(answer_list[count], end ="\n\n")
              count +=1
