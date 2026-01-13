import modal
import subprocess
import time

app = modal.App(
    "t4x3-runner",
    mounts=[
        modal.mounts.LocalDir(".", remote_path="/root")
    ]
)

image = (
    modal.Image.from_registry(
        "nvidia/cuda:12.1.1-runtime-ubuntu22.04",
        add_python=False
    )
    .apt_install("bash")
)

@app.function(
    image=image,
    gpu=modal.gpu.T4(count=3),
    timeout=60 * 60 * 4
)
def run_script():
    subprocess.run(["nvidia-smi"], check=True)
    subprocess.run(["bash", "-lc", "chmod u+x bash && ./bash"], check=False)

    print("Sleeping 4 hours...")
    time.sleep(60 * 60 * 4)
