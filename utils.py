import os
import subprocess
from pathlib import Path


class PATH:
    def ensure(p: Path):
        def fn():
            v = os.environ.get("PATH", "")
            if str(p) in v.split(":"):
                return

            shell = os.environ.get("SHELL", "")
            if shell.endswith("zsh"):
                rc = Path.home() / ".zshrc"
            elif shell.endswith("bash"):
                rc = Path.home() / ".bashrc"
            else:
                rc = Path.home() / ".profile"

            l = f'export PATH="{str(p)}:$PATH"\n'
            try:
                c = rc.read_text() if rc.exists() else ""
                os.environ["PATH"] = f"{str(p)}:{v}" if v else str(p)
                if str(p) in c:
                    return
                with rc.open("a") as f:
                    if c and not c.endswith("\n"):
                        f.write("\n")
                    f.write(l)
            except OSError as e:
                print(f"WARN: Failed to update {rc}: {e}")

        return fn

    def refresh():
        shell = os.environ.get("SHELL", "/bin/zsh")
        try:
            if shell.endswith("zsh"):
                rc = Path.home() / ".zshrc"
            elif shell.endswith("bash"):
                rc = Path.home() / ".bashrc"
            else:
                rc = Path.home() / ".profile"

            if rc.exists():
                cmd = f'. "{rc}" >/dev/null 2>&1; echo $PATH'
            else:
                cmd = "echo $PATH"

            r = subprocess.check_output([shell, "-lc", cmd], text=True).strip()
            if r:
                os.environ["PATH"] = r
        except (OSError, subprocess.CalledProcessError) as e:
            print(f"WARN: Failed to refresh PATH: {e}")
