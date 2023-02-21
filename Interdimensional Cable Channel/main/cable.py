import openai

openai.api_key = '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'


class Cable:

    def generate(self, situation):
    # Set the model and prompt
        model_engine = "text-davinci-003"
        prompt = "Generate a script for a TV show where " + situation + "."
        print(prompt)
        #Set the maximum number of tokens to generate in the response
        max_tokens = 1024

        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        #Print the response
        print(completion.choices[0].text)