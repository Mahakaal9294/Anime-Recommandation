import streamlit as st
import pickle as pkl
import json

with open('state.st','rb') as f:
    data = pkl.load(f)
    user_id = data['user']


with open('users.json','r') as f:
    data = json.load(f)


def app():

    Fname =  Lname = Age = Gender = Email = ''

    for x in data['users']:
        if x['User_id'] == user_id:
              Fname = x['Fname']
              Lname = x['Lname']
              Age = x['Age']
              Gender = x['Gender']
              Email = x['Email']

    st.markdown("<h1 style ='text-align:center' > PROFILE </h1>",
                        unsafe_allow_html=True)


    with st.container(border=True):
        c1,c2 = st.columns([3,7])

        c1.image('img/profile.jpg',)

        with c2:
            st.write(f"<p style ='justify-content: space-between;' ><b>USER ID:</b> {user_id}</p>",
                    unsafe_allow_html=True)
            st.write(f"<p style ='justify-content: space-between;' ><b>FIRST NAME:</b> {Fname}</p>",
                    unsafe_allow_html=True)
            st.write(f"<p style ='justify-content: space-between;' ><b>LAST NAME:</b> {Lname}</p>",
                    unsafe_allow_html=True)
            st.write(f"<p style ='justify-content: space-between;' ><b>AGE:</b> {Age}</p>",
                    unsafe_allow_html=True)
            st.write(f"<p style ='justify-content: space-between;' ><b>GENDER:</b> {Gender}</p>",
                    unsafe_allow_html=True)
            st.write(f"<p style ='justify-content: space-between;' ><b>EMAIL:</b> {Email}</p>",
                    unsafe_allow_html=True)
            
