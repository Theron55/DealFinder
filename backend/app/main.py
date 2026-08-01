from fastapi import FastAPI

app = FastAPI(
    title="Dealwise API",
    description="Backend API for finding and evaluating worthwhile used-item deals.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Confirm that the Dealwise API is running."""
    return {"status": "healthy"}