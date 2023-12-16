from blacksheep import Application, get

app = Application()


@get('/:greeting')
async def helloworld(greeting):
    return f"{greeting}, world!"
