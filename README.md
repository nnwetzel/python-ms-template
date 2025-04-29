# Python Microservice Template

A basic template for a Python MS application with a health check endpoint.

### Prerequisites

1. **Install `uv`**:
   - Skip to step 3 if `uv` is already installed and configured on your system.
   - If not installed, follow the guide [here](https://docs.astral.sh/uv/getting-started/installation/).

2. **Install Python 3.11**:
   ```bash
   uv python install 3.11
   ```

3. **Create a `.env` file** (values for the secret variables can be provided by a developer). This is strictly for local development only:
   ```properties
   CONNECTION_STRING=''

   NLP_ENCODING_SERVICE_HOST=localhost

   LOCAL_DATA_PATH=data/
   BASE_CONTAINER_MOUNT_PATH=/base
   ENV_CONTAINER_MOUNT_PATH=/dev

   MODE=LOCALDEV
   ```

4. **Install Dependencies**:
   ```bash
   uv sync
   ```

5. **Activate Virtual Environment**:
   ```bash
   source .venv/bin/activate
   ```

6. **Install Pre-Commit Hooks**:
   ```bash
   pre-commit install
   ```

### Running Locally

Run the application:
```bash
uv run main.py
```

### Health Check

Once the application is running, you can check the health status by visiting:

http://localhost:4000/health


- **GET /health**: Returns the health status.

### Managing Dependencies

- Add dependencies in `pyproject.toml` and run:
  ```bash
  uv sync
  ```

### Deploying the Microservice

For deployment instructions, see [here](https://confluence.ce.wolterskluwer.io/pages/viewpage.action?pageId=237670385).