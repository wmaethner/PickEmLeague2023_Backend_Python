with open("./docs/server_version.txt", "r+") as f:
    version = int(f.read())
    f.seek(0)
    f.write(f"{version+1}")
    f.truncate()
