from os import getenv

from fastapi import FastAPI

from app.api.routes.router import get_main_router
from app.core.config import get_config

if not getenv("LGS_TESTS") and get_config().is_prod:
    import sentry_sdk

    sentry_sdk.init(
        dsn=get_config().sentry_dsn,
        send_default_pii=True,
        traces_sample_rate=1.0,
    )

app = FastAPI()
app.include_router(get_main_router(), prefix="/api")
