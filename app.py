import gradio as gr
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
def translation(text_translation):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Translate this text \"{}\" to Spanish.".format(text_translation),
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return "Your text in Spanish is" + response["choices"][0]["text"] + "!!"

text_translation = gr.Interface(fn=translation, inputs=gr.Textbox(lines=2, label="English text", placeholder="Type here"), outputs=gr.Textbox(lines=2, label="Spanish text", placeholder="See translation here"),live=False, description="The app translates text from English to Spanish using GPT-3 via OpenAI API.", title='Translator English to Spanish')

text_translation.launch()
