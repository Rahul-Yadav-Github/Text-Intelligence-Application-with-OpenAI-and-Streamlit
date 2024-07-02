# streamlit is a framework that gives a technique to do frontend work of an website for machine laearning engineers it uses simple codes in python 
import streamlit as st
# Functions of streamlit
# 1. Uploading Image
st.image("C:\\Users\\rahul\\Desktop\image.png")
#2. giving title
st.title("Welcome to this tutorial, URL to key points")
#3. giving heading
st.header("Paste your url here")
#4. giving subheading
st.subheader("you will get every info youy want to know from your url")
#5.giving any information 
st.info("hi everyone this site gives you an opportunity to find any nformation from the url you pasted here")
#6. checkbox (will se in also widgets sexction)
st.checkbox("login: this is the checkbox for login")
#7. button  ( will also see in widgets section)
st.button("click this button")
#8. this is for giving warning to the user
st.warning("dont clock above button if you have not login yet")
#9. for giving error
st.error("this error shows that you clicked that button and you have not still login")
#10. writing option for user 
st.write("Enter your name if you have login")
# this write function is also used for writing n coding foramte
st.write(range(50))
#11. giving the success message to the user 
st.success("now you are competely registerd with us")
# 12. Markdown - this is used to set a markdown of a section
st.markdown("# URL") # set markdown as big as title
st.markdown('## URL') # set markdown as header
st.markdown("### URL")# set markdown as subheader 
# this function is also used to insert emojies like as
st.markdown(":moon:") # i think this fuction has limited emojies
#13. text- by using this you can show text to the users
st.text("hi, everyone this is a text:")
#14. caption- by using this user can give a caption to their work 
st.caption("you can give your caption here")
# Some extra function which are useful
#15. Mathematical Equations - you can give a mathematical equation to your text
st.latex(r"a+bx^2+c")

#Now this is the time for widgets
#1. checkbox
st.checkbox("login")
#2. button
st.button("click")
#3. Radio widget- this will give user to select one option from multiple options
st.radio("Pick your Url type",["Polytics","Science","Mythology", "others"])
#4. Select box- this will help users to select an option just like above but it will e in a box formate
st.selectbox("choose , how many urls you are submitting?",["1","2",'3','4','others'])
#5. multiselect- this will help users  to select multiple options and also allow them to deselect them by simply clicking on cutbar
st.multiselect("Select at which time of the day you are using our services:",['morning','afternoon','evening','night'])
#6. select_slider- this fuction allows user to give an outcome by just sliding the slider , like giving the ratings
st.select_slider("Ratings",["Bad",'good','exelent','outstanding'])
#7. slider - this function allows user to give a number as an outpt by just sliding the slider
st.slider("Enter your lucky number",0,100)
#8. number_input - this function is used to display numeric input digits
st.number_input("pick a number",0,1000)
#9. text_input- used to take text as an iput like , emails
st.text_input("Enter your email address")
#10. date_input- used to take date as an input
st.date_input("Opening ceremony")
#11. time_input - used to take time as an input
st.time_input("hi, what's the time ")
#12. text_area - this function is used to give texts more than one liner
st.text_area("Paste your text here")
#13. file_uploader- used to upload your file from your pc
st.file_uploader("upload your file here")# you can upload upto 200MB file 
#14. color_picker- used to pick any color
st.color_picker("color")
#15. progress- showing the progress
st.progress(90)
# 16. spinner - it will show a temperory waiting message 
#st.spinner(5)  # only this will not work we have to import time and use spinner as a function 
import time as t
with st.spinner("Just wait"):
    t.sleep(5)
#17. balloons - it is a function to show balloons for celebiration
st.balloons() # you can see balloons after execution of above commands



# Now comes the SIDEBAR
#1. title-  used to give title for sidebar
st.sidebar.title("Paste your urls here")
#2. text_input - used to take text as input 
st.sidebar.text_input("Paste your first url link here")
st.sidebar.text_input("Paste your Second url link here")
st.sidebar.text_input("Paste your third url link here")
#3. button 
st.sidebar.button("submit")
#4. radio- options
st.sidebar.radio("Your profession",["student","teacher","others"])



# Now some commands for data visualisation 
#for this we will import pandas lirary as well as numpy library
import pandas as pd
import numpy as np
data=pd.DataFrame(np.random.randn(50,2),columns=['x',"y"])
#1. bar_chart- sghowing data as barchart
st.title("bar_chart")
st.bar_chart(data)
#2. line_chart- used to create line chart
st.title("line-chart")
st.line_chart(data)
#3. area_chart- used to create arae chart of the data
st.title("area chart")
st.area_chart(data)