from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


## helper function to check if block is a quote
def __is_quote(block):
    split_blocks = block.split("\n")
    for line in split_blocks:
        if line[0] != ">":
            return False
        
    return True

def __is_unordered_list(block):
    split_blocks = block.split("\n")
    for line in split_blocks:
        
        if not line.startswith("- "):
           
            return False
        
    return True

def __is_ordered_list(block):
    split_blocks = block.split("\n")
    count = 1
    for line in split_blocks:
        if not line.startswith(f"{count}. "):
            return False
        count += 1
        
    return True


def block_to_block_type(block):
     if len(re.findall(r"\#{1,6} (.*?)", block)) == 1:
         # we have a heading
         return BlockType.HEADING
     elif(block[0:3] == "```" and block[-3:] == "```"):
         return BlockType.CODE
     elif(__is_quote(block)):
         return BlockType.QUOTE
     elif(__is_unordered_list(block)):
         return BlockType.UNORDERED_LIST
     elif(__is_ordered_list(block)):
         return BlockType.ORDERED_LIST
     else:
         return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    split_markdown = markdown.strip().split("\n\n")
    filtered_list = list(filter(lambda block: block!="",split_markdown))    
    return filtered_list