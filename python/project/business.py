# IMPORTING LIBRARIES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import warnings


# DECLARING VARIABLES

# USER INPUT LIST
name = []
age = []
loc = []
cat = []
subcat = []
year = []

# ADMIN INPUT LIST
cat_list = []
cat_sub = {}

# GUEST INPUT
file_name = 'categories.txt'

class Business:

    a = ''
    auth = False

    def __init__(self):
        print('''
            SELECT YOUR CHOICE :
                1. ADMIN
                2. USER
                3. GUEST
        ''')

        enter = int(input('Enter your Choice : '))

        if (enter == 1):
            admin_username = input('ENTER USERNAME : ')
            admin_password = input('ENTER PASSWORD : ')
            if (self.auth == False):
                if (admin_username == 'admin123' and admin_password == 'password'):
                    self.admin(cat_list,self.subcategory)
                    self.a = 'TASK COMPLETED SUCCESSFULLY'
                    self.auth = True
                else:
                    print('INVALID USERNAME OR PASSWORD')
                    self.a = 'INVALID USERNAME OR PASSWORD'
                    self.__init__()
            else:
                self.add_category(self.new_cat_list)
        elif (enter == 2):
            self.business(name,age,loc,cat,subcat,year)
            self.a = 'TASK COMPLETED SUCCESSFULLY !!!'
        elif (enter == 3):
            self.intro(file_name,read=True)
        else:
            print('PLEASE ENTER A VALID NUMBER')
            self.a = 'PLEASE ENTER A VALID NUMBER'
            self.__init__()

    def business(self,name,age,loc,cat,subcat,year):

        for i in range(1):
            print('USER NO. : ',i+1)

            user_name = input('Enter your Name : ')
            user_age = int(input('Enter your Age : '))
            user_loc = input('Enter your Location : ')
            user_cat = self.category()
            user_subcat = self.subcategory(self.category())
            user_year = datetime.datetime.now().year

            name.append(user_name.capitalize())
            age.append(user_age)
            loc.append(user_loc.upper())
            cat.append(user_cat.capitalize())
            subcat.append(user_subcat.capitalize())
            year.append(user_year)

        self.data_to_csv(name,age,loc,cat,subcat,year)

    def admin(self,category,subcategory):

        n = int(input('Enter the No. of Categories want to be Added : '))

        for i in range(n):

            print('\n ======================= STARTED CATEGORY {} =========================== \n'.format(i+1))

            print('Category No. :',i+1)
            user_category = input('Enter the Category : ')
            cat_list.append(user_category.capitalize())

            for k in cat_list:
                cat_sub.setdefault(k)

            m = int(input('Enter the No. of Sub Categories want to be added for the above Category : '))

            subcat_list = []

            for j in range(m):
                
                print('Sub Category No. :',j+1)
                user_sub_category = input('Enter the Sub-Category : ')
                subcat_list.append(user_sub_category.capitalize())

                cat_sub[k] = subcat_list

            print('\n ======================= ENDED CATEGORY {} =========================== \n'.format(i+1))

    
    def category(self):

        for i,each in enumerate(cat_list):
            print('{}. {} \t \t'.format(i+1,each),end='')
            if i % 4 == 3: 
                print("\n")

        print('\n')
        cat = int(input('Enter the No. : '))
        return cat_list[cat-1]

    
    def subcategory(self,cat_value):

        print('\n')
        print('THE CATEGORY IS : {}'.format(cat_value))
        for i,each in enumerate(cat_sub[cat_value]):
            print('{}. {} \t \t'.format(i+1,each),end='')
            if i % 4 == 3: 
                print("\n")
        print('\n')
        print('THE SUB CATEGORY OF {} IS : '.format(cat_value))
        print('\n')
        subcat = int(input('Enter the No. : '))
        print('SUBCATEGORY IS : {}'.format(cat_sub[cat_value][subcat-1]))
        return cat_sub[cat_value][subcat-1]

    new_cat_list = []
    new_cat_sub = {}

    def add_category(self,new_cat):

        n = int(input('Enter the No. of Categories want to be Added : '))

        for i in range(n):

            print('\n ======================= STARTED CATEGORY {} =========================== \n'.format(i+1))

            print('Category No. :',i+1)
            user_category = input('Enter the Category : ')
            self.new_cat_list.append(user_category.capitalize())

            cat_list.extend(self.new_cat_list)

            for k in self.new_cat_list:
                self.new_cat_sub.setdefault(k)

            m = int(input('Enter the No. of Sub Categories want to be added for the above Category : '))

            new_subcat_list = []

            for j in range(m):
                
                print('Sub Category No. :',j+1)
                user_sub_category = input('Enter the Sub-Category : ')
                new_subcat_list.append(user_sub_category.capitalize())

                self.new_cat_sub[k] = new_subcat_list

            print('\n ======================= ENDED CATEGORY {} =========================== \n'.format(i+1))

        return cat_sub.update(self.new_cat_sub)



    def data_to_csv(self,name,age,loc,cat,subcat,year):

        dict = {
            'name': name,
            'age': age,
            'location': loc,
            'category': cat,
            'subcategory': subcat,
            'year': year
        }

        df = pd.DataFrame(dict)
        csv = df.to_csv('data.csv', index=False)

        return csv

    def intro(self,file_name,read=False):
        
        f = open(file_name,'w')
        f.write('CATEGORY AND SUBCATEGORY')
        f.write('\n')

        f.write("=======================================")
        f.write('\n')
        f.write("|  CATEGORY NO.  | CATEGORY NAME |")
        f.write('\n')
        f.write("=======================================")
        f.write('\n')
        for i,cat_each in enumerate(cat_sub,start=1):
            f.write("|   {}    |   {}   ".format(str(i).center(9),cat_each))
            f.write('\n')
            f.write(" \t \t | SUB CATEGORY NO. | SUB CATEGORY NAME |")
            f.write('\n')
            for j,subcat_each in enumerate(cat_sub[cat_each],start=1):
                f.write(" \t \t |   {}    |   {}   ".format(str(j).center(11),subcat_each))
                f.write('\n')

        if(read==True):
            f = open(file_name,'r')
            print(f.read())
            f.close()

    def __str__(self):
        return self.a
