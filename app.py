
from regex import F
import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import streamlit.components.v1 as components



st.set_page_config(page_title="Zomato Recommendation System", page_icon=":pizza:")

img = Image.open("Zomato_logo.png")

col1,col2,col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.image(img, width=100)

with col3:
    st.write(' ')


st.title("ZOMATO RECOMMENDATION SYSTEM")



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
                "cuisines": zomato["cuisines"].iloc[i[0]],
            }
        )

    return reccommended_restaurants


# as we cannot push dataframe to streamlit
# store data values in key:value pairs
# convert it to dictionary to transport
zomato_dict = pickle.load(open("zomato_dict2.pkl", "rb"))
zomato = pd.DataFrame(zomato_dict)

cosine_similarities = pickle.load(open("similarity2.pkl", "rb"))

st.markdown("<h1 style='text-align: center; font-size:20px ; color: #DAA520;'><i><b> 'your one stop destination to satisfy the hunger' </i></b></h1>", unsafe_allow_html=True)

st.markdown('#')

st.markdown(
    " **_Feeling_ _Hungry_?!!** Not sure where to order from? Do not worry, we have got your back!😉 " 
)
st.markdown('##')
st.write(""" Many factors influence an individual’s health, such as physical exercise, sleep, nutrition, heredity and pollution. Being nutrition one of the biggest modifiable factors in our lives, small changes can have a big impact.  As Bangalore is the home for foodies, going out for no specific reason, sniffing the fresh aroma of coffee brewing in the various Darshinis and ultimately hopping into one to maybe have a crispy vada or a rava idli to go with it. With already a beaming number of 15,000 restaurants, the industry hasn't soaked yet. We see more cafes, pubs and dine-in restaurants being built every day; which gives birth to the question that how are the concerns of high real estate costs, rising food costs, shortage of quality manpower, fragmented supply chain being catered to. Detailed reports are an integral part of a personalization system. Accurate and up-to-the-minute reporting will allow you to make informed decisions about the direction of a campaign or the structure of a product page.
""")
st.markdown('#')
st.write("""Restaurant Recommendation System (RRS) is an on-line system to search restaurants. The system allows visitors to browse information about the restaurants, including searching restaurants., viewing/giving recommendations, and viewing/rating restaurants. Visitors can only view recommendations and view rating results. In this web app, you will also find details such as phone numbers, trending places and new openings in the neighbourhood at the sidebar. So, what are we waiting for?!

""")
options = st.multiselect(
     'Which cuisine would you prefer today?',
     ['North Indian', 'Mughlai', 'Chineese', 'Thai', 'Mexican','Italian', 'South Indian', 'Rajasthani', 'Continental', 'Fast Food', 'Cafe', 'Bakery', 'Ice Cream', 'Beverages', 'Snacks', 'Desserts', 'Biryani', 'Pizza', 'Juice', 'Burger', 'Sandwich', 'Paneer''Dal'],
     )

selected_zomato_name = st.selectbox(
    "Choose your all-time favourite Restaurant in the city!", zomato["name"].values
)

# Using "with" notation
with st.sidebar:
   with st.expander("Explore the ZomaVerse!🌆"):
     st.write(""" Zomato (/zoʊmɑːtoʊ/) is an Indian multinational restaurant aggregator and food delivery company founded by **Deepinder Goyal** and **Pankaj Chaddah** in 2008.Zomato provides information, menus and user-reviews of restaurants as well as food delivery options from partner restaurants in select cities.As of 2019, the service is available in 24 countries and in more than 10,000 cities!!
""")
with st.sidebar:
    with st.expander("10 Min Delivery Policy"):
        st.write("""Zomato attracted a lot of attention with controversy after their CEO announcing 10 min food delivery. Questions have been raised from consumers as well as Delivery partners as to how will this be feasible without compromising on safety of the delivery teams and will this not deter the quality of food being delivered.
     """)
    
with st.sidebar:
    with st.expander("Newly Opened in Bangalore"):
     st.write(""" Sashay-Taproom Kitchen,
                  MisoSexy,
                  Secret Souls,
                  Jamie's Pizza,
                  The History Pub,
                  Catch Up,
                  Sage‼️
     
""")
    
with st.sidebar:
    with st.expander("Trending this week"):
     st.write(""" The Local, One for the Road, Fire Station, Backstation Brewery,Bob's Cafe, Mitti Bar‼️
""") 
    
with st.sidebar:
    with st.expander("About the Developer"):
     st.write(""" Hi, there! I am Twisha, a sophomore pursuing Electronics & Communications Engineering from MIT,Manipal. I'm a full-stack developer and a problem-solving enthusiast. Tech is absolutely fascinating to me, feminism is my bread and butter, agnst against the male dominated spirit of this industry is what keeps me going!
""")
     st.image("https://media-exp1.licdn.com/dms/image/C4D03AQElya6matSsRA/profile-displayphoto-shrink_800_800/0/1652004179099?e=1658966400&v=beta&t=b0CWjZ-IVx0YBTLr0X915gqMWRRTAFHlkO9fm9otrgk", width=150)
    components.html(
     f"""
       <a href="https://www.linkedin.com/in/twisha-awasthy-24832720a/" target="_blank"/>LinkedIn👨🏻‍💻</a><br>
       <a href="https://github.com/Twisha30" target="_blank"/>Github👨🏻‍💻</a><br>
       <a href="https://www.zomato.com/bangalore/top-restaurants" target="_blank"/>Trending📈</a><br>
       <a href="https://www.zomato.com/bangalore/newly-opened" target="_blank"/>Newbees🏨</a><br>
       <a href="https://www.zomato.com" target="_blank"/>Zomato🍜</a><br>

     """ )

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
                  <div class="card text-dark" style="height:'320px'">  
                    <div class="card-body">
                        <h5 class="card-title text-center">🏨 {i["name"]}</h5>
                        <div class="d-flex align-items-center justify-content-center">
                          <p class="card-text m-0">⭐ {i["rate"]} </p>
                          <p class="card-text mx-4">📞 {i["phone"]}</p>
                        </div>
                        <p class="card-text text-center my-4"><span class='font-weight-bold font-italic'>De La Cuisine: </span> {i["cuisines"]}</p>
                    </div>
                </div>
        </div>"""
        )



img1 = Image.open("rest1.jpg")
img2= Image.open("rest2.jpg")
img3= Image.open("rest3.jpg")


col1,col2,col3 = st.columns(3)
with col1:
    st.image(img1, width=100 )

with col2:
    st.image(img2, width=100)

with col3:
    st.image(img3, width=100)
    

   



     
