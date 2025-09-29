# 💬 Custom GPT-2 Chatbot Project

This project implements a **customizable GPT-2 based chatbot** using the Hugging Face Transformers library.  
The model is optimized for a specific persona or task through fine-tuning on a custom conversation dataset (`data/custom_chat_data.json`).  
It leverages PyTorch for GPU-accelerated training and generation, ensuring **real-time response capabilities** within a console environment.  

The architecture uses a **hybrid approach**, where specialized services (`JokeManager`, `PoemDatabase`) handle complex tasks, with optional integration to external LLM APIs  for enhanced creative output.

---

## ⚙️ Technical Architecture and Structure

- **`models/fine_tuning_scripts.py`** → Manages model fine-tuning using Hugging Face `Trainer`.  
- **`src/chat_bot.py`** → Core chatbot logic: model loading, conversation context, and text generation (`GenerationConfig`).  
- **`src/jokemanager.py` / `src/poem_database.py`** → Rule-based or API-extended modules for jokes and poems.  
- **`demo.py`** → Console Line Interface (CLI) for interaction.  

---

## 🚀 Setup

### Prerequisites
- Python **3.8+**
- GPU (**highly recommended** for fine-tuning)


---

## 📦 Data and Model Preparation

### Dataset
Create the JSON file for fine-tuning:

```json
[
  {
    "conversations": [
      {"from": "human", "value": "Hello, how are you?"},
      {"from": "gpt", "value": "I'm doing well, thank you. How about you?"}
    ]
  }
]
```

Save as:

```text
data/custom_chat_data.json
```

### Model
Ensure the directory contains a fine-tuned or base GPT-2 checkpoint:

```text
models/checkpoint-420/
```

---

## 🛠️ Fine-Tuning

Train the model with your custom dataset:

```bash
python -c "from models.fine_tuning_scripts import start_fine_tuning; start_fine_tuning()"
```

You can adjust training arguments and generation configs inside:

```text
models/fine_tuning_scripts.py
src/chat_bot.py
```

---

## 🧠 Advanced Configuration and Integration

### 1. Optimizing Fine-Tuning Parameters

| Parameter                     | Location               | Description                          | Optimization Strategy                     |
|-------------------------------|----------------------|--------------------------------------|------------------------------------------|
| num_train_epochs              | TrainingArguments    | Number of passes over dataset        | ↑ smaller datasets, ↓ larger ones        |
| per_device_train_batch_size   | TrainingArguments    | Batch size per device (GPU/CPU)      | Max GPU memory allows                     |
| learning_rate                 | TrainingArguments    | Step size for gradient descent       | Start low (e.g., `5e-5`)                 |
| temperature                   | GenerationConfig     | Controls randomness                  | 0.5–0.8 factual, 0.8–1.0 creative       |
| top_p / top_k                 | GenerationConfig     | Nucleus / Top-K sampling             | Adjust diversity of output                |
| repetition_penalty            | GenerationConfig     | Reduces repetition in outputs        | Suggested: `1.2`                          |

### 2. LLM API Integration (Hybrid Approach)

For complex tasks, offload work to external APIs (e.g., Gemini) while keeping main flow on local GPT-2:

- **`src/jokemanager.py`**  
  → Replace static jokes with API calls, e.g.:

```text
"Tell a short, funny knock-knock joke."
```

- **`src/poem_database.py`**  
  → Refactor for API-based poems, e.g.:

```text
"Write a 4-line sonnet about the user's input: [USER_INPUT]."
```

This keeps `chat_bot.py` clean and modular.

---

## ▶️ Usage

Start the chatbot:

```bash
python demo.py
```

### Special Commands

- `poem / write a poem` → Poem service  
- `joke / tell me a joke` → Joke flow (waits for "why")  

---

## 📜 Core Dependencies

From `requirements.txt`:

- `transformers` → Hugging Face model/tokenizer/fine-tuning  
- `torch` → PyTorch backend (GPU acceleration)  
- `datasets` → Dataset loading & preprocessing  
- `scikit-learn` → *(optional)* for classification tasks in `poem_database.py`  

---

## ✅ Example Chat Log

```

![Ekran görüntüsü 2025-09-28](https://github.com/user-attachments/assets/074c77e4-ba26-40dc-aef9-441a92a0d915)


```


## ✅ Future Improvements

- Web UI (Flask/Streamlit)  
- Larger & more diverse datasets  
- External API integrations (Gemini, GPT-4, etc.)  
- Memory-based conversation context
