# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   python_study
    @File    :   db_merge.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/11/11 上午9:28   hello      1.0         None

'''
import os
import re

def merge_db(db_path, output_path,db_from_name:int,db_to_name:int,file_grep):
    if not os.path.exists(db_path):
        print("Error: db_path not exists!")
        return
    if os.path.exists(output_path):
        os.remove(output_path)

    with open(output_path, 'w') as f:
        for root, dirs, files in os.walk(db_path):
            print(root, dirs, files)
            for dir in dirs:
                if dir not in [f"db{seq}" for seq in range(db_from_name, db_to_name+1)]:
                    continue
                f.write( f"use {dir};\n")
                for file in os.listdir(f"{root}/{dir}"):
                    if not file_grep.search(file):
                        continue
                    with open(f"{dir}/{file}", 'r') as f_db:
                        f.write(f_db.read())
                        f.write("\n")

def main():
    db_path = "."
    # output_path = "import.sql"
    grep_str = "cdlf"

    file_grep = re.compile(rf"^{grep_str}.*\.sql$")

    merge_db(db_path, "import1.sql", 1, 8, file_grep)
    # merge_db(db_path, "import2.sql",9 , 16, file_grep)
    # merge_db(db_path, "import3.sql", 17, 24, file_grep)
    # merge_db(db_path, "import4.sql", 25, 32, file_grep)

if __name__ == '__main__':
    main()
