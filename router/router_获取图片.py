import io

from fastapi import APIRouter, Response
from PIL import Image

router = APIRouter(prefix="/blob")


@router.get("")
def GetImageBlob(img: str):
    byte = io.BytesIO()
    with Image.open(img) as im:
        if im.mode.lower() != "rgba":
            im = im.convert("RGBA")

        im.thumbnail((300, 300), Image.LANCZOS)
        im.save(byte, format="png")

    return Response(
        byte.getvalue(),
        media_type="image/png",
    )
