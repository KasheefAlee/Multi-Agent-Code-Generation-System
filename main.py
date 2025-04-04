import gradio as gr
import os
import code_generator
import code_debugger
import code_optimizer
import code_doc_generator
import traceback

def generate_and_process_code(prompt, api_key):
    try:
        generated_code = code_generator.generate_code(prompt, api_key)
        if generated_code:
            debugged_code = code_debugger.debug_code(generated_code, prompt, api_key)
            if debugged_code:
                optimized_code = code_optimizer.optimize_code(debugged_code, api_key)
                if optimized_code:
                    documentation = code_doc_generator.generate_docs(optimized_code, api_key)
                    if documentation:
                        return generated_code, debugged_code, optimized_code, documentation, "Code generation, debugging, optimization, and documentation successful."
                    else:
                        return generated_code, debugged_code, optimized_code, "Documentation generation failed. Check API or code.", "Documentation Error"
                else:
                    return generated_code, debugged_code, "Optimization failed. Check API or code.", "", "Optimization Error"
            else:
                return generated_code, "Debugging failed. Check API or code.", "", "", "Debugging Error"
        else:
            return "Code generation failed. Check API or prompt.", "", "", "", "Code Generation Error"
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}\n{traceback.format_exc()}"
        return error_message, "", "", "", error_message

def gradio_interface(prompt, api_key):
    return generate_and_process_code(prompt, api_key)

if __name__ == "__main__":
    with gr.Blocks() as demo:
        gr.Markdown("# Multi-Agent Code Generator")
        gr.Markdown("Enter a coding request and your OpenAI API key. The agents will generate, debug, optimize, and document the code.")

        with gr.Row():
            prompt_input = gr.Textbox(lines=3, placeholder="Enter your coding request...", label="Coding Request")
            api_key_input = gr.Textbox(lines=1, placeholder="Enter your OpenAI API Key...", type="password", label="OpenAI API Key")

        generate_button = gr.Button("Generate and Process Code")

        with gr.Tabs():
            with gr.Tab("Generated Code"):
                generated_code_output = gr.Code(label="Generated Code")
            with gr.Tab("Debugged Code"):
                debugged_code_output = gr.Code(label="Debugged Code")
            with gr.Tab("Optimized Code"):
                optimized_code_output = gr.Code(label="Optimized Code")
            with gr.Tab("Documentation"):
                documentation_output = gr.Code(label="Documentation")
            with gr.Tab("Error/Status"):
                error_output = gr.Textbox(label="Error/Status Messages")

        generate_button.click(
            fn=gradio_interface,
            inputs=[prompt_input, api_key_input],
            outputs=[generated_code_output, debugged_code_output, optimized_code_output, documentation_output, error_output],
        )

    demo.launch()
