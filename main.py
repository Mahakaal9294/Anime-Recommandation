import streamlit as st
from streamlit_option_menu import option_menu
import pickle as pkl

import About_Us, Home, Information, Login, Logout, Profile, Recommender, Signup


# setting up the page
st.set_page_config(
    page_title='Recommender',
    page_icon=":space_invader:"
)


with open('state.st','rb') as f:
    data = pkl.load(f)

if data['login']:
    with st.sidebar:
        option = option_menu(
            menu_title='Main Menu',
            menu_icon='menu-app-fill',
            options=['Home','Recommender','Information','Profile','About us','Logout'],
            icons=['house-fill','search-heart','info-circle','person-circle','file-earmark-person','box-arrow-right']
        )

    if option == 'Home':
        Home.app()
    elif option == 'Recommender':
        Recommender.app()
    elif option == 'Information':
        Information.app()
    elif option == 'Profile':
        Profile.app()
    elif option == 'About us':
        About_Us.app()
    elif option == 'Logout':
        Logout.app()


else:
    with st.sidebar:
        option = option_menu(
            menu_title='Main Menu',
            menu_icon='menu-app-fill',
            options=['Home','Login','Signup','Information','About us'],
            icons=['house-fill','box-arrow-in-left','at','info-circle','file-earmark-person']
        )
    if option == 'Home':
        Home.app()
    elif option == 'Login':
        Login.app()
    elif option == 'Information':
        Information.app()
    elif option == 'Signup':
        Signup.app()
    elif option == 'About us':
        About_Us.app()