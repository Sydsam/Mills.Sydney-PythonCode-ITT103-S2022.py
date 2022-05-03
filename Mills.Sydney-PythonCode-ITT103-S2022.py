"""Author: Sydney Mills
Date Created: April 28, 2022
Course: ITT103
Purpose:JamEX limited requires a python code to calculate an undetermined number of salespersons, the amount of sales and the class to which a salesperson belongs.""" 


while True:
     
     salesperson_num= int(input("salesperson number:"))
     amt_sales= int(input("sales amount:"))
     sales_class= int(input("class:"))
     if (sales_class==1):
          if (amt_sales<=1000):
               print("The commision is",amt_sales*.06,"The Sales Person Number is",salesperson_num) 
          elif amt_sales >1000 and amt_sales <2000:
               print("The commision is",amt_sales*.07,"The Sales Person Number is",salesperson_num) 
          elif amt_sales<=2000:
               print("The commision is",amt_sales*.10,"The Sales Person Number is",salesperson_num)
     elif(sales_class==2):
          if  (amt_sales<1000):
               print("The commision is",amt_sales*.04,"The Sales Person Number is",salesperson_num)
          else:
               print("The commision is",amt_sales*.06,"The Sales Person Number is",salesperson_num)
     if(sales_class==3):
          print("The commision is",amt_sales*.045,"The Sales Person Number is",salesperson_num)
     else:
          ("Invalid input")
     
     
     option=input("Press X to end the loop.")
     if  option == 'X' :
          break
                              
