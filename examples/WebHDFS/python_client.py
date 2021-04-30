import hdfs

client = hdfs.Client('http://localhost:9870', root='/')
print(client.list('/'))

with client.write('/streaming.txt', encoding='utf-8') as hdfs_file:
    for idx in range(10_000):
        hdfs_file.write(f'{idx} {idx ** 2} {idx ** 3}\n')
