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
    ./bash
    """

    subprocess.run(
        ["bash", "-lc", cmds],
        check=False
    )
