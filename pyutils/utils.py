import subprocess
from typing import List
import shlex


def exec(cmd):
    ps = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    output = ps.communicate()[0]
    return output.decode(encoding="utf-8").strip()


class WMCTRLUtils(object):
    def switch_to_from_windows_list(windows_options: List[str]):
        current_workspace_windows_dmenu_str = "\n".join(windows_options)
        selected_window = exec(
            f"echo '{current_workspace_windows_dmenu_str}' | dmenu -l 15 -fn 'Inconsolata-11'  -nb '#2C323E' -nf '#9899a0' -sb '#BF616A' -sf '#2C323E'"
        )
        exec(f"wmctrl -a {shlex.quote(selected_window)}")
