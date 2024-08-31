import streamlit as st
import json
import pickle as pkl

with open('users.json','r') as f:
    data = json.load(f)

def app():
    # Setting the login value to True
    def set_state():
        dic = {'user':user,
            'login':True}
        
        with open('state.st','wb') as f:
            pkl.dump(dic,f)
        

    # Checking if the user is registered
    def chk_user(user,pswd):
        for x in data['users']:
            if x['User_id'] == user and x['pwsd'] == pswd:
                set_state()
                return 0
        return 1

    # Creating Form for login
    with st.form('Login',True):

        # title
        st.markdown("<h1 style ='text-align:center' > LOGIN </h1>",
                    unsafe_allow_html=True)

        #getting the Inputs
        user = st.text_input('Enter user ID')
        pswd = st.text_input('Enter Password',type='password')


        if st.form_submit_button('Login'):

            # checking if inputs are null
            if user =='' or pswd == '':
                st.warning('Please Enter User Id and Password')

            # checking if the user has entered correct user_id and password
            elif chk_user(user,pswd):
                st.warning('Invalid User Id or Password')

            else:
                set_state()
                st.success('Login Successfull')
                st.rerun()