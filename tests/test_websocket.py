import asyncio

from hota.template.custom import CustomElement
from hota.html import b, h1, i, span
from hota.websocket import HTMLOverTheAirEndpoint, HTMLOverTheAirWebSocket
from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    return FileResponse('./tests/index.html')


class MyElement(CustomElement):
    async def setup(self):
        self.test = "foo"

    async def click(self):
        self.test = "bar"

    async def render(self):
        if self.test == "bar":
            return span[i["baz"], "foobar", b["barbaz"]]
        return h1(on_click=self.click)[self.test]


async def on_accept(websocket: HTMLOverTheAirWebSocket):
    await websocket.dom.render(MyElement)

routes = [
    Route("/", endpoint=homepage),
    WebSocketRoute("/ws", endpoint=HTMLOverTheAirEndpoint(on_accept=on_accept))
]

app = Starlette(routes=routes)
