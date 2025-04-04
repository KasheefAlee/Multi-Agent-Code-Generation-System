import os
import code_doc_generator
import code_generator
import code_debugger
import code_optimizer

if __name__ == "__main__":
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key is None:
        api_key = input("Enter your OpenAI API key: ")

    prompt = input("Enter your coding request: ")

    generated_code = code_generator.generate_code(prompt, api_key)

    if generated_code:
        print("\nGenerated Code:\n")
        print(generated_code)

        debugged_code = code_debugger.debug_code(generated_code, prompt, api_key)
        if debugged_code:
            print("\nDebugged Code:\n")
            print(debugged_code)

        optimized_code = code_optimizer.optimize_code(debugged_code, api_key)
        if optimized_code:
            print("\nOptimized Code:\n")
            print(optimized_code)

        documentation = code_doc_generator.generate_docs(optimized_code, api_key)
        if documentation:
            print("\nDocumentation:\n")
            print(documentation)

    else:
        print("Code generation failed.")