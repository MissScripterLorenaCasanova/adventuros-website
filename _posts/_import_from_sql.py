import re

def clean(string):
    string = string.replace("#", "").replace("{$$}", "#")
    return string

def generate_md(name, date, text):
    md_file = "---\nlayout: article\ntitle: \"" + name + "\"\n---\n\n"
    md_file += text

    md_clean_name = re.sub('[^a-zA-Z-\-^\d+$]+', '', name.replace(" ", "-").lower())
    md_file_name = date[:10] + "-" + md_clean_name + ".md"

    f = open(md_file_name, 'wb')
    f.write(md_file)

with open('big-file.sql') as f:
    content = f.read().replace("\\#", "{$$}").split('|')
    fields = 5
    final = ""
    for i in range(30):
        name = clean(content[1 + (i * fields)])
        date = clean(content[3 + (i * fields)])
        text = clean(content[5 + (i * fields)])
        generate_md(name, date, text)