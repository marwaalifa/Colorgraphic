# import module
import random

import google.generativeai as genai
import numpy as np
import streamlit as st
import webcolors
from PIL import Image
from streamlit_option_menu import option_menu

genai.configure(api_key="AIzaSyAt8JwfnFsMbaoSsdaPoZ1H3qPqpwBg7vc")
model = genai.GenerativeModel("gemini-pro")


def hex_to_rgb(hex_code):
    try:
        rgb = webcolors.hex_to_rgb(hex_code)
        return rgb
    except ValueError:
        return None


def display_color(hex_code):
    rgb_color = hex_to_rgb(hex_code)

    if rgb_color is not None:
        # Create an image with the specified color
        color_image = Image.fromarray(np.full((100, 100, 3), rgb_color, dtype=np.uint8))
        # Display the color box
        st.write(f"Color: {hex_code}")
        st.image(color_image, caption="Color Preview", channels="RGB")
    else:
        st.error("Invalid HEX code. Please enter a valid HEX color code.")


def generate_random_color():
    # Generate a random HEX color code
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return random_color


def mainRColor():
    st.subheader("Random Color Picker")

    # Button to generate a random color
    if st.button("Generate Random Color"):
        random_color = generate_random_color()
        # Display the generated color
        st.write("Generated Color:", random_color)
        # Display a colored box with the generated color
        st.markdown(
            f'<div style="background-color:{random_color}; width:100px; height:100px;"></div>',
            unsafe_allow_html=True,
        )


# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        "Colorgraphics",
        [
            "About",
            "Color Generate by HEX Code",
            "Generate by Text",
            "Random Color Picker",
            "Information",
        ],
        default_index=0,
    )


if selected == "About":
    # Title
    st.title("COLORGRAPHICS")
    # Header
    st.subheader("Colorgraphics: Where Art Meets Intelligence")

    # Subheader
    st.write(
        "Welcome to ChromaCraft, where the world of colors comes alive at your fingertips. Our cutting-edge Color Graphics AI is designed with you in mind—making it easier than ever for users and stakeholders to discover and choose the perfect colors for their creative projects."
        "Unleash the power of ChromaCraft as it intelligently navigates through a spectrum of hues, shades, and tones. Whether you're a designer seeking inspiration or a stakeholder looking to enhance your brand identity, our AI is your trusted guide in the vibrant realm of colors."
        "With ChromaCraft, precision meets creativity. Explore endless possibilities, effortlessly find the colors that resonate with your vision, and watch as your ideas transform into stunning, visually captivating realities."
        "Your journey into the world of colors starts here at ChromaCraft—a seamless experience where choosing the right color is as intuitive as it is exciting."
    )

elif selected == "Color Generate by HEX Code":
    st.subheader("HEX Code Generate")

    # Input field for HEX code
    hex_code = st.text_input("Enter HEX color code:", value="#D2386C")
    if st.button("Enter"):
        result = hex_code.title()
        st.success("Find out!")
        # Display color based on user input
        display_color(hex_code)

elif selected == "Random Color Picker":
    mainRColor()

elif selected == "Generate by Text":
    st.title("Text Generation for Web Developer Color Suggestions")
    input_text = st.text_input(
        "What is your product? we will give you color sugestion based on your product"
    )
    if st.button("Generate Color Sugestion"):
        with st.spinner("Generating..."):
            response = model.generate_content(
                "give me color pallete sugestion for my product, product=  "
                + input_text
            )
            st.write(response.text)

