import subprocess


subprocess.run(["git", "config", "--global", "user.name", "Diego (罗杰斯)"], check=True)
subprocess.run(["git", "config", "--global", "user.email", "noreply@labrouste.net"], check=True)
print("Configured git user information.")
