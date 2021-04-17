#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import streamlit as st

st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="centered",
     initial_sidebar_state="expanded",
 )

# In[ ]:

"""

# API Reference:

Some markdown

"""




import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time


st.subheader("Packages used: ")

code = """

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time



"""

st.code(code, language = "python")

" "

df = pd.DataFrame({'col1': [1,2,3]})
df  # <-- Draw the dataframe

x = 10
'x = ', x  # <-- Draw the string 'x' and then the value of x

"""
## Now we are gonna see some examples of text writing: 

    1. Title
    2. Header
    3. Sub Header
    4. Text
    5. Markdown 

"""

"This is st.text(): " 
st.text("Hello!")

"This is Markdown: "
st.markdown("Hello!  :+1:")
st.markdown("Hello!  :sunglasses:")
st.markdown('Streamlit is **_really_ cool**.')

"Using st.write() for displaying a df: "

st.write(pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40],
}))

"Now displaying a df as it is: "

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
})

df
"Hmm.. No difference"

"""
st.write() can have multiple arguments as well such as:

st.write('1 + 1 = ', 2)
and, 
  st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')

"""

"Cool :sunglasses:"

"Using st.title(): "

st.title('This is a title')

"## Alright we are now using st.code():"

code = """

code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')

 """

st.code(code, language = "python")

"## Okay, now we display data using st.dataframe() with code"

st.markdown("Code: ")

code = """

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)


"""

st.code(code, language = "python")

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

" "

"## Okay let's diplay an image now.."

code = """

image = Image.open("tesla.jpeg")
captionn = "Cool Tesla :sunglasses:"

st.image(image, caption = "Cool Tesla")

"""

st.code(code, language = "python")

image = Image.open("tesla.jpeg")

st.image(image, caption = "Cool Tesla")

"#### Image taken from: https://www.tesla.com/models"

"   "

"## Now we move onto adding interactive widgets: "
"### Button: "

code = """

if st.button("Use this button to see a F1 car"):

    image = Image.open("mercedes.jpg")
    st.image(image, caption = st.write("Cool F1 car :sunglasses: : https://www.formula1.com/en/latest/article.first-look-mercedes-retain-black-livery-as-they-unveil-hamilton-and-bottas.4WeK7XYYLYYxGGWViHMpOb.html"))
else:
    st.write("Okay do not look at a cool F1 car :sunglasses:")

"""

st.code(code, language = "python")

if st.button("Use this button to see a F1 car"):

    image = Image.open("mercedes.jpg")
    st.image(image, caption = st.write("Cool F1 car :sunglasses: : https://www.formula1.com/en/latest/article.first-look-mercedes-retain-black-livery-as-they-unveil-hamilton-and-bottas.4WeK7XYYLYYxGGWViHMpOb.html"))
else:
    st.write("Okay do not look at a cool F1 car :sunglasses:")


code = """


agree = st.checkbox('I agree')

# Returns bool value

if agree:   # Sort of like if True
    st.write('Great!')


"""

st.code(code, language = "python")

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')

"### Radio Button Widget: "

code = """

# Returns the value selected 

genre = st.radio(
   "What's your favorite movie genre?",
     ('Comedy', 'Drama', 'Documentary'))


"You selected " + genre

#Breaking down the code above

#if genre == 'Comedy':
#     st.write("You selected " + genre)
#elif genre == "Drama":
#     st.write("You selected " + genre)
#elif genre == "Documentary":
#    st.write("You selected " + genre)


"""

st.code(code)

genre = st.radio(
   "What's your favorite movie genre?",
     ('Comedy', 'Drama', 'Documentary'))


"You selected " + genre

"Another one: "

