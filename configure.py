import subprocess


subprocess.run(["git", "config", "--global", "user.name", "Diego (罗杰斯)"], check=True)
subprocess.run(["git", "config", "--global", "user.email", "diego@labrouste.net"], check=True)
print("Configured git user information.")

subprocess.run(["git", "config", "--global", "push.autoSetupRemote", "true"], check=True)
subprocess.run(["git", "config", "--global", "pull.rebase", "true"], check=True)
subprocess.run(["git", "config", "--global", "stash.autoStash", "true"], check=True)
print("Configured git settings.")
