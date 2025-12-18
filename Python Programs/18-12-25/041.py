list_of_numbers=[9,8,6,5,3,4,5,7,7,8,3,2]

even_lambda_funciton=lambda x:x%2==0


print(list(filter(even_lambda_funciton,list_of_numbers)))