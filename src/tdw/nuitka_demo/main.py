from tdw.nuitka_demo.config import get_settings
from tdw.nuitka_demo import __version__
from fastapi import FastAPI
import uvicorn

def get_app() -> FastAPI:
    """
    Creates the Fast API application instance
    :return: The application instance
    """
    settings = get_settings()

    app = FastAPI(
        title="Nuitka Fast API Demo",
        description="Fast API Demo App for Nuitka Compilation",
        version=__version__,
    )
    return app


if __name__ == "__main__":
    print("hello")
    settings = get_settings()

    uvicorn_params = {
        "app": settings.uvicorn_app,
        "host": settings.uvicorn_host,
        "log_config": None,
        "port": settings.uvicorn_port,
        "reload": settings.uvicorn_reload
    }

    uvicorn.run(**uvicorn_params)
