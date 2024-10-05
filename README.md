ChatCart: Mall Chatbot

ChatCart is an AI-powered chatbot designed to enhance the shopping experience in malls by helping customers find specific products, store information, and current discounts. 
Built using Flask, Firebase, and NLP techniques, this chatbot allows shoppers to input their queries and receive relevant information seamlessly.

Table of Contents

Features
Technologies Used
Setup Instructions
Usage


Features

Query Processing: The chatbot tokenizes user input to effectively understand and process queries, improving response accuracy.
Product Lookup: Searches for products and their details in the Firebase database, providing real-time information to users.
Related Products: Suggests related products when the searched item is unavailable, ensuring users have alternatives.
User-Friendly Responses: Delivers responses in a clear, formatted manner for better readability.
CORS Enabled: Supports cross-origin requests for seamless integration with various frontend applications.
Error Handling: Includes mechanisms for managing errors during data fetching to enhance user experience.


Technologies Used

Flask: A lightweight WSGI web application framework for Python.
Firebase: Used for real-time database storage and management, ensuring data is up-to-date.
Python: The programming language for backend development, leveraging its simplicity and efficiency.
CORS: Allows resources to be shared across different origins, facilitating smooth interactions between the frontend and backend.


Setup Instructions

To set up and run the ChatCart chatbot locally, follow these steps:

Clone the repository and navigate to the project directory.
Create a virtual environment (optional but recommended) for managing dependencies.
Install the required packages as listed in the requirements.txt file.
Set up Firebase by creating a project and a Realtime Database, and ensure the Admin SDK JSON file is configured correctly.
Run the application to start the server locally.


Usage

To interact with the chatbot, send a POST request to the /query endpoint with a JSON body containing the user query. The chatbot processes the query and returns relevant product information based on the database entries.

Example Interaction
Users can simply type in their product queries, such as "laptop" or "shoes," and the chatbot will provide information about availability, discounts, and related products.

Additional Points

Scalability: The chatbot is designed to handle multiple user queries simultaneously, making it suitable for high-traffic environments like shopping malls.
Customizability: Users can easily modify the query processing logic or the database structure to suit specific needs.
Integration: The chatbot can be integrated with various frontend frameworks or platforms, allowing for a versatile user interface.
User Feedback: Incorporating user feedback can help refine the chatbot's responses and enhance overall user satisfaction.
Future Enhancements: Potential features could include voice recognition for queries, user account management, and more sophisticated NLP techniques for improved understanding.
