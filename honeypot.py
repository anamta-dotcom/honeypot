import socket

def simulate_honeypot(port):
  """Simulates a basic honeypot service on a given port."""

  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind(('', port))
  server_socket.listen()

  print(f"[*] Honeypot listening on port {port}")

  while True:
    # Wait for a connection
    client_socket, address = server_socket.accept()

    # Simulate receiving data from attacker
    data = client_socket.recv(1024).decode()  # Receive up to 1024 bytes
    stripped_data = data.strip()

    # Log the received data 
    print(f"[*] Received data from attacker ({address}): {stripped_data}")

    # Simulate a basic response (e.g., echoing data)
    response = f"You connected to a honeypot! (#{stripped_data})"
    client_socket.sendall(response.encode())

    client_socket.close()

# Choose a port to listen on (replace with a valid port number)
port = 8080

# Simulate permission check (for educational purposes only)
def has_permission():
  # Replace with actual permission check for production (e.g., using libraries like psutil)
  return True  # Placeholder for educational purposes

if has_permission():
  # Start the honeypot simulation
  simulate_honeypot(port)
else:
  print('Thank you for using our honeypot')
