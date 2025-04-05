import aiohttp
import asyncio

urls=[
    "https://pic.qqans.com/up/2023-12/17014820426712446.jpg",
    "https://pic.qqans.com/up/2023-12/17014820428982222.jpg",
    "https://pic.qqans.com/up/2023-12/17014820425029890.jpg"
]

async def download(url):
    file_name=url.split("/")[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            with open(file_name,mode="wb") as f:
                f.write(await res.content.read())
    print(url,"搞定")

async def main():
    task=[]
    for url in urls:
        task.append(asyncio.create_task(download(url)))
    await asyncio.wait(task)


if __name__ == '__main__':
    asyncio.run(main())