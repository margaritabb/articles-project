#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: margaritabozhinova
"""

# Load into SQLite, avoiding duplicates


def create_table(dbfilepath):
    """
    Create a connection to a database stored in dbfilepath.
    Create table natpostaritcles.

    """
    import sqlite3

    conn = sqlite3.connect(dbfilepath)
    c = conn.cursor()

    create_natpost_table = """CREATE TABLE natpostarticles (
                            id TEXT PRIMARY KEY, 
                            link TEXT NOT NULL,
                            artxt TEXT);"""

    c.execute(create_natpost_table)

    c.close()
    conn.close()


def load_data(dbfilepath, dataframe):
    """
    Add dataframe tuples to natpostarticles.

    """
    import sqlite3

    conn = sqlite3.connect(dbfilepath)
    c = conn.cursor()

    sql = """REPLACE INTO natpostarticles 
            (id, link, artxt) 
            VALUES (?, ?, ?);
        """

    c.executemany(sql, dataframe.to_numpy().tolist())
    conn.commit()

    c.close()
    conn.close()
