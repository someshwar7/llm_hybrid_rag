import subprocess

def query_codelama(user_input):
    try:
        result = subprocess.run(
            ["ollama", "run", "codellama", user_input],
            capture_output=True, text=True, check=True, encoding='utf-8', errors='replace'
        )
        return f"[CodeLLaMA]\n{result.stdout.strip()}"
    except subprocess.CalledProcessError as e:
        return f"[CodeLLaMA Error] {e.stderr.strip()}"
