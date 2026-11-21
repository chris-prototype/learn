"""
Tests the FastAPI endpoint running at http://127.0.0.1:8000/
"""

import httpx

URL = "http://127.0.0.1:8000/"


def main() -> None:
  response = httpx.get(URL, timeout=10.0)
  print("Status code:", response.status_code)
  print("Response JSON:", response.json())


if __name__ == "__main__":
  main()