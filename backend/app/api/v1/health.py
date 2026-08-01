from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    """Confirm that the Dealwise API is running."""
    return {"status": "healthy"}