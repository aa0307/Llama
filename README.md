Here are the step to install and use this Ollma pdf reader:
1. Install Ollma from website https://ollama.com/
2. Download and install python (recommand 3.12)
3. (Optional) Create venv (virtural environment) to run the package install
4. (Optional) venv create steps:# Go to path # cd D:\GitHub\Llama # create venv # python # Activate venv # D:\GitHub\Llama\Llama\Scripts\Activate.ps1
5. Package install (type: pip install langchain langchain-community pypdf docarray) in terminal
6. Install AI model by command: ollama pull QwQ (in terminal)
7. Install AI embedding by command: ollama pull znbang/bge:small-en-v1.5-f32 (in terminal)
8. Change the path of variable llm, embeddings and loader to your AI model, embedding and file locations.
