from regex import F
import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import streamlit.components.v1 as components


st.set_page_config(page_title="Zomato Recommendation Engine", page_icon=":shark:")

img = Image.open("Zomato_logo.png")
st.image(img, width=50)

st.title("Zomato Recommendation System")


# defining a function using a for loop that will return five recommended restaurants
def reccommend(Restaurant):
    index = zomato[zomato["name"] == Restaurant].index[0]
    distances = cosine_similarities[index]
    zomato_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6
    ]
    print(zomato)
    reccommended_restaurants = []
    for i in zomato_list:

        reccommended_restaurants.append(
            {
                "name": zomato["name"].iloc[i[0]],
                "rate": zomato["rate"].iloc[i[0]],
                "phone": zomato["phone"].iloc[i[0]],
            }
        )

    return reccommended_restaurants


# as dataframe in pandas can not be pushed to streamlit directly, we convert it to dictionary and then transport it
zomato_dict = pickle.load(open("zomato_dict2.pkl", "rb"))
zomato = pd.DataFrame(zomato_dict)

cosine_similarities = pickle.load(open("similarity2.pkl", "rb"))


st.markdown(
    " **_Feeling_ _Hungry_?** Not Sure what to eat? Do not worry, we have got your back!"
)

selected_zomato_name = st.selectbox(
    "Choose your all-time favourite Restaurant!", zomato["name"].values
)
st.slider("On a scale of 1-10, how hungry are you right now?", 0, 10)


# bootstrap 4 collapse example


if st.button("Recommend"):
    reccommend(selected_zomato_name)
    Reccommendations = reccommend(selected_zomato_name)
    for i in Reccommendations:

        components.html(
            f"""
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            <div class="card-deck">
            <div class="card text-dark">  
            <div class="card-body">
                <h5 class="card-title">{i["name"]}</h5>
                <h5 class="card-title">{i["rate"]}</h5>
                <h5 class="card-title">{i["phone"]}</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
            </div>
            </div>
        </div>"""
        )
