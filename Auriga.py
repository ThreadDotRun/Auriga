import sublime
import sublime_plugin
import traceback
import os
from .llamacpp.LLama import Llama
import re

class TextChangeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			# Call the method to alter text
			self.alter_text(edit)
		except Exception as e:
			print("[Timmy Plugin] Error in TextChangeCommand: {}".format(str(e)))
			print("[Timmy Plugin] Traceback: {}".format(traceback.format_exc()))

	def alter_text(self, edit):
		try:
			# Ensure the view has content
			if self.view.size() > 0:
				# Get the cursor position (first selection, assuming single cursor)
				cursor_position = self.view.sel()[0].begin() if self.view.sel() else -1

				if cursor_position > 0:  # Ensure the cursor is not at the start of the file
					# Find the word region before the cursor
					word_region = self.view.word(cursor_position - 1) 
					word_text = self.view.substr(word_region)
					text_up_to_cursor = self.view.substr(sublime.Region(0, cursor_position))
					
					# Log the word text for debugging
					print("[Timmy Plugin] Word text: {}".format(text_up_to_cursor))

					# Model folder and selected model (replace with your actual paths)
					model_folder = "/media/tdrsvr/a2c28d32-eac8-4438-b371-ce4a345bbf6d/llama/llama.cpp/models/xtra_models/"
					selected_model = "neural-chat-7b-v3-3.Q8_0.gguf"
					
					# Simulated llama interaction (replace this block with your Llama API call)
					response = self.simulate_llama_response(text_up_to_cursor, model_folder, selected_model)
					cleaned_response = self.strip_ansi_codes(response)
					
					# Log the response
					print("[Timmy Plugin] Llama Response: {}".format(response))

					# Append the response to the end of the current line
					line_region = self.view.line(cursor_position)  # Get the current line region
					#self.view.insert(edit, line_region.end(), " " + response)  # Append the response
					# Replace the entire document with the response
					self.view.replace(edit, sublime.Region(0, self.view.size()), cleaned_response)  # Replace document text
		except Exception as e:
			print("[Timmy Plugin] Error in alter_text: {}".format(str(e)))
			print("[Timmy Plugin] Traceback: {}".format(traceback.format_exc()))
		finally:
			# Ensure the flag is cleared after modification
			self.view.settings().erase("is_modifying")

	def simulate_llama_response(self, word_text, model_folder, selected_model):
		context_size = "1000"
		selected_ctls = "1000"
		num_token = "100"
		temp = "1.0"
		
		# For demonstration purposes, we mimic a Llama response
		llama = Llama(model_folder + "//" + selected_model)
		response = llama.run_llama(word_text, context_size=selected_ctls, batch_size=selected_ctls, num_tokens=num_token, temp=temp)
		
		return response
	def strip_ansi_codes(self, text):
		"""
		Removes ANSI escape sequences from the given text.
		"""
		ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
		return ansi_escape.sub('', text)
