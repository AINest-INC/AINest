# stable_diffusion_integration.py
from stable_diffusion_api import generate_image

def create_image_variation(base_image_path, prompt, api_key):
    """Creates a variation of an existing image using Stable Diffusion.

    Args:
        base_image_path (str): The path to the base image.
        prompt (str): The prompt to guide the variation.
        api_key (str): Your Stability AI API key.

    Returns:
        PIL.Image.Image: The generated image variation if successful, None otherwise.
    """
    # In a real implementation, you would need to send the base image to the API.
    # This is a simplified example that only uses the prompt.
    full_prompt = f"A variation of the image at {base_image_path} with the following changes: {prompt}"
    return generate_image(full_prompt, api_key)

def generate_image_from_text(prompt, api_key):
    """Generates an image from a text prompt using Stable Diffusion.

    Args:
        prompt (str): The prompt to generate the image from.
        api_key (str): Your Stability AI API key.

    Returns:
        PIL.Image.Image: The generated image if successful, None otherwise.
    """
    return generate_image(prompt, api_key)

if __name__ == '__main__':
    # Example usage:
    api_key = "YOUR_STABILITY_AI_API_KEY"
    prompt = "A cat wearing a hat."
    image = generate_image_from_text(prompt, api_key)
    if image:
        image.save("cat_with_hat.png")
        print("Image generated and saved to cat_with_hat.png")

    # Example of image variation (requires a base image)
    # base_image_path = "cat_with_hat.png"  # Replace with an actual image path
    # variation_prompt = "Make the cat more fluffy."
    # variation_image = create_image_variation(base_image_path, variation_prompt, api_key)
    # if variation_image:
    #     variation_image.save("fluffy_cat.png")
    #     print("Image variation generated and saved to fluffy_cat.png")
