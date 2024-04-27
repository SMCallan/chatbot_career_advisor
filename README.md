# Guide: Making an AI Chatbot 
## Visual Studio Code, OpenAI API, and Python
### EXAMPLE: Career Advisor (highly customisable)

![image](https://github.com/SMCallan/chatbot_career_advisor/assets/126923185/772c8ac7-c162-4b8e-b892-43c156b928eb)


## Requirements
- Visual Studio Code (VSCode)
- Python
- pip
- PIL (Pillow) library
- OpenAI library
- OpenAI account with credits ($18 free credit available)

## Setup
1. Create a folder on your desktop called "Chatbot_RANDOMNAME".
2. Open the new directory (folder) using Visual Studio Code.

## Project Creation
1. Create a new file:
   - File > New File
   - Save the file as `main.py` in the project folder

## Library Installation
1. Open the terminal in VSCode.
2. (Optional) Create and activate a virtual environment using `venv`.
3. Install or update the required libraries using the following terminal commands:
   ```
   pip install --upgrade python
   pip install pillow
   pip install openai
   ```

## Application Development
1. Copy the code from the provided link into the `main.py` file.
2. Replace the placeholder API key in the code with your actual OpenAI API key.

## Implementation
1. Run the code.
2. If you encounter any issues, troubleshoot and repeat the steps as needed.
   - Tip: In programming, retrying the same steps can often resolve issues.
   - If you have any questions, search for solutions online or consult the documentation.

## OpenAI API Key
- Obtain an API key from OpenAI (keep the key secret).
  - Note: You can delete the key after revealing it and generate a new one if needed.
- OpenAI models are trained to industry standards and provide fine-tuning capabilities.
- Pricing is based on token usage. Refer to the OpenAI API pricing page for more information.
- You only pay for what you use, and the models are secure.

Remember to keep your API key confidential and avoid sharing it publicly. If you accidentally expose your key, make sure to revoke it and generate a new one from the OpenAI dashboard.

# Customise the Chatbot

## Here's a simple guide on how a user can modify certain parts of the code to make the model work differently:

1. Changing the AI Model:
   - In the `generate_career_advice` function, locate the line: `model="gpt-3.5-turbo"`.
   - Replace `"gpt-3.5-turbo"` with the name of another compatible OpenAI model, such as `"text-davinci-002"` or `"text-curie-001"`.
   - Different models have varying capabilities and specialties, so experimenting with different models can yield different results.

2. Modifying the System Message:
   - In the `generate_career_advice` function, find the line: `{"role": "system", "content": "You are a career advisor..."}`.
   - Update the content within the double quotes to change the system message that sets the behavior and persona of the AI.
   - For example, you could change it to: `"You are a life coach, providing guidance on personal growth and development..."`.
   - Modifying the system message allows you to alter the AI's purpose and the type of advice it provides.

3. Adjusting the User Questions:
   - In the `start_career_advice` function, locate the `questions` list.
   - Modify, add, or remove questions from the list to change the prompts presented to the user.
   - For instance, you could add a question like: `"What are your passions and hobbies?"`.
   - Changing the user questions will influence the input collected from the user and the resulting advice generated by the AI.

4. Customizing the Chatbot Responses:
   - Throughout the code, you'll find lines where the chatbot's responses are defined, such as: `"Chatbot: Hello! What is your name?\n"`.
   - Update the text within the double quotes to customize the chatbot's responses and personality.
   - For example, you could change the greeting to: `"Chatbot: Hi there! I'm excited to help you explore your career path. Can you tell me your name?\n"`.
   - Customizing the chatbot's responses allows you to tailor the user experience and make the interactions more engaging.

5. Modifying the Advice Formatting:
   - In the `generate_career_advice` function, the system message includes formatting instructions for the AI's response.
   - Adjust the formatting guidelines to change how the advice is presented to the user.
   - For instance, you could modify the bullet points to numbered steps or add a closing message.
   - Changing the advice formatting can enhance readability and make the output more visually appealing.

Remember to run the code after making any modifications to see the effects of your changes. Experimenting with different variations can help you create a unique and tailored AI chatbot experience.

Note: Make sure to handle any errors or exceptions that may arise due to the modifications you make to the code.

By following this guide and making incremental changes to the code, users can explore different possibilities and adapt the AI chatbot to suit their specific needs and preferences.

