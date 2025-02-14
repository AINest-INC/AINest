# deepseek_integration.py
from deepseek_api import generate_code

def create_function_documentation(function_code, api_key):
    """Creates documentation for a given function using the DeepSeek API.

    Args:
        function_code (str): The code of the function.
        api_key (str): Your DeepSeek API key.

    Returns:
        str: The generated documentation if successful, None otherwise.
    """
    prompt = f"Generate documentation for the following Python function:\n{function_code}"
    return generate_code(prompt, api_key)

def generate_unit_tests(function_code, api_key):
    """Generates unit tests for a given function using the DeepSeek API.

    Args:
        function_code (str): The code of the function.
        api_key (str): Your DeepSeek API key.

    Returns:
        str: The generated unit tests if successful, None otherwise.
    """
    prompt = f"Generate unit tests for the following Python function:\n{function_code}"
    return generate_code(prompt, api_key)

if __name__ == '__main__':
    # Example usage:
    api_key = "YOUR_DEEPSEEK_API_KEY"
    function_code = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
"""
    documentation = create_function_documentation(function_code, api_key)
    if documentation:
        print("Documentation:")
        print(documentation)

    unit_tests = generate_unit_tests(function_code, api_key)
    if unit_tests:
        print("\nUnit Tests:")
        print(unit_tests)
    else:
        print("Failed to generate unit tests.")
