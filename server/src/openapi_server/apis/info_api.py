# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.info import Info


router = APIRouter()


@router.get(
    "/info",
    responses={
        200: {"model": Info, "description": "successful operation"},
        405: {"description": "Invalid input"},
    },
    tags=["Info"],
    response_model_by_alias=True,
)
async def get_info(
) -> Info:
    """"""
    ...
