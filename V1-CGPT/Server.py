import asyncio
import websockets

async def handle_client(websocket, path=None):  # ✅ FIX: Ensure 'path' is included
    """Handles communication with a WebSocket client."""
    client_address = websocket.remote_address
    print(f"🔵 New client connected: {client_address}")

    try:
        async for message in websocket:
            print(f"📩 Received from {client_address}: {message}")

            response = f"Echo: {message}"
            await websocket.send(response)
            print(f"📤 Sent to {client_address}: {response}")

    except websockets.exceptions.ConnectionClosed:
        print(f"🛑 Client {client_address} disconnected.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

async def start_server():
    """Starts a WebSocket server on ws://localhost:8765."""
    print("🚀 Starting WebSocket server on ws://localhost:8765")
    
    server = await websockets.serve(handle_client, "localhost", 8765)  # ✅ FIX: Corrected handler
    print("✅ WebSocket server is running. Waiting for clients...")

    await server.wait_closed()  # ✅ FIX: Keeps server running properly
    print("✅ This LINE Can't be Printed")

if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print("🛑 Server shutting down...")
