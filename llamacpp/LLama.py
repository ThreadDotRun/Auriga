import subprocess
import os
import time

class Llama:
    def __init__(self, model):
        self.model = model

    def prompt(self, prompt):
	    print("{}: ".format(prompt))
	    return input()


    def run_llama(self, user_prompt
                  , context_size='2048'
                  , batch_size='8'
                  , num_tokens='1024'
                  , temperature='0.8'
                  , keep='75'
                  , repeat_penalty='1.1'
                  , color=True
                  , temp=.08):
        # Read password from a file        
            
        response = []
        command = ['/media/tdrsvr/a2c28d32-eac8-4438-b371-ce4a345bbf6d/llama/llama.cpp/main', '-m', self.model, '-c', context_size, '-b', batch_size, '-n', num_tokens,
                   '--keep', keep, '--repeat_penalty', repeat_penalty, '--no-penalize-nl', '--mirostat-lr', "0.1",
                  "--temp", "0.15", "--tfs", "0.95", "--mirostat-ent", "4.0"]        
        print("")
        print("command = {}: ".format(command))
        if color:
            command.append('--color')

        command += ['-p', user_prompt]

        try:
            with subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as proc:
                for line in proc.stdout:
                    #print(f"Line: {line}", end='')
                    # Escape HTML special characters and replace newlines with <br> tags
                    #escaped_line = line.replace('\n', '<br>')
                    response.append(line)
                    time.sleep(5)
                    #command_clear_buffers = "sh -c 'sync; echo 3 > /proc/sys/vm/drop_caches'"
                    #full_command = f"echo {password} | sudo -S {command_clear_buffers}"
                    #result = subprocess.run(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    #print(f"Result {result}")
        except subprocess.SubprocessError as e:
            print("n error occurred: {}".format(e))
            response = ["Error processing the request."]
        return ''.join(response)

    def save_output(self, prompt, output):
        safe_prompt = prompt.replace(' ', '_')
        filename = "{}.txt".format(safe_prompt)
        with open(filename, 'w') as f:
            f.write(output)