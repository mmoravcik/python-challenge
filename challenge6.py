# www.pythonchallenge.com/pc/def/channel.html

# first you need to change URL to end with channel.zip and get the archive

def get_next_file_content(content):
    filename = '/tmp/channel/%s.txt' % content
    with file(filename) as f:
        s = f.read()

    s.replace('The new nothing is ', '')
    return filter(str.isdigit, s)

content = "90052"

previous_files = []

while True:
    try:
        int(get_next_file_content(content))
    except ValueError:
        print content
        break
    else:
        previous_files.append("%s.txt" % content)
        content = get_next_file_content(content)


# using the code above I've found that file 45145 has the next clue
# which was `collect the comments`

import zipfile

filename = '/tmp/channel/%s.txt' % file
with zipfile.ZipFile('/tmp/channel.zip') as myZip:
    print ''.join(myZip.getinfo(file).comment for file in previous_files)

# you will get `hockey`. hockey.html has `it's in the air. look at the letters.`
# hockey word from above is made from letters `oxygen`. `oxygen.html is the solution