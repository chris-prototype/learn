from pathlib import Path
import threading
import time

_write_lock = threading.Lock()
FILE_PATH = Path("threads.txt")


def append_line(line: str) -> None:
  with _write_lock:
    content = FILE_PATH.read_text() if FILE_PATH.exists() else ""
    FILE_PATH.write_text(content + line + "\n")
    print('line is being written ...')
    time.sleep(1) # simulate a long write_text operation
    print('line is written:', line)


t1 = threading.Thread(target=append_line, args=("from thread 1",))
t2 = threading.Thread(target=append_line, args=("from thread 2",))

t1.start()
t2.start()

t1.join()
t2.join()