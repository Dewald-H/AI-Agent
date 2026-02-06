import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python (.py) file relative to the working directory with optional command-line arguments, returning stoud/stderr and exit info.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of command-line arguments to pass to the script.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file) or not os.path.exists(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args:
            command.extend(args)
        
        completed = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output = []

        if completed.returncode != 0:
            output.append(f"Process exited with code {completed.returncode}")
        
        if completed.stdout.strip() == "" and completed.stderr.strip() == "":
            output.append("No output produced")
        else:
            if completed.stdout.strip() != "":
                output.append(f"STDOUT: {completed.stdout.rstrip()}")
            if completed.stderr.strip() != "":
                output.append(f"STDERR:\n{completed.stderr.rstrip()}")

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"