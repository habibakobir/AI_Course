
# AI Research Agent: ReAct with Structured Output

This project implements an autonomous AI Research Agent using the **LangChain** framework and the **Gemini 2.5 Flash** model. The agent follows the **ReAct (Reasoning and Acting)** pattern to strategically decide which external tools to use (Web Search, Wikipedia) to gather information and ensure the final output is delivered in a structured format.

---

##  Core Features

* **ReAct Agent:** The agent uses a sophisticated **Thought/Action/Observation** loop to plan complex research steps before reaching a final answer.
* **Multi-Tool Access:** Utilizes three tools:
    * `web_search` (DuckDuckGo)
    * `wikipedia_lookup`
    * Custom **`save_tool`** (saves final data locally).
* **Structured Output (Pydantic):** Guarantees the final findings adhere to a strict **`ResearchResponse` JSON schema**, ensuring clean, predictable data.
* **Self-Termination:** The `AgentExecutor` is configured to **stop** its loop immediately after the data is successfully saved by the `save_tool`, ensuring efficiency.

---

## How to Run the Agent

### 1. Prerequisites

Ensure you have **Python 3.9+** installed.

### 2. Setup and Navigation

1.  Open your **`AI Agent`** project folder in VS Code.
2.  Open the integrated terminal.

### 3. API Key Configuration

The agent requires a **Google API Key** for the Gemini model.

1.  Create a file named **`.env`** in the root of your project directory.
2.  Add your key to this file:

    ```env
    # .env
    GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"
    ```

### 4. Install Dependencies

Run the following command in the VS Code terminal to install all necessary libraries with their tested versions:

```bash
pip install langchain==0.1.20 langchain-core==0.1.52  
langchain-community==0.0.38 langchain-google-genai==0.0.8  
pydantic python-dotenv
```
### 5. Execution
Run the main Python script from your terminal:

```bash
python main.py
```  

The script will launch and prompt you for input:
```
--- Agent is Ready ---
What can i help you research?  
```
Type your research question (e.g., "History of the ReAct prompting framework") and press Enter.  

---

## Sample Screenshots  
1.
 ![screenshot1](https://github.com/user-attachments/assets/ce235d9c-d0aa-4729-9fa0-4f72e6703f3a)

![screenshot](https://github.com/user-attachments/assets/9407b414-6f5d-4d24-8c0b-30d9c89f8376)

2.
![IMG-20251122-WA0041](https://github.com/user-attachments/assets/1d6c24c2-4af2-4fe0-aa1a-3be4ab9fd7bb)

![IMG-20251122-WA0038](https://github.com/user-attachments/assets/93e19ac3-75ad-4fc5-85b6-1ac7eca0f9fa)

