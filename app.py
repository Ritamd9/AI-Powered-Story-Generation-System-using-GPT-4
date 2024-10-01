import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = "OPEN-API-KEY"

def generate_story(prompt, max_tokens=500, temperature=0.7):
    """
    Generates a story based on the given prompt using OpenAI's GPT-4 API.
    
    Args:
    prompt (str): The input text prompt for the story.
    max_tokens (int): Maximum number of tokens to generate (default 500).
    temperature (float): Controls randomness/creativity (default 0.7).
    
    Returns:
    str: The generated story.
    """
    try:
        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            n=1,
            stop=None
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit app interface
st.title("AI-Powered Story Generator")

# Input: Story prompt from the user
prompt = st.text_area("Enter your story prompt", placeholder="Once upon a time...")

# Input: Maximum number of tokens for the story generation
max_tokens = st.slider("Select the length of the story (in tokens)", min_value=100, max_value=1000, value=500, step=50)

# Input: Temperature control for creativity
temperature = st.slider("Creativity level (temperature)", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

# Generate story when button is clicked
if st.button("Generate Story"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt to generate a story!")
    else:
        st.write("Generating story, please wait...")
        story = generate_story(prompt, max_tokens=max_tokens, temperature=temperature)
        st.subheader("Generated Story:")
        st.write(story)

# Streamlit app with genre selection
st.title("AI-Powered Story Generator")

# Input: Story prompt from the user
prompt = st.text_area("Enter your story prompt", placeholder="Once upon a time...")

# Input: Select genre
genre = st.selectbox("Select a genre", ["Fantasy", "Sci-Fi", "Mystery", "Adventure", "Romance", "Horror"])

# Input: Maximum number of tokens for the story generation
max_tokens = st.slider("Select the length of the story (in tokens)", min_value=100, max_value=1000, value=500, step=50)

# Input: Temperature control for creativity
temperature = st.slider("Creativity level (temperature)", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

# Modify the prompt based on the selected genre
if genre:
    prompt = f"{genre} Story: {prompt}"

# Generate story when button is clicked
if st.button("Generate Story"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt to generate a story!")
    else:
        st.write("Generating story, please wait...")
        story = generate_story(prompt, max_tokens=max_tokens, temperature=temperature)
        st.subheader("Generated Story:")
        st.write(story)

if story:
    st.download_button(
        label="Download Story as .txt",
        data=story,
        file_name="generated_story.txt",
        mime="text/plain",
    )

