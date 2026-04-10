from transformers import pipeline

class TextGenerator:
    def __init__(self, model_name="gpt2"):
        self.generator = pipeline("text-generation", model=model_name)

    def generate_text(self, prompt, max_length=100, temperature=0.7):
        output = self.generator(
            prompt,
            max_length=max_length,
            temperature=temperature,
            num_return_sequences=1
        )
        return output[0]['generated_text']
