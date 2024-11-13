
# Anema Chat

Anema Chat is a chatbot application built using [Streamlit](https://streamlit.io/), featuring two AI chatbot integrations:
1. **Google Bard** – An AI model for general-purpose conversation.
2. **Hugging Face Hub** – Integrates with Hugging Face's `blenderbot-400M-distill` model for conversational AI.

## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [License](#license)

## Demo
![Anema Chat Demo](demo.gif)

## Features
- **Multi-Tab Interface**: Interact with either Google Bard or Hugging Face in separate tabs.
- **Chat History**: Keeps conversation history during the session.
- **Extra Features**: Includes sidebar buttons for microphone and audio options (future development).

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/anema-chat.git
    cd anema-chat
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

To use Anema Chat, you will need API keys for both **Google Bard** and **Hugging Face**:

1. **Google Bard**:
    - Set up your API key for Bard in an environment variable:
      ```bash
      export _BARD_API_KEY="YOUR_GOOGLE_BARD_API_KEY"
      ```

2. **Hugging Face**:
    - Set up your API key for Hugging Face in an environment variable:
      ```bash
      export HUGGINGFACE_API_KEY="YOUR_HUGGING_FACE_API_KEY"
      ```

## Usage

To run the application, use the following command:

```bash
streamlit run app.py
```

After running this command, a local URL (e.g., `http://localhost:8501`) will be displayed. Open it in your web browser to start using Anema Chat.

## Dependencies

- **Streamlit** - for creating the web interface.
- **bardapi** - for Google Bard integration.
- **requests** - for making API requests to Hugging Face.

To install all required libraries:
```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy chatting with AI using **Anema Chat**! Feel free to contribute, report issues, or suggest features via [Issues](https://github.com/yourusername/anema-chat/issues).

![image](https://github.com/user-attachments/assets/85a81041-44cf-4c77-8c27-dade305a400d)
