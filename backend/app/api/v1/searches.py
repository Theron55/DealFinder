from fastapi import APIRouter

from app.schemas.search import SearchPreviewRequest

router = APIRouter(prefix="/searches")


@router.post("/preview")
def preview_search(request: SearchPreviewRequest) -> SearchPreviewRequest:
    """Validate and preview a marketplace search request."""
    return request