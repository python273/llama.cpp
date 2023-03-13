import socket
import sys

prompt = """Cypher:
All I do is what he tells me to do. If I had to choose between that and the Matrix, I'd choose the Matrix.
Trinity:
The Matrix isn't real.
Cypher:
I disagree, Trinity. I think that the Matrix"""

# prompt = sys.argv[1]
prompt = prompt.encode("utf-8")

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print("Connecting to socket")
s.connect("/tmp/llama.sock")

n_predict = 128  # tokens to predict

print("Sending prompt")
s.send(
    len(prompt).to_bytes(4, byteorder="little")
    + prompt
    + n_predict.to_bytes(4, byteorder="little")
)

print("Receiving response")

while True:
    d = s.recv(4096)
    if not d: break
    sys.stdout.buffer.write(d)
    sys.stdout.flush()

print()
