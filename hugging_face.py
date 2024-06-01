# login into hg account
from huggingface_hub import login
login()

# push a single file to the hugging face hub
from huggingface_hub import HfApi
api = HfApi()
api.upload_file(
    path_or_fileobj="/kaggle/working/mamba_python_1.pt",
    path_in_repo="mamba_python_1.pt",
    repo_id="pt-sk/mamba_python",
    repo_type="model",
)

# push entire folder to the hub
from huggingface_hub import HfApi
api = HfApi()

api.upload_folder(
    folder_path="/path/to/local/space",
    repo_id="username/my-cool-space",
    repo_type="space",
)
