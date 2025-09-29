💬 Custom GPT-2 Chatbot Project
This project implements a customizable language model (GPT-2) based chatbot application using the Hugging Face transformers library. The model is optimized for a specific persona or task through fine-tuning on a custom conversation dataset (data/custom_chat_data.json). It leverages PyTorch for GPU-accelerated training and generation, ensuring real-time response capabilities within a console environment. The architecture utilizes a hybrid approach, where specialized services (JokeManager, PoemDatabase) abstract complex tasks, offering potential integration with external LLM APIs (e.g., Gemini) for enhanced creative output.

⚙️ Technical Architecture and Structure
The project follows a modular structure for clean coding practices:

models/fine_tuning_scripts.py: Manages the Model Fine-Tuning process. It automates training using the Hugging Face Trainer class.

src/chat_bot.py: Contains the core bot logic, including model loading, conversation context management, and text generation (GenerationConfig).

src/jokemanager.py / src/poem_database.py: These modules serve as abstraction layers for special, rule-based functionalities (joke flow management, poem selection/generation) that extend the core capabilities of the fine-tuned LLM.

demo.py: The Console Line Interface (CLI) for user interaction.

🚀 Setup
Prerequisites
Python 3.8+

GPU (Highly recommended for Fine-Tuning)

Project Installation
Install the necessary Python libraries using the requirements.txt file:

# Install dependencies
pip install -r requirements.txt

📦 Data and Model Preparation
Dataset: Create the JSON file required for fine-tuning.

// data/custom_chat_data.json format
[
  {
    "conversations": [
      {"from": "human", "value": "Hello, how are you?"},
      {"from": "gpt", "value": "I'm doing well, thank you. How about you?"}
    ]
  },
  // ... more conversations
]

Pre-trained Model: Ensure the models/checkpoint-420 directory contains either the fine-tuned model or a base GPT-2 model for initial training.

🛠️ Fine-Tuning
To train the model with your custom dataset:

python -c "from models.fine_tuning_scripts import start_fine_tuning; start_fine_tuning()"

Adjust the TrainingArguments (number of epochs, batch size, etc.) and GenerationConfig (temperature, top-p, max-new-tokens) parameters within models/fine_tuning_scripts.py according to your project needs.

🧠 Advanced Configuration and Integration
1. Optimizing Fine-Tuning Parameters
The success of fine-tuning relies heavily on adjusting the following parameters in models/fine_tuning_scripts.py and src/chat_bot.py:

Parameter

Location

Description

Optimization Strategy

num_train_epochs

TrainingArguments

Number of passes over the entire dataset.

Increase for smaller datasets, decrease to avoid overfitting on larger, high-quality data.

per_device_train_batch_size

TrainingArguments

The batch size per device (GPU/CPU).

Use the largest size your GPU memory allows for faster training and better gradient stability.

learning_rate

TrainingArguments

The step size for gradient descent.

Start low (e.g., 5e-5). Too high can cause the model to diverge.

temperature

GenerationConfig

Controls randomness. Lower = more deterministic/safe.

Use lower values (0.5-0.8) for factual tasks; higher values (0.8-1.0) for creative writing.

top_p / top_k

GenerationConfig

Sampling strategies (Nucleus / Top-K sampling).

Adjust these to control the diversity of the output vocabulary. High top_p (e.g., 0.95) allows for more diverse, high-probability words.

repetition_penalty

GenerationConfig

Reduces the likelihood of the model repeating tokens.

Critical for chat models. Increase (e.g., 1.2) to prevent the bot from getting stuck in loops.

2. LLM API Integration (Hybrid Approach)
For complex or knowledge-intensive tasks, you can leverage an external, more powerful LLM API (like Google's Gemini API) while keeping the main conversational flow on the local, cost-effective GPT-2 model.

The Service Layer Pattern implemented by JokeManager and PoemDatabase enables this hybrid approach:

src/jokemanager.py: Instead of returning hardcoded joke strings, this module can be updated to make an asynchronous API call to an external LLM with the prompt: “Tell a short, funny knock-knock joke.”

src/poem_database.py: This can be refactored to use the external API for creative generation, prompting: “Write a 4-line sonnet about the user's input: [USER_INPUT]”.

This design allows the core src/chat_bot.py to remain clean, delegating specific high-demand tasks to specialized external services.

▶️ Usage
Start the chatbot using the fine-tuned model:

python demo.py

The bot's special commands are:

poem or write a poem: Triggers a response from the Poem Database/Service.

joke or tell me a joke: Initiates the joke flow (the bot waits for the user to respond with 'why').

📜 Core Dependencies
requirements.txt
The core Python libraries used in this project are:

transformers: For model loading, tokenization, and fine-tuning.

torch: The computation engine (essential for GPU utilization).

datasets: For loading and processing the dataset.

scikit-learn: (Optional, may be used for classification tasks like poem type detection in poem_database.py).
