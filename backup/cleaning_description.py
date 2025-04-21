import re

# Extract text from the description

def extracting_description(raw_desc):
    description = []
    # Extract text after ">"
    for line in raw_desc.splitlines():
        # find > and extract until <
        list_words = re.findall(r'>([^<]+)', line)
        #join list of sentences and remove the &qout;
        sentence = ''.join(list_words).replace("&quot;", '')
        # continue to remove junk words
        if sentence != '' and sentence != '&nbsp;':
            description.append(sentence)
    
    return description

# Extract text from the markdown description

def extracting_markdown_desciption(raw_desc):
    descriptions = []
    # Extract text after ">"
    for line in raw_desc.splitlines():
        #join list of sentences and remove the &qout;
        #sentence = ''.join(list_words).replace("&quot;", '')
        # continue to remove junk words
        if line != '' and line != '```' and line != '\xa0':
            descriptions.append(line)
    
    return descriptions