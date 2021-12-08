import aiohttp
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({"hello": "world"})


async def mockcalls(request):
    async with aiohttp.ClientSession() as client:
        async with client.get("http://wiremock:8080/ret") as resp:
            return await resp.text()


app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
        Route("/call1", mockcalls),
    ],
)
