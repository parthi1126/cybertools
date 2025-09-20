import requests
import threading
import time
from datetime import datetime

# Configuration
TARGET_URL = "https://xnxx.com"  # Replace with your website URL
NUM_REQUESTS = 100  # Total number of requests
CONCURRENT_THREADS = 10  # Number of concurrent threads
DELAY_BETWEEN_REQUESTS = 0.1  # Delay in seconds between requests in each thread

# Function to send a single HTTPS request
def send_request():
    try:
        start_time = time.time()
        response = requests.get(TARGET_URL, timeout=5)
        elapsed_time = time.time() - start_time
        status = response.status_code
        print(f"[{datetime.now()}] Status: {status}, Response Time: {elapsed_time:.2f}s")
    except requests.RequestException as e:
        print(f"[{datetime.now()}] Error: {e}")

# Function to run requests in a thread
def worker():
    for _ in range(NUM_REQUESTS // CONCURRENT_THREADS):
        send_request()
        time.sleep(DELAY_BETWEEN_REQUESTS)

# Main function to start load test
def main():
    print(f"Starting load test on {TARGET_URL}")
    print(f"Total Requests: {NUM_REQUESTS}, Concurrent Threads: {CONCURRENT_THREADS}")

    # Create and start threads
    threads = []
    for _ in range(CONCURRENT_THREADS):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Load test completed.")

if __name__ == "__main__":
    main()
