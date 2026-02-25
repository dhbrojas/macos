import os
import shutil
import subprocess
import sys
import time
from abc import ABC, abstractmethod
from pathlib import Path

from utils import PATH


class Item(ABC):
    def __init__(self, name, hooks = None):
        self.name = name
        self.hooks = hooks or []

    @abstractmethod
    def is_installed(self) -> bool:
        return False

    @abstractmethod
    def install(self): ...


class BrewPackage(Item):
    def __init__(self, name, slug, *, version = None, cask = False, hooks = None):
        super().__init__(name, hooks)
        self.slug = slug
        self.version = version
        self.cask = cask

    def is_installed(self):
        if self.cask:
            command = f"brew list --cask {self.slug}"
        else:
            command = f"brew list {self.slug}"
        try:
            subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            return True
        except subprocess.CalledProcessError:
            return False

    def install(self):
        if self.cask:
            command = f"brew install --cask {self.slug}"
        else:
            command = f"brew install {self.slug}"
        subprocess.run(command, shell=True, check=True)


class PipeBashCommand(Item):
    def __init__(
        self,
        name,
        command,
        interactive = False,
        which = None,
        stat = None,
        hooks = None
    ):
        super().__init__(name, hooks)
        self.command = command
        self.interactive = interactive
        self.which = which
        self.stat = stat

    def is_installed(self) -> bool:
        if self.which:
            return shutil.which(self.which) is not None
        elif self.stat:
            return os.path.exists(self.stat.replace("~", str(Path.home())))
        else:
            return False

    def install(self):
        subprocess.run(self.command, shell=True, check=True)


items = [
    PipeBashCommand(
        "Homebrew", "curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh | sh", which="brew"
    ),
    PipeBashCommand(
        "Oh My ZSH",
        "curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | sh",
        stat="~/.oh-my-zsh",
    ),
    BrewPackage("Ghostty", "ghostty", cask=True),
    BrewPackage("Spotify", "spotify", cask=True),
    BrewPackage("Feishu", "feishu", cask=True),
    BrewPackage("Docker", "docker", cask=True),
    BrewPackage("WeChat", "wechat", cask=True),
    BrewPackage("Slack", "slack", cask=True),
    BrewPackage("Discord", "discord", cask=True),
    BrewPackage("Cursor", "cursor", cask=True),
    BrewPackage("Wispr Flow", "wispr-flow", cask=True),
    BrewPackage("Logitech Options", "logi-options+", cask=True),
    BrewPackage("Golang", "go"),
    BrewPackage("Infisical", "infisical/get-cli/infisical"),
    BrewPackage("UV", "uv"),
    PipeBashCommand(
        "Rust", "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh", interactive=True, which="cargo"
    ),
    PipeBashCommand(
        "Claude Code",
        "curl -fsSL https://claude.ai/install.sh | sh",
        interactive=True,
        which="claude",
        hooks=[PATH.ensure(Path.home() / ".local" / "bin")],
    ),
    PipeBashCommand("Bun", "curl -fsSL https://bun.com/install | sh", interactive=True, which="bun"),
]

PATH.refresh()

for item in items:
    if len(sys.argv) > 1:
        if item.name not in sys.argv[1:] and item.name.replace(" ", "-").lower() not in sys.argv[1:]:
            print(f"Skipping {item.name}...")
            continue

    if item.is_installed():
        print(f"Target '{item.name}' is already installed.")
        continue
    else:
        try:
            s = time.time()
            item.install()
            [hook() for hook in item.hooks]
            print(f"Target '{item.name}' installed in {time.time() - s:.2f}s.")
            PATH.refresh()
        except subprocess.CalledProcessError as e:
            print(f"ERR! Failed to install {item.name}: {e}")
