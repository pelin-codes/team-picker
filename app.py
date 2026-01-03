import streamlit as st
import random

st.title("Who will pay the bill?")

people = []
count = st.number_input("How many people you want to insert?", min_value=1,step=1)
for person in range(count):
    name = st.text_input(f"Insert name #{person+1}",key=person)
    if name:
        people.append(name)

if st.button("Pick who pays"):
    if len(people)==count:
        chosen_person=random.choice(people)
        st.write(f"{chosen_person} will pay the bill!")
    else:
        st.warning("Please fill in all names.")