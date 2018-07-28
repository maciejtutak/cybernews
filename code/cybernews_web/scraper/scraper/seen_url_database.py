import sqlite3


class SeenURLDatabase:
    """Simple sqlite3 wrapper that filters already seen urls."""
    def __init__(self):
        self.conn = sqlite3.connect('seen_urls.db')
        # self.conn.row_factory = lambda cursor, row: row[0]
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS seen_urls(url)")

    def check_url(self, url):
        self.c.execute("SELECT url FROM seen_urls WHERE url=?", (url,))
        seen_url = self.c.fetchone()
        if seen_url is None:
            self.c.execute("INSERT INTO seen_urls VALUES (?)", (url,))
            return True
        else:
            return False

    def close(self):
        if self.conn:
            self.conn.commit()
            self.c.close()
            self.conn.close()
