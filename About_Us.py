import streamlit as st


def app():
    st.markdown("<h1 style ='text-align:center' > ABOUT US </h1>",
                        unsafe_allow_html=True)


    st.write("""
                <p style ='justify-content: space-between;' >
                Welcome to <b>Epc-Finds</b>, your go-to destination for discovering your next
                favorite anime! Our project, built with Python, is designed to provide 
                tailored anime recommendations based on your preferences and viewing 
                history. Whether you're a seasoned otaku or just starting your anime journey,
                <b>Epc-Finds</b>, leverages advanced algorithms to suggest shows you'll love.
                </p>
                """,
                unsafe_allow_html=True)



    st.write("<h2>Our Mission</h2>",unsafe_allow_html=True)

    st.write("""
                <p style ='justify-content: space-between;' >
                At <b>Epc-Finds</b>, our mission is to enhance your anime-watching experience by 
                making it easier to find high-quality shows that match your taste. We believe 
                that everyone deserves a personalized recommendation system that helps them 
                explore the vast world of anime.
                </p>
                """,
                unsafe_allow_html=True)

    st.write("<h2>Meet the Creator</h2>",unsafe_allow_html=True)

    st.write("""
                <p style ='justify-content: space-between;' >
                <b>Epc-Finds</b>, is the brainchild of <b>Mahakaal</b>, a passionate anime enthusiast 
                and skilled Python developer. With a love for both coding and anime, 
                <b>Mahakaal</b>, combined these interests to create a tool that can help 
                others discover great anime. The project is continuously evolving, with 
                new features and improvements being added based on user feedback
                </p>
                """,
                unsafe_allow_html=True)

    st.write("<h2>Connect with Us</h2>",unsafe_allow_html=True)

    st.write("""
                <p style ='justify-content: space-between;' >
                You can explore the AnimeRecs project on GitHub for more details about 
                its development and contribute to its growth. Check out our 
                <a href="https://example.com" target="_blank">GitHub page</a>
                <br><br>
                Thank you for visiting <b>Epc-Finds</b>! We hope our recommendations 
                bring you countless hours of enjoyment and adventure.
                </p>
                """,
                unsafe_allow_html=True)