# O(n)
def finder(files, queries):
    query_path = {}
    for f in files:
        # split once from the right side with '/', and get the second one,which index = 1
        # for example, /usr/bin/baz, after one time split from the right, we got ['/usr/bin','baz']
        # then we get key='baz' by index = 1
        key = f.rsplit('/', 1)[1]
        value = f
        if key not in query_path:
            query_path[key] = []

        query_path[key].append(f)

    result = []
    # for each item in queries, check if it is also in query_path(compare with the key)
    # if yes, append the values(full paths)
    for x in queries:
        if x in query_path:
            result += query_path[x]

    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

    