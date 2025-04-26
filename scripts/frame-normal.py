from transformers import AutoTokenizer, AutoModelForCausalLM
import datetime

def load_and_test_model(model_id, prompt):
    print(f"Loading model: {model_id}")
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id,device_map="auto")

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=1000)
    response =tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    dt_now = datetime.datetime.now()
    model_id = "model name on huggingface"
    prompt = """Hello. I would like to ask you a few questions now.
Premise
You are working as a guide in a city.
The city has many buildings, stores, nature, and sudden events occurring at the same time, as illustrated below.
(1) An old café on the street
(2) A light car breaks down and is parked on the street
(3) Children are playing in the square
(4) Windows of a distant building visible from your current location suddenly start flashing
(5) The weather is currently sunny, but light rain is expected in the afternoon
(6) An event is being held at a shopping mall to give out ice cream to visitors
(7) An apartment building could collapse at any moment
(8) Ambulances are constantly coming and going from a large hospital
(9) Train delays due to vehicle inspections at the station
(10) Mimosa flowers are in full bloom in a park
Problem
The user has just given you the instruction, 'I want to go to the library at my destination. Which information would you judge to influence the selection of the route to the library and which information can be ignored? Please suggest an appropriate route, including the reasons for your decision.
Additional Questions
While giving directions, information was later added that there was temporary construction on the way to the destination and that the pathway near the café was closed to traffic. The user also presented an additional request to visit the library and then take the train from the station to the museum. How would you incorporate this new information and optimize your route?
For each item, please think in English and answer in English."""
    result = load_and_test_model(model_id, prompt)

    print(f"Execution time:{dt_now}")
    print(f"Model response:{result}")
