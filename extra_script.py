import os
import re

env = DefaultEnvironment()

def get_cpu():
    flags = str(env.get("CCFLAGS", []))
    m = re.search(r"-mcpu=([^\s]+)", flags)
    return m.group(1) if m else None

cpu = get_cpu()

if cpu is None:
    cpu = env.BoardConfig().get("build.mcu", "")

arch = ""

if cpu == "cortex-m4":
    arch = "cortex-m4f"
elif cpu == "esp32" or cpu == "esp32s2" or cpu == "esp32s3":
    arch = "xtensa-esp32"
elif cpu == "esp32c3" or cpu == "esp32c6":
    arch = "riscv32"

if arch == "":
    print("Unknown architecture")
    return None

env.Append(
    LIBPATH=[os.path.realpath("lib/{}/".format(arch))],
    LIBS=["pinyin_simple_backend"]
)
