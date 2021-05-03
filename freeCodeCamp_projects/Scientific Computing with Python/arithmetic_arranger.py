def arithmetic_arranger(maths_problems, answers):

    list = []

    for i in maths:
        list.append(i.split())

    answer_list = []

    for i in list:
        first_number = float(i[0])
        second_number = float(i[2])
        if i[1] == "+":
             answer_list.append(first_number+second_number)
        else:
             answer_list.append(first_number-second_number)

    #formatting
    count = 0
    for i in list:
          print(i[0], end ="\n")
          print(i[1])
          print(i[2], end="\n-----\n")
          if answers == True:
              print(answer_list[count], end ="\n\n")
              count +=1
