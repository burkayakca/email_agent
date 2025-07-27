# E-Mail Agent

## Description

The Email Agent is a Python-based email agent that leverages the Google ADK (Agent Development Kit) to send emails. It uses the `smtplib` library for sending emails and the `dotenv` library to manage environment variables.

## Features

-   Sends emails to specified recipients.
-   Customizable email subject and message.
-   Uses environment variables for sensitive information like email credentials.

## Requirements

-   Python 3.6+
-   Google ADK
-   `smtplib`
-   `dotenv`
-   An email account with SMTP enabled (e.g., Gmail with an app password)

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/burkayakca/email_agent.git
    cd <repository_directory>
    ```

2.  Install the required Python packages:

    ```bash
    pip install google-adk python-dotenv
    ```

## Configuration

1.  Rename the `_env` file to `.env`.
2.  Update the `.env` file with your email credentials and Google API key:

    ```
    GOOGLE_API_KEY=<Your_Google_API_Key>
    GOOGLE_GENAI_USE_VERTEXAI=FALSE
    SENDER_EMAIL="your_email@gmail.com"
    SENDER_PASSWORD="your_app_password"
    ```

    **Note:** For Gmail, you need to create an App Password for security reasons. You can generate one in your Google Account settings under Security. (Make you sure two-factor login is already enable)

## Usage

1.  Import the agent in your Python script:

    ```python
    from email_agent import agent
    ```

2.  Use the `emailTool` function to send emails:

    ```python
    from email_agent.agent import emailTool

    recipient_email = "recipient@example.com"
    subject = "Test Email"
    message = "This is a test email sent from the MIME Agent."

    result = emailTool(recipient_email, subject, message)
    print(result)  # Output: Successful! or Message could not be send
    ```

3.  Alternatively, you can use the `root_agent` directly with the Google ADK:

    ```python
    from email_agent.agent import root_agent

    # Example usage with Google ADK (replace with actual ADK implementation)
    response = root_agent.run(prompt="Send an email to recipient@example.com with subject 'Test' and message 'Hello'")
    print(response)
    ```


## Environment Variables

-   `GOOGLE_API_KEY`: Your Google API key.
-   `GOOGLE_GENAI_USE_VERTEXAI`:  A boolean to specify whether to use Google's Vertex AI.
-   `SENDER_EMAIL`: The email address used to send emails.
-   `SENDER_PASSWORD`: The password or app password for the sender email account.

## Dependencies

-   google-adk
-   smtplib
-   dotenv
-   os

