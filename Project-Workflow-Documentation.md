**Building an Interactive Portfolio Website with Streamlit and GitHub-Hosted Resume**

**Introduction**

This article explores the development of a dynamic, interactive portfolio website using Streamlit, a Python library for creating web applications with minimal effort. This portfolio application not only provides a rich user interface for showcasing a professional's skills and projects but also leverages GitHub for hosting and serving the resume, thus ensuring a seamless and accessible presentation.


**Architecture**

![image](https://github.com/user-attachments/assets/4b70a780-c0b2-4405-afc2-20a319dcd61d)


- User (Browser): The individual accessing the portfolio website.

- Streamlit Application: The core application that drives the website's functionality.

- Streamlit Server: The local server launched when running the Streamlit app. It interprets the Python code and generates the user interface (UI).

- Portfolio Web App (Python): This is where the Python script's logic resides, including defining the UI elements, data, interactions, and the overall application flow.

- GitHub API (Raw Content URL): The application utilizes the GitHub API by retrieving a file directly from a raw content URL.

- Resume (PDF): The PDF resume file stored in the GitHub repository.

- Streamlit UI Components: Pre-built UI elements such as dropdowns, text displays, download buttons provided by Streamlit that is used to create user friendly application.

**Process Flow**

1.User Interaction: The user initiates a request through their web browser to access the Streamlit application (e.g., navigating to the local URL where the app is running.)

2.Streamlit Server: Upon the request, the Streamlit Server comes into action. It starts to process the Python script, interpreting and executing its commands.

3.Web App Execution: The python script uses the Streamlit package to generate UI components such as sidebar selectbox, text descriptions, image renders and other UI components based on the logic in python program. Also, it fetches data from GitHub through a request made using the raw URL of the resume.

4.Resume Handling: The application directly access the PDF content using raw url. The Streamlit download_button component then allows the user to directly download the file as a PDF.

5.UI Generation: The processed data from application is rendered as a web page which will be presented to the user, providing the user interactive elements to engage with.

6.Interactive UI: User can select the sections via the side bar to navigate through different parts of the portfolio. The selected section will dynamically display content based on the logic of the python application.


