import streamlit as st

import pickle as pkl

def app():
    def logout():
        dic = {'user':'',
                    'login':False}

        with open('state.st','wb') as f:
                    pkl.dump(dic,f)



    st.markdown("<h1 style ='text-align:center' > LOG-OUT </h1>",
                        unsafe_allow_html=True)

    st.markdown("<h2 style ='text-align:center; color:red;' > WARNING </h1>",
                        unsafe_allow_html=True)

    st.write("""
            <p style ='justify-content: space-between;' >
            You are about to log out of your account. Any unsaved changes will be lost, 
            and you will be required to log in again to access your account.
            <br><br>
            Are you sure you want to continue?
            </p>
             <br>
            """,
            unsafe_allow_html=True)
    
    c1,c2,c3 = st.columns(3)


    if c2.button(':red[Yes, log out]'):
            logout()
            st.rerun()


