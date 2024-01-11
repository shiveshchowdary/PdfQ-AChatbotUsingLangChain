# Ask Your PDF with EchoBot

This application allows users to ask questions about a PDF document using the EchoBot, a helpful assistant powered by the OpenAI GPT-3.5 Turbo model. The application splits the PDF text into chunks, creates embeddings, and provides answers based on user questions.

## Getting Started

1. Clone the repository
2. Install the required dependencies:
3. Set up a virtual environment (optional but recommended)
4. Run the application:

## Usage

1. Open the application in your web browser.
2. Upload a PDF document using the file uploader.=
3. Ask a short question about the PDF in the chat input.=
4. The EchoBot will process your question, analyze the PDF content, and provide a relevant answer.

## Demo Images

- `image1.png`
- `image2.png`

These images capture moments from a demo using a resume PDF as an example. You can see the interaction with the application and how questions are asked and answered.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pythonhosted.org/PyPDF2/)
- [langchain](https://github.com/your-username/langchain) (custom library for text processing)
- [OpenAI GPT-3.5 Turbo](https://beta.openai.com/signup/) (requires API key)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Configuration

To use the OpenAI GPT-3.5 Turbo model, make sure to set up your API key. Create a `.env` file in the project root and add your API key:

```
OPENAI_API_KEY=your-api-key
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://beta.openai.com/) for providing the powerful GPT-3.5 Turbo model.
- [Streamlit](https://streamlit.io/) for the user interface framework.
- [langchain](https://github.com/your-username/langchain) for custom text processing capabilities.

Feel free to explore, contribute, and enhance the functionality of the Ask Your PDF application! If you encounter any issues or have suggestions, please open an issue or create a pull request.