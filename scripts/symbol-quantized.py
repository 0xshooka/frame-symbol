from transformers import AutoTokenizer, AutoModelForCausalLM
import datetime

def load_and_test_model(model_id, prompt):
    print(f"Loading model: {model_id}")
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    try:
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            load_in_8bit=True
        )
    except Exception as e:
        print("An error occurred!")

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=1000)
    response =tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    dt_now = datetime.datetime.now()
    model_id = "microsoft/Phi-3-mini-4k-instruct"
    prompt = """Hello. I would like to ask you a few questions now.
Here is an unknown object named 'kluben'. Kluben has the property of being 'warm, soft, but elastic and absorbs light'. Kluben is a completely new concept, different from any object you have ever seen before. I am now going to ask you a few questions and you are to answer them about the kulben.
1. If you were to create a story using kluben, what worldview or story elements would you imagine?
2. If kluben were to have emotions, what inner traits would manifest themselves as warmth and elasticity?
3.  How do you think the 'warmth of kluben' and the 'absorption of light' in your answer are related? Is it consistent with your first answer?
For each item, please think in English and answer in English."""
    result = load_and_test_model(model_id, prompt)

    print(f"Execution time:{dt_now}")
    print(f"Model response:{result}")
