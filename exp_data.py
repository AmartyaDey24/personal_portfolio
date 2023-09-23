#This file contains all the data for experinces. Edit/add here for any changes in the experiences

from flask import url_for

class Exp_data:
    def get_exp_data():
        experiences = [
            {
                "start_date": "March 2023",
                "end_date": "September 2023",
                "company_name": "Natwest Group",
                "role": "Software Engineer Intern",
                "logo_url": url_for('static', filename='assets/company_logo/natwest.png'),
                "image_height": "100px",
                "image_weight": "100px",
                "linkedin_url": "https://www.linkedin.com/company/natwest-group/",
                "details": [
                    "Full-Stack Web Development: I gained hands-on experience in full-stack web development using Python Flask framework and SQLite database while working as a software engineering intern on the TAM portal project at Natwest Group.",
                    "Feature Development and Testing: My responsibilities included developing new features, conducting comprehensive testing, and debugging code to ensure the functionality and reliability of the TAM portal project..",
                    "Collaboration and Skill Enhancement: I had the opportunity to collaborate with experienced professionals in the field, which enabled me to deepen my technical skills, enhance my problem-solving abilities, and improve my communication and teamwork skills."
                ],
            },
            {
                "start_date": "August 2022",
                "end_date": "September 2022",
                "company_name": "Gnani.ai",
                "role": "Android Developer Intern",
                "logo_url": url_for('static', filename = 'assets/company_logo/gnani.png'),
                "image_height": "90px",
                "image_weight": "90px",
                "linkedin_url": "https://www.linkedin.com/company/gnani-ai/",
                "details": [
                    "Key Android Development Contributions: As an Android Developer Intern at Gnani.ai, I played a vital role in mobile app development, focusing on UI design, seamless API integration, and thorough testing to ensure exceptional user experiences in our Android applications.",
                    "Created a backbone.js-like framework for the Captions editor."
                ],
            },
            {
                "start_date": "April 2022",
                "end_date": "June 2022",
                "company_name": "Yenveez",
                "role": "Android Developer Intern",
                "logo_url": url_for('static', filename = 'assets/company_logo/yenveez.png'),
                "image_height": "60px",
                "image_weight": "60px",
                "linkedin_url": "https://www.linkedin.com/company/yenveez/",
                "details": [
                    "Immersive Android App Development: During my tenure as an Android Development Intern at Yenveez, I had the opportunity to deeply engage in mobile app development. I actively participated in designing and implementing Android applications, focusing on enhancing user interfaces and seamlessly integrating APIs to expand app functionality.",
                    "Rigorous Testing and Debugging: I played an essential role in the testing and debugging phase of our projects, diligently working to ensure a smooth and error-free user experience within the Android applications I contributed to."
                ]
            }
        ]

        return experiences