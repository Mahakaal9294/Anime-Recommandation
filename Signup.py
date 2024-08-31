import streamlit as st
import json
import random
import re
import pickle as pkl


def app():
    # check if the user is already registered
    def chk_user(user,email):
        with open('users.json','r') as f:
            data = json.load(f)
        for x in data['users']:
            if x['User_id'] == user:
                return 'user Id aleady exists'
            if x['Email'] == email:
                return 'Email already exists'
        return 0


    # storing the user in the database
    def store_users(user,fname,lname,age,gender,email,pswd):

        with open('users.json','r') as f:
            data = json.load(f)

        data['users'].append({'User_id':user,
                                'Fname':fname,
                                'Lname':lname,
                                'Age':age,
                                'Gender':gender,
                                'Email':email,
                                'pwsd':pswd
                                })
        data['total_users']+=1
        
        with open('users.json','w') as f:
            json.dump(data,f,indent=2)
        


    # upper, lower case letters and numerics
    char_lst = [chr(ch) for ch in range(65,91)] +[chr(ch) for ch in range(97,123) ]+[str(i) for i in range(0,10)]   
    # it contains all the letters and numbers


    # function to check if email is valid
    def email_isvalid(email):
        pat = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9].[A-Z|a-z]{2,7}'
        return re.match(pat,email)



    # Function to check password
    def check_pswd(pswd:str):

        l = u = d = s = 0

        if len(pswd) < 8:
            return 'Password length must be more than 8'
        
        for x in pswd:
            if x.islower():
                l+=1
            elif x.isupper():
                u+=1
            elif x.isdigit():
                d+=1
            elif x=='@' or x=='#' or x=='$' or x=='&':
                s+=1
        
        if l > 0 and u > 0 and s > 0 and d > 0:
            return 0
        else:
            return 'Password must include upper,lower case letter,digit and special symbol[@,#,$,&]'
        

    # Sign Up form
    with st.form('Signup',True):

        # title
        st.markdown("<h1 style ='text-align:center' > SIGN-UP </h1>",
                    unsafe_allow_html=True)
        
        # inputs of form
        c1,c2 = st.columns(2)

        fname = c1.text_input('First Name :red[*]')
        lname = c2.text_input('Last Name :red[*]')
        age = c1.number_input('Age :red[*]', min_value=15, step=1)
        gender = c2.selectbox('Gender :red[*]',['Male','Female'])
        email = st.text_input('Enter Email Address :red[*]')
        user = st.text_input('Enter user name :red[*]',max_chars=15)
        pswd = st.text_input('Enter Password :red[*]', type='password',max_chars=20)
        cnf_pswd = st.text_input('Confirm Password :red[*]', type='password',max_chars=20)


        # Checking the values entered and signing up
        if st.form_submit_button('Sign-Up'):

            if fname == '' or lname == '' or email == '' or user == '' or pswd == '' or cnf_pswd == '':
                st.warning('Please fill the Details')

            elif not email_isvalid(email):
                st.warning('Please enter valid Email Address')

            elif pswd != cnf_pswd:
                st.warning("Password not matched")
                
            elif check_pswd(pswd):
                st.warning(check_pswd(pswd))

            
            elif chk_user(user,email):
                st.warning(chk_user(user,email))

            else:
                store_users(user,fname,lname,age,gender,email,pswd)
                st.success('Account Created')
            
