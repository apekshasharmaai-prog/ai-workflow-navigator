import ollama


class LocalLLM:
    """
    Wrapper around Ollama.
    """

    def __init__(self, model):

        self.model = model

    def generate(self, prompt):

        response = ollama.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response["message"]["content"]