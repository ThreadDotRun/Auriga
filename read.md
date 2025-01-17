Auriga Plugin for Sublime Text
A Sublime Text plugin that integrates the Llama language model for real-time text generation and completion.

* Features
- Real-time text generation using Llama models
- Context-aware completions based on cursor position
- Support for custom Llama model configurations
- ANSI code stripping for clean output
* Prerequisites
- Sublime Text 4
- Python 3.x (tested using 3.10)
- llama.cpp installed and configured (supply path in LLama.py line 26)
- Sufficient disk space for Llama models
* Installation
- Clone this repository to your Sublime Text packages directory:
- cd ~/.config/sublime-text/Packages # Linux
* Clone the repository:
- git clone https://github.com/ThreadDotRun/Auriga.git
* Configuration
- Set up your model path in the plugin code:
- model_folder = "/path/to/your/llama/models/"
- selected_model = "your-model-name.gguf"
* Configure model parameters (optional):
- In LLama.py these are used as such : response = llama.run_llama(user_input, context_size=f'{selected_ctls}', batch_size=f'{selected_ctls}', num_tokens=f'{num_token}', temp=f'{temps}')
- context_size = "1000" 
- selected_ctls = "1000" 
- num_token = "100"
- temp = "1.0"
* Usage
- Open a text file in Sublime Text
- Type your text or code in a editor window
- Press the configured shortcut key (default: [I used ctrl-shift-c in this example is the Sublime user setting (pics included)])
- The plugin will generate text based on the context before the cursor
* Model Compatibility
- Supports GGUF format models
- Tested with:
- neural-chat-7b-v3-3.Q8_0.gguf
* Known Issues
- Large models may cause performance impact
- Initial loading time may vary based on model size
* Contributing
- Fork the repository
- Create your feature branch (git checkout -b feature/amazing-feature)
- Commit your changes (git commit -m 'Add amazing feature')
- Push to the branch (git push origin feature/amazing-feature)
- Open a Pull Request
* License
[Apache 2.0]
- Acknowledgments
- llama.cpp project
- Sublime Text community
[Other acknowledgments]
- Caffeine and Nicotine
