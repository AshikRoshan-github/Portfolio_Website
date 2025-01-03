import streamlit as st
import requests

# Set Page Configuration with theme styling
st.set_page_config(
    page_title="Portfolio | Ashik Roshan",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS for theme styling
st.markdown("""
    <style>
        /* Apply light theme and serif font */
        body {
            background-color: #f5f5f5; /* Light background */
            color: #333333; /* Dark text */
            font-family: 'Times New Roman', serif; /* Serif font */
        }

        /* Rainbow Heading Styling */
        .rainbow-line {
            font-size: 24px;
            font-weight: bold;
            position: relative;
            margin-bottom: 0.5rem;
            display: block;
            width: 100%;
        }
        .rainbow-line::after {
            content: '';
            display: block;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, #f12711, #f5af19); /* Red-to-orange gradient */
            margin-top: 4px;
        }

        /* Sidebar Customization */
        [data-testid="stSidebar"] {
            color: #333333;
            border-right: 3px solid #e67e22; /* Orange border */
            box-shadow: 3px 0px 8px rgba(0, 0, 0, 0.1); /* Soft shadow */
            padding: 16px;
            background-color: #ffffff; /* White background */
        }

        /* Sidebar Header */
        div[data-testid="stSidebar"] h2 {
            color: #e67e22; /* Orange header text */
            font-size: 18px; /* Reduced font size */
            font-weight: bold;
            margin-bottom: 16px;
            text-align: center;
        }
        
        /* Sidebar Dropdown Label */
        div[data-testid="stSidebar"] label {
            color: #333333; /* Dark label text */
            font-size: 10px; /* Reduced font size */
            font-weight: bold;
            margin-top: 12px;
        }

        /* Sidebar Dropdown Style */
        div[data-testid="stSidebar"] select {
        color: #333333; /* Dark text */
        border-radius: 12px;
        border: 2px solid #e67e22; /* Orange border */
        padding: 10px;
        margin-top: 8px;
        transition: all 0.3s ease;
        border: 2px solid #e67e22;  /* Add border here */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Optional shadow effect */
        }

        div[data-testid="stSidebar"] select:hover {
            color: #333333;
        }

        /* Sidebar Buttons */
        div[data-testid="stSidebar"] button {
            color: #ffffff;
            font-size: 12px; /* Reduced font size */
            padding: 10px 14px;
            border-radius: 20px;
            margin-top: 16px;
            border: none;
            transition: transform 0.2s ease, background 0.3s ease;
        }

        div[data-testid="stSidebar"] button:hover {
            transform: scale(1.05); /* Slight zoom effect */
            cursor: pointer;
        }

        /* Download Button Styling */
        div[data-testid="stSidebar"] .stDownloadButton {
            background-color: #f39c12; /* Gold button */
            color: #ffffff;
            font-weight: bold;
            padding: 14px;
            border-radius: 25px;
            width: 100%;
            margin-top: 20px;
            transition: all 0.3s ease;
        }

        div[data-testid="stSidebar"] .stDownloadButton:hover {
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Add shadow */
            transform: translateY(-2px); /* Lift effect */
        }
    </style>
""", unsafe_allow_html=True)

# Define sections
sections = {
    "Introduction":"Introduction",
    "Professional Summary": "professional_summary",
    "Educational Qualification": "educational_qualification",
    "Technical Skills": "technical_skills",
    "Certifications": "certifications",
    "Projects": "projects",
    "Contact Info.": "contact_information"
}

# Sidebar with selectbox
selected_section = st.sidebar.selectbox(
    "**Please select the section of your preference:**", 
    list(sections.keys()), 
    index=0
)


# GitHub raw URL of the resume
github_raw_url = "https://raw.githubusercontent.com/AshikRoshan-github/Portfolio_Website/main/Resume.pdf"

# Fetch the file content from GitHub
response = requests.get(github_raw_url)

if response.status_code == 200:
# Resume Download Button in Sidebar
    st.sidebar.download_button(
        label="**Download Resume**",
        data=response.content,
        file_name="AshikRoshan_DataEngineer_Resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )
else:
    st.error(f"Failed to fetch the file. HTTP Status Code: {response.status_code}")

# Rainbow Heading Function
def rainbow_heading(text):
    st.markdown(f"<div class='rainbow-line'>{text}</div>", unsafe_allow_html=True)

# Render Section Content Based on Selected Section
def render_section(section):
    if section == "professional_summary":
        rainbow_heading("🚀 Professional Summary")
        st.markdown(
            """
            Dynamic and results-driven technology professional with expertise in programming, cloud computing, data engineering, and analytics.

            - Skilled in designing and implementing scalable data pipelines to optimize ETL/ELT processes, enabling efficient ingestion, transformation, and loading of structured and unstructured data.
            - Experienced in building and managing data integration workflows and orchestrating tasks to ensure seamless connectivity across diverse systems and applications.
            - Proficient in data modeling, schema design, and managing complex data ecosystems to ensure accessibility, reliability, and optimal performance.
            - Adept at leveraging Generative AI (GENAI) and Large Language Models (LLMs) to automate workflows, enhance data-driven decision-making, and deliver innovative real-time solutions.
            - Advanced expertise in web scraping and web crawling, focusing on automated data extraction, real-time monitoring, and deep analysis to support critical business operations.
            - Passionate about applying artificial intelligence and machine learning to solve real-world problems, drive automation, and foster innovation in complex environments.
            - Recognized for strong leadership, exceptional organizational skills, and a commitment to adopting cutting-edge technologies to deliver impactful, data-driven solutions.
            """
        )
    
    elif section == "Introduction":
        rainbow_heading("Introduction")
        st.markdown("""
            <style>
            .intro-container {
                display: flex;
                flex-direction: column;
                max-width: 1200px;
                margin: 0 auto;
                padding: 1rem;
            }

            .content-section {
                width: 100%;
                margin-bottom: 2rem;
            }

            .image-section {
                width: 100%;
                display: flex;
                justify-content: center;
            }

            .profile-image {
                width: 500px;
                height: 300px;
                object-fit: cover;
                border-radius: 8px;
            }

            .intro-title {
                font-size: 2rem;
                color: #333;
                margin: 0.5rem 0;
            }

            .name-title {
                font-size: 2.5rem;
                color: #1a1a1a;
                margin: 0.5rem 0;
            }

            .role-title {
                font-size: 1.5rem;
                color: #444;
                margin: 0.5rem 0 1.5rem 0;
            }

            .intro-text {
                font-size: 1rem;
                line-height: 1.6;
                color: #555;
            }
            /* Project Section Styling */
            .project-card {
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                padding: 16px;
                margin-bottom: 16px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }
            .project-card:hover {
                box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
                transform: scale(1.02);
                transition: all 0.3s ease-in-out;
            }
            .project-title {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 8px;
            }
            .project-details {
                font-size: 14px;
                line-height: 1.6;
                color: #555555;
            }

            </style>

            <div class="intro-container">
                <div class="content-section">
                    <h2 class="intro-title">Hello,</h2>
                    <h1 class="name-title">I'm Ashik Roshan I!</h1>
                </div>
                <div class="image-section">
                    <img src="https://cdn.dribbble.com/users/3484830/screenshots/16787618/media/b134e73ef667b926c76d8ce3f962dba2.gif" alt="Profile Illustration" class="profile-image">
                </div>
                <br>
                <div class="content-section">
                    <h3 class="role-title">Data Engineer</h3>
                    <p class="intro-text">
                        I am a results-oriented professional with a strong passion for technology and data-driven solutions. With a natural aptitude for leadership and a strategic approach, I excel in optimizing processes and enhancing efficiency. My expertise spans across programming, ELT/ETL tools, and cutting-edge data methodologies, with a particular focus on using generative AI and large language models (LLMs) to solve real-time problems and automate tasks. I also bring experience in cloud technologies such as AWS and Azure, and have a proven ability to extract actionable insights through web scraping and crawling techniques.
                    </p>
                </div>
 
            </div>
        """, unsafe_allow_html=True)




    elif section == "educational_qualification":
        rainbow_heading("🎓📚 Educational Qualification")
        st.markdown(
            """
            - **Bachelor of Engineering (B.E. Computer Science):** K.L.N. College of Engineering, Madurai, Tamil Nadu, India.
            """
        )
    elif section == "technical_skills":
        rainbow_heading("💡 Technical Skills")
        st.markdown(
            """
            - **Programming Languages:** Python, SQL, JavaScript, HTML, CSS
            - **Cloud Platforms & Services:** Azure Blob Storage, Azure Data Lake, Azure SQL Database, Azure Open AI, Azure Databricks, AWS S3, AWS Lambda, AWS Glue, AWS Step Functions
            - **Data Engineering & Analytics:** ADF (Azure Data Factory), PySpark, DBT (Data Build Tool), Informatica, Snowflake, Power BI, ThoughtSpot
            - **Automation & Web Development:** Selenium, Web Scraping, Web Crawling, FastAPI
            - **Development Tools & Version Control:** GitHub, Putty
            - **Database Management & Administration:** SSMS (SQL Server Management Studio), pgAdmin, MySQL
            - **AI & Machine Learning:** Azure Document Intelligence, GenAI
            """
        )
    elif section == "certifications":
        rainbow_heading("🏅 Certifications")
        st.markdown(
            """
            - Microsoft: Azure Data Fundamentals
            - Snowflake: Snowpro Core Certification
            - Databricks: Databricks Lakehouse Fundamentals
            - dbt Labs: DBT Learn Fundamental
            - Udemy: 100 Days of Code - Python Bootcamp
            - Udemy: Snowflake – The Complete Masterclass (2023 Edition)
            - HackerRank: SQL (Basic) Certificate

            """
        )

    elif section == "projects":
        rainbow_heading("⚙️🔧 Projects")
        projects = [
            {
                "name": "**Jiffy-Hanover Data Migration**",
                "details": """
                **Technologies Utilized:** Azure Data Lake, Azure Data Factory (ADF), SQL Server Management Studio (SSMS), GitHub, Python
                
                **Project Description:**  
                The Jiffy-Hanover Data Migration project aimed at transitioning data from a legacy database to an updated data system, leveraging Azure-based technologies and automation to ensure efficient migration and transformation processes.
                
                **Key Phases of the Project:**
                
                - **Legacy System Data Mapping:**  
                    Thoroughly analyzed the legacy database schema to understand its structure and domain-specific requirements.  
                    Mapped data from the legacy system to the new database schema, ensuring compatibility and alignment with business rules.
                
                - **Data Migration with Azure Data Factory:**  
                    Migrated data stored in CSV format within Azure Data Lake to the legacy database (SSMS) using Azure Data Factory pipelines.  
                    Configured ADF pipelines, linked services, and datasets to manage the entire data migration workflow efficiently.
                
                - **Data Transformation & Processing:**  
                    Leveraged Python scripts to perform advanced data transformation tasks that went beyond ADF’s native capabilities.  
                    After transformation, the processed data was stored in Azure Data Lake before being transferred to the legacy system.
                
                - **Automation and Version Control:**  
                    Used Azure Data Factory Data Flows for most of the transformations to ensure automated, scalable data processing.  
                    Implemented version control for pipeline configurations, scripts, and resources through GitHub to maintain proper change management and facilitate collaboration among the development team.
                
                - **Testing & Data Validation:**  
                    Conducted unit testing of the migration process using Python to validate the accuracy and integrity of the data before it was handed over for formal QA testing.  
                    Ensured that data transformations were accurate, complete, and met business requirements.
                
                **Project Outcome:**  
                The migration was completed successfully, with a seamless transition of data from the legacy database to the new system. The solution demonstrated improved data accuracy, better scalability for future migrations, and enhanced operational efficiency through automation.
                """
            },
            {
                "name": "**Republic Services (RS) Data Migration**",
                "details": """
                **Technologies Used:** Informatica, SQL Server Management Studio (SSMS), Snowflake, DBT, AWS Step Functions, Putty, GitHub, Oracle
                
                **Project Overview:**  
                The Republic Services Data Migration project is focused on migrating data from the US Ecology systems to Republic Services (RS), integrating data from multiple sources including Azure SQL Server, Oracle, and MS SQL into a Snowflake staging schema. Informatica was employed as the ETL tool to load the data into Snowflake, and DBT was utilized for data transformation and movement from the staging schema to the Operational Data Store (ODS) schema. This end-to-end migration was carried out across four environments: DEV, STG, QA, and PROD, ensuring a reliable, scalable, and automated data pipeline for ongoing data processing.
                
                **Key Contributions and Steps:**
                
                - **ETL Pipeline Development and Maintenance:**  
                    Designed, developed, and maintained ETL pipelines in Informatica to handle both initial full loads and incremental data loads, ensuring the smooth migration of large volumes of data into Snowflake.  
                    Configured daily pipeline runs to automate data loading, monitoring for potential issues, and implementing resolutions to ensure continuous operation.
                
                - **Data Transformation Using DBT:**  
                    Utilized DBT Core integrated with Visual Studio Code for efficient data transformations within Snowflake.  
                    Automated the transition of data from the staging schema to the ODS schema, orchestrated by AWS Step Functions, ensuring optimal data flow across environments.
                
                - **Quality Assurance and Data Integrity:**  
                    Developed custom DBT macros for data validation, ensuring that data transformations were accurate, met business requirements, and maintained data consistency throughout the migration process.  
                    Conducted extensive data quality checks across DEV, STG, QA, and PROD environments to ensure that the data met integrity standards before moving to production.
                
                - **Testing and Automation:**  
                    Performed both manual and automated unit testing using Python scripts to validate the correctness of data loads and transformations.  
                    Worked closely with the testing team to address and resolve any discrepancies, ensuring that the data migration process adhered to strict business rules.
                
                - **Version Control and Deployment:**  
                    Utilized GitHub for version control, ensuring that all code, configurations, and scripts were properly maintained and easily accessible for collaborative development efforts.
                
                **Project Outcome:**  
                The RS Data Migration project successfully migrated large datasets from multiple sources into Snowflake, automating data loads and transformations, and ensuring high-quality data across all environments. The integration of AWS Step Functions, Informatica, DBT, and Snowflake streamlined the migration process, enhanced operational efficiency, and ensured data integrity, enabling seamless reporting and analytics for Republic Services.
                """
            },
            {
                "name": "**CycleCommerce Insight**",
                "details": """
                **Technologies Used:** Python, SQL Server, Snowflake, Azure Data Factory (ADF), Azure Storage Service, Power BI
                
                **Project Overview:**  
                The CycleCommerce Performance Analysis project was initiated to enhance business insights and inform decision-making by analyzing transactional data from the online store. The project encompassed a comprehensive approach, involving data migration, modeling, transformation, visualization, and the generation of actionable insights to drive business growth.
                
                **Key Contributions and Steps:**
                
                - **Data Extraction and Transformation:**  
                    Developed Python scripts to extract and transform raw transactional data from various sources associated with the online store.  
                    Loaded the transformed data into SQL Server, preparing it for advanced data processing and analysis.
                
                - **Data Orchestration with Azure Data Factory (ADF):**  
                    Utilized Azure Data Factory to orchestrate the seamless movement of data from SQL Server to Azure Blob Storage, ensuring smooth and efficient data transfer between systems.  
                    Implemented data synchronization strategies, enabling real-time data updates and ensuring consistency across platforms.
                
                - **Data Loading and Staging in Snowflake:**  
                    Managed the transfer of data from Azure Blob Storage into Snowflake using external staging, maintaining strict data integrity and security protocols throughout the process.  
                    Ensured that the data was readily available and optimized for use within the Snowflake environment for advanced analytics.
                
                - **Data Modeling and Optimization in Snowflake:**  
                    Created and implemented data models within Snowflake, structuring the e-commerce transaction data to improve accessibility and performance for analytical tasks.  
                    Optimized data schemas to enhance query performance and support reporting and business intelligence processes.
                
                - **Visualization and Insights with Power BI:**  
                    Designed and developed Power BI dashboards to visualize key performance indicators (KPIs) from the transaction data.  
                    Provided actionable insights to the business team, supporting data-driven decision-making and identifying opportunities for optimization within the online store.
                
                **Project Outcome:**  
                The CycleCommerce Performance Analysis project successfully enhanced business intelligence by efficiently migrating, transforming, and modeling data for advanced analytics. By leveraging Snowflake, ADF, and Power BI, the project provided real-time insights into business performance, enabling data-driven decisions and supporting continuous growth for the online store.
                """
            }
        ]

        for project in projects:
            with st.expander(project["name"]):
                st.markdown(project["details"])

    elif section == "contact_information":
        rainbow_heading("📬 Contact Information")
        st.markdown("""
            <style>
                .contact-container {
                    display: flex;
                    flex-direction: column;
                    align-items: left;
                    justify-content: center;
                    margin-top: 2rem;
                }
                .contact-item {
                    display: flex;
                    align-items: center;
                    margin-bottom: 1rem;
                }
                .contact-icon {
                    width: 24px;
                    height: 24px;
                    margin-right: 10px;
                }
                .contact-text {
                    font-size: 16px;
                    color: #555;
                    text-decoration: none;
                }
            </style>

            <div class="contact-container">
                <!-- GitHub Link -->
                <div class="contact-item">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" class="contact-icon" alt="GitHub"/>
                    <a href="https://github.com/AshikRoshan-github" target="_blank" class="contact-text">GitHub</a>
                </div>
                <!-- LinkedIn Link -->
                <div class="contact-item">
                    <img src="https://images.rawpixel.com/image_png_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvdjk4Mi1kMy0xMC5wbmc.png" class="contact-icon" alt="LinkedIn"/>
                    <a href="https://www.linkedin.com/in/ashik-roshan-i-073897249?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B3kvXfdbXQuuS2%2FBrgZQ0YA%3D%3D" target="_blank" class="contact-text">LinkedIn</a>
                </div>
                <!-- Gmail Address -->
                <div class="contact-item">
                    <img src="https://png.pngtree.com/template/20190725/ourmid/pngtree-gmail-logo-png-image_282635.jpg" class="contact-icon" alt="Gmail"/>
                    <a href="mailto:ashikroshan261@gmail.com" class="contact-text">ashikroshan261@gmail.com</a>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        🌟 I cordially invite you to explore my **GitHub repository** 💻, where I showcase a diverse array of open-source contributions in the realms of generative AI 🤖 and data-centric projects 📊.

        ✨ Additionally, I encourage you to visit my **LinkedIn profile** 🔗 to gain deeper insights into my professional accomplishments 🏆, prestigious accolades 🥇, industry standards 📜, and thought-provoking posts 💡.

        🚀 **Do not miss the opportunity to connect through these platforms!**
        """)


render_section(sections[selected_section])

# Footer
st.markdown("---")
st.markdown("© 2025 Ashik Roshan. Built with Streamlit.")
