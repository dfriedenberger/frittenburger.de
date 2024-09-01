# main.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import markdown
import chevron

app = FastAPI()


def get_markdown(file, title):
    with open(f'content/{file}', 'r', encoding='UTF-8') as f:
        md_text = f.read()
        html_body = markdown.markdown(
            md_text, extensions=['fenced_code', 'tables'])
        with open('template.html', 'r', encoding='UTF-8') as t:
            return chevron.render(t, {'title': title, 'body': html_body})


@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = get_markdown(file='index.md', title='frittenburger.de')
    return HTMLResponse(content=html_content, status_code=200)

app.mount("/", StaticFiles(directory="."), name="static")
