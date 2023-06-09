import pandas as pd
import streamlit as st
from PIL import Image
from bokeh.models.widgets import Div
import plotly.express as px
import base64


title = 'Asian Football Player Performance on Top Leagues'




# Layout
img = Image.open('assets/icon_pink-01.png')
st.set_page_config(page_title=title, page_icon=img, layout='wide')






st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
#   width: 50%;
}
</style> """, unsafe_allow_html=True)


padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

file_name='style.css'
with open(file_name) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)






# Content
@st.cache
def load_data():
    df_raw = pd.read_csv(r'data/data_for_streamlit.csv', sep=';')
    df = df_raw.copy()
    return df_raw, df

df_raw, df = load_data()
df_merged = df_raw.copy()

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s" class="center" width="100" height="100"/>' % b64
    st.write(html, unsafe_allow_html=True)


# Sidebar color
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #ef4da0;
    }
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    f = open("assets/icon-01.svg","r")
    lines = f.readlines()
    line_string=''.join(lines)

    render_svg(line_string)

    st.write('\n')
    st.write('\n')
    st.write('\n')

    if st.button('🏠 HOME'):
        # js = "window.location.href = 'http://www.muarrikhyazka.com'"  # Current tab
        js = "window.open('http://www.muarrikhyazka.com')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

    if st.button('🍱 GITHUB'):
        # js = "window.location.href = 'https://www.github.com/muarrikhyazka'"  # Current tab
        js = "window.open('https://www.github.com/muarrikhyazka')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)








st.title(title)

st.write(
    """
    \n
    \n
    \n
    """
)

st.subheader('Business Understanding')
st.write(
    """
    As a football fans, this project really enjoys me a lot. 
    """
)

st.write(
    """
    Back to topic, I just want to see the Asian football player performance in top leagues. They are Premiere League, Serie A, La Liga, Ligue 1, and Bundesliga.
    As topping, there is comparison Asian player with other continent player, mainly European player.
    """
)

st.write(
    """
    \n
    \n
    \n
    """
)

st.subheader('Data Understanding')
st.write(
    """
    **Source :**
    \n 1. Take it from Kaggle, here is the [link](https://www.kaggle.com/datasets/vivovinco/20222023-football-player-stats)
    \n 2. Nation Code [link](https://datahub.io/core/country-codes)
    """
)


st.write(
    """
    **Below is sample of the data, after merged.** 
    """
)

st.dataframe(df.sample(5))

st.write(
    """
    **In [Kaggle](https://www.kaggle.com/datasets/vivovinco/20222023-football-player-stats), there is full description of each columns. But, I will provide below only columns which I used.**
    """
)

st.write(
    """
    **Description of each column**
    \nPlayer : Player's name
    \nNation : Player's nation
    \nPos : Position 
    \nAge : Player's age
    \nMin : Minutes played
    \nGoals : Goals scored or allowed
    \nSoT% : Shots on target percentage (Does not include penalty kicks)
    \nPasTotCmp% : Pass completion percentage
    \nAssists : Assists
    \nScaDrib : Successful dribbles that lead to a shot attempt
    \nInt : Interceptions
    \nTklDri% : Percentage of dribblers tackled
    \nBlocks : Number of times blocking the ball by standing in its path
    \nInt : Interceptions
    \nClr : Clearances
    \nAerWon% : Percentage of aerials won
    \nRegion Name : Player's Continent Name
    \nofficial_name_es : Player's nation full name

    """
)

st.write(
    """
    \n
    \n
    \n
    """
)

st.subheader('Method')
st.write(
    """
    Just do simple exploratory data analysis by using some visualizations.
    """
)


st.write(
    """
    \n
    \n
    \n
    """
)

st.subheader('Insights')
st.write(
    """
    My first boundary is only on Asian player. After that, compare to other continent player. Here is my finding :
    """
)

## filter asian player
df_asia = df_merged[df_merged['Region Name']=='Asia'].copy()

## goals on bar chart
fig_1 = px.bar(df_asia.sort_values(by = 'Goals', ascending = False), x="Player", y="Goals", barmode="group", text='Goals')
fig_1.update_traces(textposition="outside")
st.plotly_chart(fig_1, use_container_width=True)

st.write(
    """
    First of all, its a mandatory to see goals number which is reflected the performance of each players. Definitely, it will be dominated by Forward and Midfielder.
    """
)


## playing time on bar chart plotly
tks = df_asia.groupby('Player', as_index=False)['Min'].mean().sort_values(by = 'Min', ascending = False)
fig_2 = px.bar(tks.sort_values(by = 'Min', ascending = False), x="Player", y="Min", barmode="group", text='Min')
fig_2.update_traces(textposition="outside")
st.plotly_chart(fig_2, use_container_width=True)

st.write(
    """
    Mostly have been trusted to play more than 1 match. I think its good opportunity for asian player in Top European League. Some of them is regular player on each teams.
    """
)

## top 10 playing time on plotly viz
fig_3 = px.bar(tks.nlargest(10, 'Min').sort_values(by = 'Min', ascending = False), x="Player", y="Min", barmode="group", text='Min')
fig_3.update_traces(textposition="outside")
st.plotly_chart(fig_3, use_container_width=True)

st.write(
    """
    Just want to highlight, here they are 10 which have the most playing time. Are your idol in there?.
    """
)

## age on plotly viz
fig_4 = px.bar(df_asia.sort_values(by = 'Age', ascending = False), x="Player", y="Age", barmode="group", text='Age')
fig_4.update_traces(textposition="outside")
st.plotly_chart(fig_4, use_container_width=True)

st.write(
    """
    They are on every generation, I think its a good regeneration of asian player in Europe.
    """
)

## player number by nationality
nation = df_asia.groupby('official_name_es', as_index=False)['Player'].count().sort_values(by = 'Player', ascending = False)
fig_5 = px.bar(nation, y='Player', x='official_name_es', title = 'Nationality', text='Player')
fig_5.update_traces(textposition="outside")
st.plotly_chart(fig_5, use_container_width=True)

st.write(
    """
    Top 3 on Turkey, Japan, and South Korea.
    """
)

st.write(
    """
    **After this, I want to compare asian player with other continent player per position.**
    Before that, lets see the distribution of position
    """
)

## position distribution
pos = df_asia.groupby('Pos', as_index=False)['Player'].count().sort_values(by = 'Player', ascending = False)
fig_6 = px.pie(pos, values='Player', names='Pos', title = 'Position')
st.plotly_chart(fig_6, use_container_width=True)

st.write(
    """
    Mostly on Forward and Defender.
    """
)


st.write(
    """
    Here they are the comparison
    \n**FORWARD**
    """
)

df_all_forward = df_merged[df_merged['Pos'].str.contains('FW')].copy()
forward_metrics = ['Goals', 'SoT%', 'Assists', 'AerWon%']
df_group_forward = df_all_forward.groupby('Region Name', as_index=False)[forward_metrics].mean()
for metrics in forward_metrics:
    df_group_forward[metrics] = round(df_group_forward[metrics], 2)
    fig = px.bar(df_group_forward.sort_values(by = metrics, ascending = False), 
                 x="Region Name", 
                 y=metrics, 
                 barmode="group", 
                 title = metrics, 
                 width=800, 
                 height=600,
                 text= metrics)
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

st.write(
    """
    Asian forward player is dominating compared to other continent forward player on all metrics.
    """
)


st.write(
    """
    **MIDFIELDER**
    """
)

df_all_midfielder = df_merged[df_merged['Pos'].str.contains('MF')].copy()
midfielder_metrics = ['PasTotCmp%', 'Assists', 'ScaDrib']
df_group_midfielder = df_all_midfielder.groupby('Region Name', as_index=False)[midfielder_metrics].mean()
for metrics in midfielder_metrics:
    df_group_midfielder[metrics] = round(df_group_midfielder[metrics], 2)
    fig = px.bar(df_group_midfielder.sort_values(by = metrics, ascending = False),
                 x="Region Name", 
                 y=metrics, 
                 barmode="group", 
                 title = metrics, 
                 width=800, 
                 height=600,
                 text= metrics)
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

st.write(
    """
    As of now, there is no good midfielder from Asia, if compare to other.
    """
)

st.write(
    """
    **DEFENDER**
    """
)

df_all_defender = df_merged[df_merged['Pos'].str.contains('DF')].copy()
defender_metrics = ['Blocks', 'TklDri%', 'Int', 'Clr', 'AerWon%']
df_group_defender = df_all_defender.groupby('Region Name', as_index=False)[defender_metrics].mean()
for metrics in defender_metrics:
    df_group_defender[metrics] = round(df_group_defender[metrics], 2)
    fig = px.bar(df_group_defender.sort_values(by = metrics, ascending = False), 
                 x="Region Name", 
                 y=metrics, 
                 barmode="group", 
                 title = metrics, 
                 width=800, 
                 height=600,
                 text= metrics)
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

st.write(
    """
    On Defender metrics, asian players are only good at Interception and Clearance.
    """
)

st.write(
    """
    **GOALKEEPER**
    """
)
st.write(
    """
    **There is no viz per metrics, bcs there is no metrics which is related with goalkeeper.**
    """
)







st.write("""
    Lastly, We can conclude that asian player can compete with other continent player even european player. They are mostly still on green age so can grow up many more. 
    From the data, Turkey, Japan, and South Korea can make a hard game with top European country team in world cup in the meantime.
""")

st.write(
    """
    \n
    \n
    \n
    """
)

c1, c2 = st.columns(2)
with c1:
    st.info('**[Github Repo](https://github.com/muarrikhyazka/asian-football-player-performance-analysis)**', icon="🍣")

