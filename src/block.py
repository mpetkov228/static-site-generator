import re

from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def block_to_blocktype(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("* ") or line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    is_ordered_list = True
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i+1}. "):
            is_ordered_list = False
            break
    
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH