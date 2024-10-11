import streamlit as st
import pandas as pd
import pickle as pkl
import ast 


# loading the similarity vectors
with open('Datasets/anime_similarity.pkl','rb') as f:
    similarity = pkl.load(f)


# loading the dataset
df = pd.read_csv('Datasets/anime_df.csv')

def app():
    ## function to get anime recommandation
    def get_anime(name):
        
        idx = []
        # index of anime 
        anime_idx = df[df['name'] == name].index[0]

        distance = similarity[anime_idx]

        anime_ls = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

        for i,s in anime_ls:
            idx.append(i)

        return anime_idx, idx


    st.write("<h1 style ='text-align:center' >  ANIME RECOMMENDER </h1>",
                    unsafe_allow_html=True)

    anime_names = df['name'].tolist()
    anime_names.insert(0,'Select Anime')

    anime_name = st.selectbox('Select the Anime that you have already watched to view recommandation',
                            options=anime_names)



    if anime_name != 'Select Anime':


        idx,recom_idx = get_anime(anime_name)




        c1,c2 = st.columns([0.3, 0.7])

        c1.image(df['image'][idx])

        def get_eval(ele):

            ele = ast.literal_eval(ele)
            return ', '.join(ele)

        with c2:
            st.subheader(df['name'][idx])

            st.write('<b>Jname:</b>',df['jname'][idx], unsafe_allow_html=True)

            genre= get_eval(df['genre'][idx])
            st.write('<b>Genres:</b>',genre, unsafe_allow_html=True)

            aired= get_eval(df['aired'][idx])
            st.write('<b>Aired:</b>',aired, unsafe_allow_html=True)

            st.write('<b>Studio:</b>',df['studio'][idx], unsafe_allow_html=True)


            st.write('<b>PG Rating:</b>',df['pganime'][idx], unsafe_allow_html=True)

            st.write('<b>Format:</b>',df['formats'][idx], unsafe_allow_html=True)
                            

        st.write(f"<p style ='justify-content: space-between;' > <b>Description:</b> {df['desc'][idx] } </p>",unsafe_allow_html=True)

                
        st.subheader("The Recommendations are:")

        c1,c2,c3,c4,c5 = st.columns(5)

        img1=img2=img3=img4=img5 = ''

        img_ls = []
        title = []

        for i,idx in enumerate(recom_idx):
            img_ls.append(df['image'][idx])
            title.append(df['name'][idx])

        with c1:
            st.image(img_ls[0])
            st.write(f"<h6 style = 'text-align: center;'>{title[0]}</h6>",unsafe_allow_html=True)


        with c2:
            st.image(img_ls[1])
            st.write(f"<h6 style = 'text-align: center;'>{title[1]}</h6>",unsafe_allow_html=True)

        with c3:
            st.image(img_ls[2])
            st.write(f"<h6 style = 'text-align: center;'>{title[2]}</h6>",unsafe_allow_html=True)


        with c4:
            st.image(img_ls[3])
            st.write(f"<h6 style = 'text-align: center;'>{title[3]}</h6>",unsafe_allow_html=True)

        with c5:
            st.image(img_ls[4])
            st.write(f"<h6 style = 'text-align: center;'>{title[4]}</h6>",unsafe_allow_html=True)

            
