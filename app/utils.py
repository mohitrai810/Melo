import subprocess

def synthesize(text: str, output_path: str):
    subprocess.run(["melotts", text, output_path], check=True)
