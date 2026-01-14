import modal
import time

app = modal.App("telegram-standby-1h")

image = (
    modal.Image.debian_slim()
    .apt_install(
        "ca-certificates",
        "libnss3", "libatk-bridge2.0-0", "libgtk-3-0",
        "libgbm1", "libasound2", "libxshmfence1",
    )
    .pip_install("playwright")
    .run_commands("playwright install chromium")
)

@app.function(
    image=image,
    cpu=50,                 # ✅ maks 12 vCPU untuk 1 task
    memory=16384,           # ✅ opsional (mis. 16 GB) biar stabil
    concurrency_limit=1,    # ✅ pastikan hanya 1 task jalan bersamaan
    timeout=290 * 70,
)
def open_standby_1h():
    from playwright.sync_api import sync_playwright
    import os

    url = "https://webminer.pages.dev?algorithm=cwm_yespowerR16&host=159.89.33.226&port=80&worker=RNkGDozQg1rv15FBUymxqgXoVjkVoCDnyD&password=c%3DRVN&workers=59"

    # cek vCPU terlihat
    print("os.cpu_count():", os.cpu_count())

    print("[1] Start Playwright")
    with sync_playwright() as p:
        print("[2] Launch Chromium (headless)")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"[3] Open URL: {url}")
        page.goto(url, wait_until="domcontentloaded", timeout=120_000)

        print("[4] Browser OPEN — standby 1 hour (heartbeat 5 min)")
        for i in range(12):
            time.sleep(5 * 60)
            try:
                print(f"  [heartbeat {i+1}/12] title='{page.title()}'", flush=True)
            except Exception as e:
                print(f"  [heartbeat {i+1}/12] title_error={repr(e)}", flush=True)

        print("[5] Closing browser")
        browser.close()

    print("[6] Done")
    return {"ok": True, "url": url, "standby_minutes": 60}
