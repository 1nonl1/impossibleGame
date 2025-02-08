import subprocess

def hider():
    subprocess.check_call(["attrib","+H","Python/game/hide.py"])
    subprocess.check_call(["attrib","+H","Python/game/easy.py"])
    subprocess.check_call(["attrib","+H","Python/game/fork.py"])
    subprocess.check_call(["attrib","+H","Python/game/hard.py"])
