# Saber Test

This project leverages FastAPI and Docker for easy development and testing.

## Getting Started

To start the project, simply open a terminal at the root directory and execute the following command:

```bash
docker-compose up
```

This will start two services:
1. `build_system` - The FastAPI application.
2. `build_system_tests` - Runs the test suite contained in the `tests/test_app.py` file.

## Testing

You can interact with the application by accessing the following endpoint:

```
http://127.0.0.1:8000/get_tasks
```

There are unit tests set to run automatically through the `build_system_tests` container. The tests are located in `tests/test_app.py`.

## Troubleshooting

If you experience difficulties running the application, it's possible that port 8000 is being used by another service on your machine. You can change the port by adjusting the `ports` configuration in the `docker-compose.yml`.

In the following configuration,

```yaml
ports:
  - "8000:8000"
```

The first `8000` refers to the port on your machine. Change this number to another available port if 8000 is already in use.

Feel free to reach out if you have questions or need further assistance.