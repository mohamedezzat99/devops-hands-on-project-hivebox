# ---- 1. Builder Stage: Prepare the environment ----
# This stage has all the tools needed to build our dependencies correctly.
FROM ghcr.io/astral-sh/uv:python3.13-alpine AS builder

WORKDIR /app

# Create a virtual environment. This is a crucial step.
RUN uv venv

# Copy only the dependency files to leverage layer caching.
COPY pyproject.toml uv.lock ./

# Install dependencies into the virtual environment. This will install the
# correct, musl-compatible version of pydantic-core.
RUN uv sync --locked

# Copy the rest of your application code.
COPY . .

# ---- 2. Final Stage: Run the application ----
# Start from a clean, lightweight Python base image.
FROM python:3.13-alpine AS final

# Create the non-root user for security.
RUN addgroup -S app && adduser -S -G app app

WORKDIR /app

# Copy the pre-built virtual environment from the builder stage.
# No installation happens here, we just copy the finished product.
COPY --from=builder /app/.venv ./.venv

# Copy the application source code.
COPY --from=builder /app .

# Fix ownership so the non-root user can access the files.
RUN chown -R app:app /app

# Switch to the non-root user.
USER app

# **THE KEY FIX**: Activate the virtual environment by adding it to the PATH.
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

# **THE SECOND KEY FIX**: Call uvicorn directly.
# It's now on the PATH, and we are no longer using `uv run`.
# This prevents any runtime re-installation.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]