elif selected == "Information":
    # Selection box
    # first argument takes the titleof the selectionbox
    # second argument takes options
    st.subheader("About Color of the Years")
    st.write(
        "The Color of the Year is an annual design trend set by various color authorities, with Pantone being one of the most influential."
        "This chosen color is intended to reflect the current cultural and social climate, influencing trends in fashion, design, and "
        "aesthetics. The selection process involves a thoughtful analysis of global influences, including societal shifts, technological "
        "advancements, and artistic expressions. "
        )
    st.write("As we embrace the Color of the Year, it becomes more than just a shade on the color spectrum;"
        "it encapsulates a narrative, conveying emotions, moods, and aspirations. The chosen color often embodies a collective sentiment, "
        "offering a symbolic representation of our collective hopes and dreams. In the upcoming year, we can anticipate that the Color of the Year"
        "will continue to inspire creativity and innovation across various industries. It may serve as a catalyst for fresh design perspectives,"
        "influencing everything from interior decor to graphic design and fashion. "
        )
    st.write("This color trend is not merely a reflection of aesthetics buta visual language that connects us to the evolving dynamics of our world. "
        "Whether it's a calming hue that promotes tranquility or a bold shade that sparks energy, the Color of the Year is a powerful force" 
        "that transcends its visual appeal. It serves as a cultural marker, "
        "reflecting the spirit of the times and inviting us to explore new realms of expression. Embracing the Color of the Year is an exciting "
        "journey into the intersection of art, design, and cultural evolution, where a single shade can speak volumes about the collective "
        "consciousness of our global community. "
    )
    Cyears = st.selectbox("Color Trends: ", 
                          ["2021", "2020", "2019", "2018", "2017"])
    #Information
    st.write("Colors of ", Cyears)
    if Cyears == "2021":
        st.success("Color of the Years")
        img = Image.open("Cyears2021.png")
        st.image(img, width=200)
        st.write(
            "A 'Raspberry Sorbet' HEX: #D2386C is a vibrant and rich pinkish-red color with a HEX code of #D2386C."
            "This hue resembles the deep and luscious tones of ripe raspberries, conveying a sense of warmth, energy, "
            "and indulgence. The color exudes a playful and feminine vibe, making it a popular choice in various design applications, including fashion, graphic design, and interior decor."
        )
    elif Cyears == "2020":
        st.success("Color of the Years")
        img = Image.open("Cyears2020.png")
        st.image(img, width=200)
        st.write(
            "One of the trendy colors of 2020 was 'Classic Blue' which was announced as the Pantone Color of the Year for 2020."
            "The HEX code for Classic Blue is #0F4C81. "
        )
    elif Cyears == "2019":
        st.success("Color of the Years")
        img = Image.open("Cyears2019.png")
        st.image(img, width=200)
        st.write(
            "The color of the year for 2019, according to Pantone, was 'Living Coral'."
            "The HEX code for Living Coral is #FF6F61. This vibrant and warm color was chosen for its energetic and nurturing qualities."
            "Keep in mind that trends in color can vary across different sources and industries."
        )
    elif Cyears == "2018":
        st.success("Color of the Years")
        img = Image.open("Cyears2018.png")
        st.image(img, width=200)
        st.write(
            "In 2018, Pantone's Color of the Year was 'Ultra Violet', and its HEX code is #5F4B8B."
            "It's important to note that different organizations may have different color trend predictions for a given year."
            "If you are referring to a different trend-setting organization, the color may vary."
        )
    else:
        st.success("Color of the Years")
        img = Image.open("Cyears2017.png")
        st.image(img, width=200)
        st.write(
            "In 2017, Pantone's Color of the Year was 'Greenery' which is a fresh and zesty yellow-green shade."
            "The HEX code for Pantone Greenery is #88B04B. Keep in mind that other sources might have different trendy colors for 2017,"
            "so it's a good idea to check specific trends or color reports from that year for a comprehensive view."
        )

    #st.subheader("Information")
    # Markdown
    #st.markdown("### This is a markdown")
    # success
    #st.success("Success")
    # success
    #st.info("Information")
    # success
    #st.warning("Warning")
    # success
    #st.error("Error")

    st.info(
        "Every year the Pantone Color Institute evaluates the colors shown by fashion designers at the New York Fashion Week."
        "This information is used to create The Pantone Color of the Year and the Pantone Fashion Color Report with the top "
        "fashion colors for the year: ")
