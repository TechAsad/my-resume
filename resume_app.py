import streamlit as st

# Sidebar navigation
#st.sidebar.title("Navigation")
st.set_page_config(page_title='Muhammad Asadullah Resume', page_icon="adult")
pages = ["Home", "Resume", "Projects"]
page = st.radio("Go to", pages, horizontal=True)

# Home Page
if page == "Home":
    st.title("Engr. Muhammad Asadullah")
    st.subheader("Electrical Engineer | Data Scientist | AI Developer")
    st.write("Welcome to my portfolio! I'm a dynamic and innovative professional with a strong technical background, "
             "passion for advancing technology through AI, and a track record of success in electrical engineering and "
             "data science. I am excited to share my experience and projects with you.")
    st.write("Email: asadiqbal1247@gmail.com")
    st.write("Phone: +92-320-4109120")
    st.write("LinkedIn: [Engr. Muhammad Asadullah](https://www.linkedin.com/in/asad18/)") # Placeholder for LinkedIn link

    
    st.subheader("SKILLS & EXPERTISE")
    
    st.write("✓ Expertise in Python for Data Analysis, Machine Learning, and Web Application Development. Proficient in LangChain, Streamlit, CrewAI, Autogen, YOLO, TensorFlow, PyTorch, and Pandas.\n\n"
    "✓ Comprehensive knowledge of Data Analytics, Visualization, and Predictive Modeling using R-studio and RapidMiner.\n\n"
    "✓ Proficient in using SQL for Database Management and Data Analysis, including data extraction, manipulation, and querying.\n\n"
    "✓ Skilled in developing AI chatbots and applications using advanced Natural Language Processing techniques and large language models like OpenAI's GPTs, Llama 2/3, and Google PaLM2.\n\n"
    "✓ Experienced in designing and implementing solar power systems using Sketchup Pro and PVsyst.\n\n"
    "✓ Proficient in Tableau and Power BI for Data Visualization and Dashboard Creation.\n\n"
    "✓ Basic knowledge of web development using HTML, CSS, and JavaScript.\n\n"
    "✓ Experience with Power Distribution Transformers' assembly and testing.\n\n"
    "✓ Developed websites using WordPress to showcase projects and skills.\n\n"
    "✓ Leadership and ability to manage medium to large size teams.\n\n"
    "✓ Quick learner with excellent communication, negotiation, and presentation skills.\n\n")

# Resume Page
elif page == "Resume":
    st.title("Resume")
    st.subheader("Executive Summary")
    st.write("""
    Dynamic and innovative professional with a strong technical background, passion for advancing technology through AI,
    and a track record of success in electrical engineering and data science. Poised to leverage AI development skills
    in a high-growth environment.
    """)
    st.subheader("Key Competencies")
    st.write("""
    - AI and Machine Learning: Extensive experience in developing AI chatbots, implementing machine learning algorithms,
    and utilizing advanced techniques in Natural Language Processing (NLP) and large language models such as OpenAI's GPTs, Llama 2/3, and Google PaLM2.
    - Electrical Engineering: Proficient in power system protection, high voltage DC transmission lines, and solar system design.
    - Data Science and Analytics: Adept at statistical data analysis, predictive modeling, and developing innovative data-driven solutions.
    - Quick Learner and Team Player: Capable of working under pressure, quickly learning new technologies, and effectively handling multiple tasks while maintaining attention to detail.
    """)

    st.subheader("Work Experience")
    st.write("""
    **Data Scientist & AI Developer | Remote (2019 – Present)**
    - Led the development of AI chatbots and machine learning algorithms for various innovative applications.
    - Utilized advanced techniques in NLP and large language models such as OpenAI's GPTs, Llama 2/3, and Google PaLM2.
    - Applied Python and R for data analysis, machine learning, and web application development.
    
    **Deputy Management Representative & Lab Engineer | GRIT Pvt Ltd (2021 – 2022)**
    - Managed lab records for yearly evaluations and worked with a team to achieve production milestones.
    - Gained expertise in transformer assembly and testing, enhancing quality control processes.
    
    **Solar System Designer | SME Pvt Ltd (2022 – 2024)**
    - Developed design specifications and functional requirements for solar energy systems.
    - Designed a 1MW Solar System for Industrial State, improving energy efficiency by 30%.
    """)

    st.subheader("Academic Qualifications")
    st.write("""
    - Bachelor of Electrical Engineering (3.01 CGPA), Lahore Leads University, Lahore, Pakistan (2017 – 2021)
    - A-Level, Mansoorah Model Degree College, Lahore, Pakistan (2015 – 2017)
    """)

# Projects Page
elif page == "Projects":
    st.title("Projects")
    
    st.subheader("[AI Legal Advisor](%s)" % 'https://smartedgelawai.onrender.com/')
    #st.write("check out this [link](%s)" % url)
    st.write("""
    **Technologies Used:** LangChain ChatGPT-4, TypeScript, Pinecone Vector DB
    - Developed an AI legal advisor application utilizing LangChain framework to provide legal advice and guidance through legal documents.
    - Integrated ChatGPT-4 for helpful answer generation using extracts from pre-loaded legal documents.
    """)
    
    st.subheader("[Market Researcher AI Tool](%s)" % 'https://ai-market-researcher.streamlit.app/')
    st.write("""
    **Technologies Used:** Python, Reddit Scrapper, LangChain, LangGraph, GPT-4
    - Market Researcher about the given product details.
    - Creates marketing campaign, target audience personas, and landing page contents with help of market research.
    """)

    st.subheader("Personalized Cold Email Writer")
    st.write("""
    **Technologies Used:** Python, Web Scrapper, LangChain, LangGraph, GPT-4 / LlaMa 3
    - AI driven cold email writer which writes emails for provided leads by researching their websites and personal social media accounts.
    """)

    st.subheader("[Multi-Agent AI Chatbot for Document Search](%s)" % 'https://pdfchatbot-palm.streamlit.app/')
    st.write("""
    **Technologies Used:** Python, LangChain, CrewAI, OpenAI LLMs
    - Designed and developed a multi-agent AI chatbot with capabilities for document search, Google search, and Wikipedia search.
    """)

    st.subheader("Baseball Pitcher's Strikeout Prediction")
    st.write("""
    **Technologies Used:** Python, PyTorch, R
    - Predictive modeling with neural network to predict the probability of a pitcher earning more than a certain number of strikeouts.
    """)

    st.subheader("Colour Sorting Device")
    st.write("""
    **Technologies Used:** Arduino, Servo Motors, Colour Sensors
    - Designed and manufactured a colour sorting device using Arduino UNO.
    """)


