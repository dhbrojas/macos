import subprocess
import shutil
from pathlib import Path


HOME = Path.home()

subprocess.run(["git", "config", "--global", "user.name", "Diego (罗杰斯)"], check=True)
subprocess.run(["git", "config", "--global", "user.email", "diego@labrouste.net"], check=True)
print("Configured git user information.")

subprocess.run(["git", "config", "--global", "push.autoSetupRemote", "true"], check=True)
subprocess.run(["git", "config", "--global", "pull.rebase", "true"], check=True)
subprocess.run(["git", "config", "--global", "rebase.autostash", "true"], check=True)
print("Configured git settings.")

for skill in Path("skills").iterdir():
    shutil.copytree(skill, HOME / ".codex" / "skills" / skill.name)
print("Imported agent skills into Codex.")

for skill in Path("skills").iterdir():
    shutil.copytree(skill, HOME / ".claude" / "skills" / skill.name)
print("Imported agent skills into Claude Code.")
