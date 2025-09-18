from google import genai
from dotenv import load_dotenv
import os
from firecrawl import Firecrawl
import validators
import requests
from io import BytesIO
from PIL import Image
import questionary
from datetime import datetime

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY must be set in environment variables")
if not firecrawl_api_key:
    raise ValueError("FIRECRAWL_API_KEY must be set in environment variables")

client = genai.Client(api_key=gemini_api_key)
firecrawl = Firecrawl(api_key=firecrawl_api_key)


def is_valid_url(url: str):
    """Validate if the input string is a valid URL and return normalized URL"""
    try:
        # Add https:// if no scheme is provided
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        if validators.url(url):
            return url
        return False
    except Exception:
        return False


def get_image_from_url(url: str):
    """Get the image from the given URL"""
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))


def generate_filename(prefix: str) -> str:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{prefix}_{stamp}.png"


def scrape_website_screenshot(url: str):
    """Capture screenshot of the given URL using Firecrawl and return the screenshot URL"""
    try:
        result = firecrawl.scrape(url=url, formats=["screenshot"])

        if result and hasattr(result, "screenshot") and result.screenshot:
            return result.screenshot
        else:
            return None

    except Exception as e:
        print(f"Error scraping website: {str(e)}")
        return None


def edit_screenshot(
    image: Image.Image, prompt: str, version: int, filename_suffix: str = ""
):
    """Edit the screenshot using Gemini 2.5 Flash"""
    try:
        full_prompt = f"""
        You will be given a screenshot of a website and a user provided prompt. You need to edit the website screenshot to help address the user's prompt.
        The user's prompt is: {prompt}.
        """

        print("Editing screenshot...")
        response = client.models.generate_content(
            model="gemini-2.5-flash-image-preview", contents=[full_prompt, image]
        )

        if response.candidates[0].content.parts is None:
            print("No response from Gemini")
            return None

        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image = Image.open(BytesIO(part.inline_data.data))
                filename = generate_filename(
                    f"edited_screenshot_v{version}{filename_suffix}"
                )
                image.save(filename)
                print(f"Image saved to {filename}")
                return image
    except Exception as e:
        print(f"Error editing screenshot: {str(e)}")
        return None


def main():
    try:
        current_image = None
        reference_stack = []
        version = 0

        while True:
            url = input("Enter a website URL: ").strip()
            if not url:
                print("Please enter a valid URL.")
                continue

            normalized_url = is_valid_url(url)
            if not normalized_url:
                print("Invalid URL format. Try e.g. https://google.com or google.com")
                continue

            print(f"Capturing screenshot of {normalized_url}...")
            screenshot_url = scrape_website_screenshot(normalized_url)
            if not screenshot_url:
                print("Failed to capture screenshot.")
                retry = (
                    input("Would you like to try another URL? (y/n): ").strip().lower()
                )
                if retry != "y":
                    break
                continue

            try:
                current_image = get_image_from_url(screenshot_url)
                print("Screenshot captured successfully!")
            except Exception as e:
                print(f"Failed to download screenshot: {e}")
                continue

            # Reset versioning for a fresh URL
            version = 0
            reference_stack = [current_image]  # v1 will be produced from this reference

            while True:
                prompt = input("Enter a prompt to edit the screenshot: ").strip()
                if not prompt:
                    continue

                version += 1
                reference_image = reference_stack[-1]  # last reference used
                edited_image = edit_screenshot(reference_image, prompt, version)
                if not edited_image:
                    print("Failed to edit screenshot.")
                    again = input("Try a different prompt? (y/n): ").strip().lower()
                    if again == "y":
                        version -= 1  # don't consume a version number on failure
                        continue
                    else:
                        break

                current_image = edited_image
                # For "edit further", the new reference becomes the current result
                reference_stack.append(current_image)

                # Choice loop - shows choices after each edit/redo
                while True:
                    choices = [
                        "Edit the screenshot further",
                        "Redo last edit with a new prompt",
                        "Start over with a new URL",
                        "Exit",
                    ]
                    choice = questionary.select(
                        "What would you like to do next?", choices=choices
                    ).ask()
                    if not choice:
                        print("No selection. Exiting.")
                        return

                    if choice == "Edit the screenshot further":
                        # Break out of choice loop to ask for new prompt
                        break

                    elif choice == "Redo last edit with a new prompt":
                        # Pop the last reference because redo should use the SAME reference as the current version
                        if len(reference_stack) >= 2:
                            redo_reference = reference_stack[
                                -2
                            ]  # the reference used for current version
                        else:
                            redo_reference = reference_stack[-1]

                        redo_prompt = input(
                            "Enter a new prompt to redo the last edit: "
                        ).strip()
                        if not redo_prompt:
                            continue  # Stay in choice loop

                        redo_image = edit_screenshot(
                            redo_reference,
                            redo_prompt,
                            version,
                            filename_suffix="-redo",
                        )
                        if not redo_image:
                            print("Failed to generate redo image.")
                        else:
                            print(
                                "Redo image generated (current image remains unchanged)."
                            )
                        # Stay at same version; do not alter stack or current_image
                        # Continue in choice loop to show choices again
                        continue

                    elif choice == "Start over with a new URL":
                        break  # break choice loop -> break editing loop -> ask for url again

                    elif choice == "Exit":
                        return

                # If we broke out of the choice loop, check if it was "Start over"
                if choice == "Start over with a new URL":
                    break  # break editing loop -> ask for url again

    except KeyboardInterrupt:
        print("\nExiting...")
        return


if __name__ == "__main__":
    main()
