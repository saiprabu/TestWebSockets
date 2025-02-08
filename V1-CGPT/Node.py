import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"
    print("🔄 Connecting to the WebSocket server...")

    try:
        async with websockets.connect(uri) as websocket:
            print("✅ Connected successfully!")

            while True:
                message = input("📝 Enter message (or type 'exit' to quit): ")
                if message.lower() == "exit":
                    print("🔚 Closing connection...")
                    break

                await websocket.send(message)
                print(f"📤 Sent: {message}")

                response = await websocket.recv()
                print(f"📩 Received from server: {response}")

    except websockets.exceptions.ConnectionClosed:
        print("❌ Server closed the connection.")
    except Exception as e:
        print(f"⚠️ Error: {e}")
    finally:
        print("🔴 Disconnected from server.")

# Run client
if __name__ == "__main__":
    asyncio.run(client())
