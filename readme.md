# Auriga Fully Open Source Code and Text Completion Plugin for Sublime Text
## Using llama.cpp binaries (to keep it small so it runs almost anywhere with no network connections needed)
### Demo runs on a Dell optiplex built circa 2016
- A Sublime Text plugin that integrates a machine learning model for real-time text generation and completion using fully open source components and GGUF (Generic Graph Universal Format) model files.

# TLDR
- Auriga.py goes in the Sublime Text package folder in another folder (Auriga works)
- The llamacpp folder (in this project, not the llama.cpp binaries) also goes in this folder so that the plugin (Auriga) can find and import it
	- See (Set the path for your llama.cpp binaries locally like referenced in Llama.py:) below for where to put the llama.cpp binaries and the linked project to get them.
- Use the Sublimetext menu Preferences->Key Bindings and add the code in the pic included in pics for your shortcut key
- Make sure you have Python 3.10 (tested) or better installed on as your system python 
- Tested under Ubuntu 24
- Restart Sublime Text after installation to activate the plugin.
- Use your keyboard shortcut to do code or text completion in the open editor window.
- Use ctrl-` to watch output in the console.
- The model used here can be found at https://huggingface.co/TheBloke/neural-chat-7B-v3-3-GGUF

## Features
- Real-time text generation using GGUF models
- Context-aware completions based on cursor position
- Support for custom Llama model configurations
- ANSI code stripping for clean output
## Prerequisites
- Sublime Text 4
- Python 3.x (tested using 3.10)
- llama.cpp installed and configured (supply path in LLama.py line 26)
- Sufficient disk space for Llama models
## Installation
- ```Clone this repository to your Sublime Text packages directory:```
- ```cd ~/.config/sublime-text/Packages ## Linux```
## Clone the repository:
- ```git clone https://github.com/ThreadDotRun/Auriga.git```
## Configuration
- Set up your model path in the plugin code:
- model_folder = "/path/to/your/llama/models/"
- selected_model = "your-model-name.gguf"
## Set the path for your llama.cpp binaries locally like referenced in Llama.py:
- ```command = ['/media/tdrsvr/a2c28d32-eac8-4438-b371-ce4a345bbf6d/llama/llama.cpp/main', '-m', self.model, '-c', context_size, '-b', batch_size, '-n', num_tokens,'--keep', keep, '--repeat_penalty',repeat_penalty, '--no-penalize-nl', '--mirostat-lr', "0.1","--temp", "0.15", "--tfs", "0.95", "--mirostat-ent", "4.0"]```
- Download here https://github.com/ggerganov/llama.cpp
## Configure model parameters (optional):
- In LLama.py these are used as such : response = llama.run_llama(user_input, context_size=f'{selected_ctls}', batch_size=f'{selected_ctls}', num_tokens=f'{num_token}', temp=f'{temps}')
- context_size = "1000" 
- selected_ctls = "1000" 
- num_token = "100"
- temp = "1.0"
## Usage
- Open a text file in Sublime Text
- Type your text or code in a editor window
- Press the configured shortcut key (default: [I used ctrl-shift-c in this example is the Sublime user setting (pics included)])
- The plugin will generate text based on the context before the cursor
## Model Compatibility
- Supports GGUF format models
- Tested with:
- neural-chat-7b-v3-3.Q8_0.gguf
## Known Issues
- Large models may cause performance impact
- Initial loading time may vary based on model size
## Contributing
- Fork the repository
- Create your feature branch (git checkout -b feature/amazing-feature)
- Commit your changes (git commit -m 'Add amazing feature')
- Push to the branch (git push origin feature/amazing-feature)
- Open a Pull Request
## License
[Apache 2.0]
- Acknowledgments
- llama.cpp project
- Sublime Text community
## Other acknowledgments]
- [Caffeine and Nicotine]
