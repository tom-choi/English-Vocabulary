def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

# A Tool for creating Markdown file
import os
import time
import re
import pandas as pd


def EV_generate_markdown_file(directory, output_file):
    with open(output_file, 'w+', encoding="UTF-8") as f:
        f.write("# English-Vocabulary List\n\n")
        f.write("| Words | Pos | CEFR |\n")
        f.write("|---|---|---|\n")

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_name = os.path.basename(file_path)
                if (file_name[-4:] != ".txt"):
                    continue
                file_name = file_name[:-4]
                relative_path = os.path.relpath(file_path, directory)
                
                content = ReadTXT(f"{directory}/{relative_path}")
                wordslist = content.split(',')
                for i in wordslist:
                    if (i == "" or i == " "):
                        continue
                    print(i)  
                    try:
                        CEFR_name = ps[i]
                    except:
                        CEFR_name = "N/A"
                    try:
                        tags_name = posps[i]
                    except:
                        tags_name = "N/A"
                    word_name = i
                    result = f"| {word_name} | {CEFR_name} | {tags_name} |\n"
                    f.write(f"{result}")

    print(f"Markdown file generated: {output_file}")

def ReDiff(path: str):
    content = ReadTXT(path)

    # Extract tags using regular expression
    wordslist = content.split(',')
    for i in wordslist:
        print(i)    
    return content
    
def ReadTXT(filename: str):
    print("Loading:" + filename)
    with open(filename, "r", encoding="UTF-8") as file:
        content = file.read()
    return content

url1 = "https://raw.githubusercontent.com/openlanguageprofiles/olp-en-cefrj/master/octanove-vocabulary-profile-c1c2-1.0.csv"
url2 = "https://raw.githubusercontent.com/openlanguageprofiles/olp-en-cefrj/master/cefrj-vocabulary-profile-1.5.csv"
df1 = pd.read_csv(url1)
df2 = pd.read_csv(url2)
ps = {}
posps = {}
for i in range(len(df1)):
    ps[df1.headword[i]] = df1.CEFR[i]
    posps[df1.headword[i]] = df1.pos[i]
    # print(ps[df1.headword[i]])
for i in range(len(df2)):
    ps[df2.headword[i]] = df2.CEFR[i]
    posps[df2.headword[i]] = df2.pos[i]
    # print(ps[df2.headword[i]])

directory_to_search = "./text"
output_markdown_file = "Daily.md"

EV_generate_markdown_file(directory_to_search, output_markdown_file)