code = """

# Returns the value selected 


logo_choice = st.radio("Which logo do you want to see?" , ("Apple Inc.", "Tesla", "Formula 1", "Real Madrid"))


if logo_choice == "Apple Inc.":

    image = Image.open("apple_logo.jpeg")
    st.image(image, caption = "Apple Logo (https://www.apple.com and https://www.logolynx.com/topic/apple)")

elif logo_choice == "Tesla":

    image = Image.open("tesla_logo.jpeg")
    st.image(image, caption = "Tesla Logo (https://www.pinterest.com/pin/116671446576027863/)")

elif logo_choice == "Formula 1":

    image = Image.open("f1_logo.jpeg")
    st.image(image, caption = "Formula 1 Logo (https://en.logodownload.org/formula-1-logo-f1-logo/)")

elif logo_choice == "Real Madrid":

    image = Image.open("real_madrid_logo.jpeg")
    st.image(image, caption = "Real Madrid Logo (https://www.pinterest.com/pin/585608757771201882/)")


"""

st.code(code, language = "python")

logo_choice = st.radio("Which logo do you want to see?" , ("Apple Inc.", "Tesla", "Formula 1", "Real Madrid"))


if logo_choice == "Apple Inc.":

    image = Image.open("apple_logo.jpeg")
    st.image(image, caption = "Apple Logo (https://www.apple.com and https://www.logolynx.com/topic/apple)")

elif logo_choice == "Tesla":

    image = Image.open("tesla_logo.jpeg")
    st.image(image, caption = "Tesla Logo (https://www.pinterest.com/pin/116671446576027863/)")

elif logo_choice == "Formula 1":

    image = Image.open("f1_logo.jpeg")
    st.image(image, caption = "Formula 1 Logo (https://en.logodownload.org/formula-1-logo-f1-logo/)")

elif logo_choice == "Real Madrid":

    image = Image.open("real_madrid_logo.jpeg")
    st.image(image, caption = "Real Madrid Logo (https://www.pinterest.com/pin/585608757771201882/)")

"### Moving on now.."
" "
"### Using selectbox widgets instead of radio buttons.. "

code = """

# Returns the value selected 


logo_choice = st.selectbox("Which logo do you want to see?" , ("Apple Inc.", "Tesla", "Formula 1", "Real Madrid"))

if logo_choice == "Apple Inc.":

    image = Image.open("apple_logo.jpeg")
    st.image(image, caption = "Apple Logo (https://www.apple.com and https://www.logolynx.com/topic/apple)")

elif logo_choice == "Tesla":

    image = Image.open("tesla_logo.jpeg")
    st.image(image, caption = "Tesla Logo (https://www.pinterest.com/pin/116671446576027863/)")

elif logo_choice == "Formula 1":

    image = Image.open("f1_logo.jpeg")
    st.image(image, caption = "Formula 1 Logo (https://en.logodownload.org/formula-1-logo-f1-logo/)")

elif logo_choice == "Real Madrid":

    image = Image.open("real_madrid_logo.jpeg")
    st.image(image, caption = "Real Madrid Logo (https://www.pinterest.com/pin/585608757771201882/)")



"""

st.code(code, language = "python")


logo_choice = st.selectbox("Which logo do you want to see?" , ("Apple Inc.", "Tesla", "Formula 1", "Real Madrid"))

if logo_choice == "Apple Inc.":

    image = Image.open("apple_logo.jpeg")
    st.image(image, caption = "Apple Logo (https://www.apple.com and https://www.logolynx.com/topic/apple)")

elif logo_choice == "Tesla":

    image = Image.open("tesla_logo.jpeg")
    st.image(image, caption = "Tesla Logo (https://www.pinterest.com/pin/116671446576027863/)")

elif logo_choice == "Formula 1":

    image = Image.open("f1_logo.jpeg")
    st.image(image, caption = "Formula 1 Logo (https://en.logodownload.org/formula-1-logo-f1-logo/)")

elif logo_choice == "Real Madrid":

    image = Image.open("real_madrid_logo.jpeg")
    st.image(image, caption = "Real Madrid Logo (https://www.pinterest.com/pin/585608757771201882/)")


"### Moving onto multiple selections example now.."

code = """

# Returns a string list with selected options

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

"### 1st display option: "

a = ", ".join(options)
a

"### Or.. a list output: "
" "
st.write('You selected:', options)

"""

