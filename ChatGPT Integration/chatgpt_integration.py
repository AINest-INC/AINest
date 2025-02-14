# chatgpt_integration.py
from chatgpt_api import generate_text

def summarize_text(text, api_key):
    """Summarizes a text using the OpenAI ChatGPT API.

    Args:
        text (str): The text to summarize.
        api_key (str): Your OpenAI API key.

    Returns:
        str: The summarized text if successful, None otherwise.
    """
    prompt = f"Summarize the following text: {text}"
    return generate_text(prompt, api_key)

def translate_text(text, target_language, api_key):
    """Translates text to a target language using the OpenAI ChatGPT API.

    Args:
        text (str): The text to translate.
        target_language (str): The target language.
        api_key (str): Your OpenAI API key.

    Returns:
        str: The translated text if successful, None otherwise.
    """
    prompt = f"Translate the following text to {target_language}: {text}"
    return generate_text(prompt, api_key)

if __name__ == '__main__':
    # Example usage:
    api_key = "YOUR_OPENAI_API_KEY"
    text = "Artificial intelligence is revolutionizing many industries. It is used in healthcare, finance, and transportation."
    summary = summarize_text(text, api_key)
    if summary:
        print("Summary:")
        print(summary)

    translated_text = translate_text(text, "French", api_key)
    if translated_text:
        print("\nTranslated Text (French):")
        print(translated_text)
    else:
        print("Failed to translate text.")
