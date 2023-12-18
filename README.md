## iMessage analytics

A small script for personal use.

### Quick start

Run this in your terminal (obviously replacing the phone number with the one you want to investigate):

```sh
cd ~/Library/Messages ; sqlite3 chat.db "SELECT text FROM message JOIN handle ON message.handle_id = handle.ROWID WHERE handle.id = '+12345678910' AND text IS NOT NULL ORDER BY message.date ASC;" > data.txt
```

This will then output the entire locally-stored conversation into a file at the same location the command was executed called `output.txt`. Bring this file to the same level as the `main.py` file.

Run `pip install -r requirements.txt`.

Add a `.env` file and set the `MATCH` variable to be the regex you want to match against.

Run `python main.py`.