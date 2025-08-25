import streamlit as st
from PIL import Image

# --- CONFIG ---
st.set_page_config(page_title="William C. Weinberger - Portfolio", page_icon="💻", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    body {
        font-family: 'Segoe UI', sans-serif;
    }
    /* Hero Section */
    .hero-title {
        font-size: 3rem;
        font-weight: bold;
        color: #ECF0F1;
        margin-bottom: 10px;
    }
    .hero-subtitle {
        font-size: 1.5rem;
        color: #95A5A6;
        margin-bottom: 20px;
    }
    /* Section Titles */
    .section-title {
        font-size: 2rem;
        margin-top: 40px;
        margin-bottom: 20px;
        color: #1ABC9C;
    }
    /* Cards */
    .card {
        padding: 20px;
        border-radius: 12px;
        background-color: #2C3E50;
        margin-bottom: 20px;
        color: #ECF0F1;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5),
                    0 0 12px rgba(26, 188, 156, 0.3); /* subtle teal glow */
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.6),
                    0 0 20px rgba(26, 188, 156, 0.6); /* brighter glow on hover */
    }
    /* Skills */
    .skill-badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        margin: 5px;
        font-size: 0.9rem;
        color: white;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .skill-badge:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 12px rgba(255,255,255,0.4);
    }
    .python { background:#3776AB; }
    .aws { background:#FF9900; }
    .angular { background:#DD0031; }
    .typescript { background:#3178C6; }
    .devops { background:#2ECC71; }
    .db { background:#8E44AD; }
    .leadership { background:#F1C40F; color:black; }
    /* Centering / Max Width */
    .block-container {
        max-width: 1000px;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
        margin: auto;
    }
    /* Background Gradient */
    body {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        background-attachment: fixed;
    }
    .stApp {
        background: transparent;
    }
    /* Hide Sidebar */
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stSidebarNav"] {display: none;}
    [data-testid="stSidebarNavItems"] {display: none;}
    [data-testid="stSidebarCollapsedControl"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 3])
with col1:
    st.image("headshot.png", width=200)
with col2:
    st.markdown("<div class='hero-title'>William C. Weinberger</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-subtitle'>Engineering Leader | Cloud & Data Expert | Technical Program Manager</div>", unsafe_allow_html=True)
    st.write("Greater Pittsburgh Region | 📧 wcweinberger@gmail.com | 📱 724-366-3205")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/wcweinberger/)")
    with open("resume.pdf", "rb") as f:
        st.download_button("📄 Download Resume", f, "William_Weinberger_Resume.pdf")

st.write("---")

# --- SUMMARY ---
st.markdown("<div class='section-title'>🔎 Summary</div>", unsafe_allow_html=True)
st.write("""
Engineering leader with a proven record of building high-performing teams and delivering scalable software solutions across healthcare, SaaS, and enterprise platforms.  
Experienced in **cloud-native architectures, large-scale data systems, and DevOps automation**, with hands-on expertise in Python, TypeScript, and AWS serverless.  
Skilled at bridging technical strategy with business objectives, driving initiatives from concept to MVP, and fostering collaborative, resilient engineering cultures.  
""")

# --- CAREER HIGHLIGHTS ---
st.markdown("<div class='section-title'>🌟 Career Highlights</div>", unsafe_allow_html=True)

highlights = [
    {
        "title": "Compass Group USA",
        "text": "Architected and led development of a serverless Master Data Management (MDM) platform mastering 2.5M+ client records. Successfully guided the Client domain to MVP release."
    },
    {
        "title": "MURAL",
        "text": "Managed two teams: a Full-stack Integrations team (6 engineers, TypeScript/React/C#/Playwright) and a QA Automation team (4 engineers). Delivered an innovative Microsoft Teams integration that contributed to MURAL being recognized as a Microsoft Partner of the Year."
    },
    {
        "title": "SoftWriters",
        "text": "Built an Automation Engineering team from the ground up (2 → 5 engineers). Designed Python-based test frameworks, enhanced reliability of C# pharmacy applications, and launched a performance testing program that uncovered bottlenecks and database locking issues, significantly improving responsiveness for enterprise customers."
    },
    {
        "title": "Arcadia",
        "text": "Designed and implemented a company-wide end-to-end testing suite. Contributed to an Auth0 SSO migration, replacing Cognito across the enterprise."
    },
    {
        "title": "MedCPU",
        "text": "Engineered a Python/Kafka HL7 test harness that simulated clinical data feeds, enabling standardized testing of Clinical Decision Support pathways. This innovation became the company-wide approach for validating the Clinical Rules Engine."
    },
    {
        "title": "UPMC Enterprises",
        "text": "Contributed to multiple healthcare startup initiatives. Selected by leadership to join the core team scaling MedCPU after its acquisition, demonstrating adaptability and trusted execution in high-visibility projects."
    },
    {
        "title": "Compunetix",
        "text": "Founded and built a web testing team from the ground up. Implemented automation frameworks for teleconferencing solutions, establishing long-term quality practices across the product suite."
    },
]

for h in highlights:
    st.markdown(f"""
    <div class='card'>
    <b>{h["title"]}</b><br/>
    {h["text"]}
    </div>
    """, unsafe_allow_html=True)

# --- PROFESSIONAL EXPERIENCE ---
st.markdown("<div class='section-title'>💼 Professional Experience</div>", unsafe_allow_html=True)
st.write("Expanded role details, responsibilities, and scope:")

with st.expander("Compass Group USA – Senior Technical Lead/Manager (2024–Present)"):
    st.write("""
    - Led architecture and delivery of a serverless MDM platform (AWS Lambda, API Gateway, Aurora, Snowflake).  
    - Hands-on contributions across Python backend and Angular/TypeScript frontend.  
    - Built CI/CD pipelines in Azure DevOps; implemented IaC using AWS CDK (TypeScript).  
    - Managed a cross-functional team of engineers across dev, QA, and DevOps.  
    """)

with st.expander("MURAL – Engineering Manager (2022–2023)"):
    st.write("""
    - Managed two teams:  
        • Full-stack Integrations (6 engineers, TypeScript/React/C#/Playwright)  
        • QA Automation (4 engineers)  
    - Collaborated with Product and Design for roadmap alignment.  
    - Implemented structured production support rotations and customer feedback loops.  
    - Supported delivery of Microsoft Teams integration that won Microsoft Partner of the Year.  
    """)

with st.expander("Loyal Healthcare – Engineering Manager (2023)"):
    st.write("""
    - Managed a 6-person full-stack engineering team working primarily in C#/.NET.  
    - Introduced Kanban workflows to optimize delivery cadence.  
    - Partnered with product leadership to align strategic roadmap.  
    - Designed career growth frameworks for team development.  
    """)

with st.expander("Idelic – Engineering Manager (2023–2024)"):
    st.write("""
    - Led two teams:  
        • Core Software (6 engineers, C#/MSFT stack)  
        • DevOps (3 engineers, Terraform, CI/CD, observability)  
    - Enhanced monitoring/observability with Datadog.  
    - Drove improvements in deployment reliability and infrastructure stability.  
    """)

with st.expander("SoftWriters – Automation Engineering Manager (2020–2022)"):
    st.write("""
    - Built an Automation Engineering team from scratch, growing from 2 → 5 engineers.  
    - Authored Python-based testing frameworks; enhanced reliability of C# legacy pharmacy systems.  
    - Developed and managed IaC with Terraform for AWS environments.  
    - Launched a performance testing program that identified DB bottlenecks, resulting in 40% AWS cost savings and improved app performance.  
    """)

with st.expander("Arcadia – Senior Software Engineer in Test (2019–2020)"):
    st.write("""
    - Designed and implemented an end-to-end testing suite to improve release confidence.  
    - Contributed to the company-wide migration from Cognito to Auth0 for secure authentication.  
    """)

with st.expander("MedCPU – Senior Quality Engineer (2016–2019)"):
    st.write("""
    - Created an HL7 simulation test harness using Python/Kafka, standardizing testing of Clinical Decision Support pathways.  
    - Partnered with NLP teams to validate clinical rule sets and terminology ontologies.  
    """)

with st.expander("UPMC Enterprises – Software Engineer (2014–2016)"):
    st.write("""
    - Contributed to multiple healthcare startup initiatives.  
    - Selected to help scale MedCPU following its acquisition by UPMC.  
    - Developed payment system software in C#/Java and served as Scrum Master.  
    """)

with st.expander("Compunetix – Software Engineer → Lead Engineer (2006–2014)"):
    st.write("""
    - Founded and built a dedicated web testing team for teleconferencing solutions.  
    - Implemented automation frameworks to ensure quality across a suite of web products.  
    - Progressed through multiple roles: software engineer, lead engineer, and test manager.  
    """)

# --- SKILLS ---
st.markdown("<div class='section-title'>🛠 Technical Skills & Expertise</div>", unsafe_allow_html=True)

skills = [
    ("Python", "python"),
    ("AWS (Lambda, API Gateway, Cloudwatch, SQS, SNS)", "aws"),
    ("Angular / React / TypeScript", "typescript"),
    ("CI/CD (Azure DevOps, Jenkins, CircleCI)", "devops"),
    ("Terraform / AWS CDK", "devops"),
    ("Snowflake / Glue / Kafka", "db"),
    ("SQL / MongoDB / Postgres", "db"),
    ("Leadership & Agile (SAFe, Scrum, Kanban)", "leadership"),
]

for skill, cls in skills:
    st.markdown(f"<span class='skill-badge {cls}'>{skill}</span>", unsafe_allow_html=True)

# --- WHY HIRE ME ---
st.markdown("<div class='section-title'>🚀 Why Hire Me?</div>", unsafe_allow_html=True)
st.write("""
- **Proven Team Builder & Leader** — Built and scaled engineering teams from scratch (Compunetix, SoftWriters), managed cross-functional groups of 3–12 engineers across multiple companies.  
- **Technical Depth + Breadth** — Hands-on expertise across **Python, C#/TypeScript/React, AWS serverless, and DevOps (Terraform/CDK, Azure DevOps CI/CD)**, combined with leadership in architecture and delivery.  
- **Innovation with Business Impact** — Designed testing frameworks (MedCPU, Arcadia) that became company standards, delivered performance programs that cut AWS costs by 40% (SoftWriters), and led MDM platform delivery mastering 2.5M+ records (Compass).  
- **Recognition & Results** — Led teams to industry recognition (**Microsoft Partner of the Year at MURAL**) and delivered high-stakes MVP launches in healthcare and enterprise SaaS.  
- **Adaptable & Trusted** — Selected for high-visibility initiatives (UPMC → MedCPU integration), consistently deliver results in dynamic, evolving environments.  
""")

# --- CONTACT ---
st.markdown("<div class='section-title'>📬 Contact</div>", unsafe_allow_html=True)
st.write("""
📧 [Email](mailto:wcweinberger@gmail.com) | 💼 [LinkedIn](https://www.linkedin.com/in/wcweinberger/) | 📱 724-366-3205  
""")

st.write("---")
st.write("Made with ❤️ using Streamlit")
