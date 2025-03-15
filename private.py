from rubpy import filters, Client
from rubpy.types import Update

app = Client('h_o')

@app.on_message_updates(filters.is_private)
async def group(m:Update):
    if m.text.startswith("e"):
     t = m.text.replace('e','').strip()
     up = sum(1 for char in t if char.isupper())
     await m.reply(f"تعداد حروف بزرگ : {up} ")
     
     
app.run()