st.code(code, language = "python")

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

"### 1st display option: "

a = ", ".join(options)
a

"### Or.. a list output: "
" "
st.write('You selected:', options)

" "

"### Now we will use the slider button example.. "

code = """

# The current value of the slider widget. The return type will match the data type of the value parameter.

age = st.slider('How old are you?', 0, 130, 25)

st.write("I'm ", age, 'years old')


"""

st.code(code, language = "python")

age = st.slider('How old are you?', 0, 130, 25)

st.write("I'm ", age, 'years old')

"### Using a slider with range.."


code = """

values = st.slider(
'Select a range of values',
0.0, 100.0, (25.0, 75.0))

"#### Output will be: "

st.write('Values:', values)

"Minimum value chosen: " + str(values[0])
"Maximum value chosen: " + str(values[1])

# Notice the use of decimal in the code

"""

st.code(code, language = "python")

values = st.slider(
'Select a range of values',
0.0, 100.0, (25.0, 75.0))

"#### Output will be: "

st.write('Values:', values)

"Minimum value chosen: " + str(values[0])
"Maximum value chosen: " + str(values[1])

"### Time slider: "

code = """

from datetime import time
appointment = st.slider(
"Schedule your appointment:",
value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

"""

st.code(code, language = "python")

# For time 
from datetime import time
appointment = st.slider(
"Schedule your appointment:",
value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)


"### Moving onto text input widget: "

code = """

# Returns text string

title = st.text_input('What is your name? ')

st.write('Your name is ', title)

# For writing password

passwrd = st.text_input("Please enter your password", type = "password")

passwrd_agree = st.checkbox("Check this box to see your password")

if passwrd_agree:
    
    "Your password is: " + passwrd


"""

st.code(code, language = "python")

title = st.text_input('What is your name? ')

st.write('Your name is ', title)

# For writing password

passwrd = st.text_input("Please enter your password", type = "password")

passwrd_agree = st.checkbox("Check this box to see your password")

if passwrd_agree:
    
    "Your password is: " + passwrd

"## Testing out file upload options"

code = """

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    a = df.head()
    st.write(a)

"""

st.code(code, language = "python")

"#### Upload a csv file and the program will diplay the top 5 rows of the data"

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    a = df.head()
    st.write(a)

"### Pick a color widget"

code = """

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

"""

st.code(code, language = "python")

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

" "

"### Now we are going to test out adding widgets to sidebar functionality"

code = """

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

"""

st.code(code, language = "python")


"## Beta columns"
"### Insert containers laid out as side-by-side columns."

code = """

col1, col2, col3 = st.beta_columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

"""

st.code(code, language = "python")

col1, col2, col3 = st.beta_columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")


"## Beta Expander"

"### Insert a multi-element container that can be expanded/collapsed. Can be used to provide explanation to the code"

code = """

st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.beta_expander("See explanation"):
     st.write("
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random. Note: Code taken from streamlit docs - https://docs.streamlit.io/en/stable/api.html#streamlit.beta_expander")
     st.image("https://static.streamlit.io/examples/dice.jpg")


"""

st.code(code, language = "python")

st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.beta_expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random. Note: Code taken from streamlit docs - https://docs.streamlit.io/en/stable/api.html#streamlit.beta_expander
     """)
     st.image("https://static.streamlit.io/examples/dice.jpg")


"## Displaying Progress Bar"

code = """

import time

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.01)
     my_bar.progress(percent_complete + 1)

st.info('This is a purely informational message')
"""

st.code(code, language="python")

import time

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.01)
     my_bar.progress(percent_complete + 1)


st.info('This is a purely informational message')
st.success('This is a success message!')


code = """

prog = 0
my_bar = st.progress(prog)

prog = prog + 50
my_bar.progress(prog)
time.sleep(5)
prog = prog + 50
my_bar.progress(prog)

st.success('Success!')


"""

st.code(code, language="python")

"# End of API Reference Doc!"
st.balloons()