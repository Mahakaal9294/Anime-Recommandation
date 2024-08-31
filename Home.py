import streamlit as st


def app():
    st.write("<h1 style ='text-align:center; color:#6A0D91' > EPIC-FINDS </h1>",
                        unsafe_allow_html=True)

    st.write("""
            <h2 style ='text-align:center' >
            Discover Your Next Anime Obsession
            </h2>
            """,
            unsafe_allow_html=True)

    st.image('img/all_anime.jpg',output_format='jpg')

    st.write("""
            <p style ='text-align:center; justify-content: center;' >
            Welcome to Epic-Finds, where finding your next favorite series is a breeze! 
            If you’re tired of endlessly scrolling through lists of titles,
            let our cutting-edge recommendation system guide you to your perfect match. 
            Here, we make it easy for you to uncover anime
            that resonate with your unique tastes.
            </p>
            """,
            unsafe_allow_html=True)

    st.write("""
            <h3>
            How It Works
            </h3>
            """,
            unsafe_allow_html=True)


    st.write("""
            <p style ='justify-content: space-between;' >
            <b>Personalized Recommendations:</b> Start by entering your preferences—favorite 
            genres, themes, and past favorites. Our intelligent algorithm takes these 
            inputs and curates a bespoke list of recommendations tailored just for you.
            Whether you crave adrenaline-pumping action, touching romances, or 
            mind-bending sci-fi, Epic-Finds delivers suggestions that are right up your
            alley.
            </p>
            """,
            unsafe_allow_html=True)

    st.write("""
            <p style ='justify-content: space-between;' >
            <b>Explore Diverse Genres:</b> Our extensive database encompasses every genre 
            imaginable. Dive into thrilling adventures, cozy slice-of-life stories, 
            epic fantasies, or gripping mysteries. No matter what mood you’re in,
            we’ve got something to match.
            </p>
            """,
            unsafe_allow_html=True)

    st.write("""
            <p style ='justify-content: space-between;' >
            <b>User-Friendly Interface:</b> Our platform is designed with you in mind. 
            Easily navigate through your personalized list, read detailed descriptions, 
            view ratings and reviews, and find your next obsession without any hassle.
            </p>
            """,
            unsafe_allow_html=True)


    st.write("""
            <p style ='justify-content: space-between;' >
            <b>Community Connection:</b> Join a vibrant community of fellow enthusiasts. 
            Share your thoughts, rate the series you’ve enjoyed, and connect with 
            others who share your passions. With Epic-Finds, you’re never alone in
            your fandom.
            </p>
            """,
            unsafe_allow_html=True)

    st.write("""
            <p style ='justify-content: space-between;' >
            <b>Stay Informed:</b> Keep up with the latest in the anime and manga world. From 
            news and updates to release schedules and upcoming events, we keep you in
            the loop so you never miss out.
            </p>
            """,
            unsafe_allow_html=True)

    st.write("""
            <p style ='justify-content: space-between;' >
            Ready to discover something new? Dive into Epic-Finds today and let us help 
            you find your next anime obsession. Your perfect 
            series is just a few clicks away!
            </p>
            """,
            unsafe_allow_html=True)
