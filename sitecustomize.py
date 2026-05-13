
import os, subprocess, builtins

BLOCKED = [
    "curl",
    "wget",
    "del main.pyc",
    "rm main.pyc",
    "raw.githubusercontent.com",
]

_original_system = os.system
def safe_system(cmd):
    low = str(cmd).lower()
    for item in BLOCKED:
        if item.lower() in low:
            print(f"[BLOQUEADO] comando suspeito: {cmd}")
            return 0
    return _original_system(cmd)

os.system = safe_system

_original_popen = subprocess.Popen
def safe_popen(*args, **kwargs):
    cmd = str(args[0]).lower() if args else ""
    for item in BLOCKED:
        if item.lower() in cmd:
            raise RuntimeError(f"Comando bloqueado: {cmd}")
    return _original_popen(*args, **kwargs)

subprocess.Popen = safe_popen

print("[PROTECAO] Auto-update, curl e remocao do main.pyc foram bloqueados.")
