def topic(client, input):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Is the user talking about housing preference or lease tutorials? If housing preference, return 0. Otherwise, return 1. This is user input: " + input,
    )
    generated_text = response.choices[0].text.strip()
    print(generated_text)
    return generated_text

