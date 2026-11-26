import os


line = "I opened the intern's pull request planning to rewrite his clumsy loop; his one comment showed my API was the bug, so I merged his three lines and quietly deleted mine."
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as output_file:
    output_file.write(line + "\n")
