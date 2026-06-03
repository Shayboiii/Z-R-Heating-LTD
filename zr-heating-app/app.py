import streamlit as st

st.set_page_config(page_title="Z&R_HEATING_LTD.co.uk")

# 1. Create Tabs
tab1, tab2, tab3 = st.tabs(["🏡 Home", "📞 Contact Us", "🪪 My Profile"])

# 2. Inside Tab 1
with tab1:
    st.title("Z&R Heating Ltd")
    st.subheader("Expert heating solutions tailored to your needs.")
    st.header("Gas Engineering")
    st.divider()

# Row 1 of Columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 🧰 Boiler Repairs")

    with col2:
        st.markdown("#### 🔥 Heating Installations")

    with col3:
        st.markdown("#### 👍 Friendly & Reliable Service!")

    st.write("---")
    
    #Row 2 of Columns
    col4,col5,col6 = st.columns(3)
    with col4:
        st.markdown("#### 🧰 Boiler Maintenance & Servicing")

    with col5:
        st.markdown("#### 🏷️ Competetive Pricing")

    with col6:
        st.markdown("#### 🔍 Central Heating Fault Finding & Repairs")
    






# 3. Inside Tab 2
with tab2:
    st.header("Get in Touch with us!")
    st.write("Need a Repair or Installation? click the button below to see our emergency line.")

    if st.button("Our Phone number"):
        st.write("### 📞 Call Us: 07908305492")

    if st.button("Our Email"):
        st.write("### 📧 Email Us: heatingmate@outlook.com")

# 4. Inside Tab 3
with tab3:
    st.header("My Profile")
    st.write("Need a Legit Engineer? Come Look at my profile!")
    st.image("zr-heating-app/62820b86-9766-47f8-9bc7-cac1872ae20b.jpeg")


# 5. Style configuration
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F4F4F6;
    }
    h1, h2, h3, h4, p {
        color: #1E1E24 !important;
    }
    hr {
        border-color: #1E1E24 !important;
    }
    header {
        visibility: hidden;
    }
    .stButton > button {
        background-color: #1E1E24 !important;
    }
    .stButton > button * {
        color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

