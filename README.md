# FastAPI Chessboard Application

## Overview

Welcome to the FastAPI Chessboard application! This project demonstrates a chessboard where you can find valid moves for different chess pieces, including Queen, Bishop, Rook, and Knight.

## Prerequisites

Before running the application, make sure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/installation/)
- [Uvicorn](https://www.uvicorn.org/)

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/fastapi-chessboard.git
    cd fastapi-chessboard
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-repository
    ```

3. **Build the Docker image:**

    ```bash
    docker build -t image_name:0.0.1 .
    ```

   Replace `image_name` with a meaningful name for your Docker image, and `0.0.1` with the desired version.

4. **Run the Docker container:**

    ```bash
    docker run -p 8000:8000 image_name:0.0.1
    ```

5. **Access your application:**

    Visit [http://localhost:8000](http://localhost:8000) in your browser.

6. **API Usage:**

    After accessing [http://localhost:8000](http://localhost:8000), append the route `/chess/<slug>`, where `<slug>` represents the name of the chess piece (queen, rook, bishop, knight).

7. **Make a POST request:**

    Use a POST method with JSON-formatted input sent in the request body. For example:

    ```json
    {"postions": {"Queen": "E7", "Bishop": "B7", "Rook": "G5", "Knight": "C3"}}
    ```

8. **Review the JSON response:**

    The output will be a JSON response containing the valid moves for the given chess piece. For example:

    ```json
    {"valid_moves": ["A4", "A2", "B1", "D1"]}
    ```

9. **Stop the container:**

    To stop the running container, use the following command:

    ```bash
    docker stop $(docker ps -q --filter ancestor=image_name:0.0.1)
    ```

   or with `ctrl + c`.

