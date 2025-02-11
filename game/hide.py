import subprocess

def hider():
    subprocess.check_call(["attrib","+H","game/hide.py"])
    subprocess.check_call(["attrib","+H","game/easy.py"])
    subprocess.check_call(["attrib","+H","game/fork.py"])
    subprocess.check_call(["attrib","+H","game/hard.py"])
