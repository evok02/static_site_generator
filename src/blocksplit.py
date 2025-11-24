from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered"
    ORDERED_LIST = "ordered"

def markdown_to_blocks(text):
    blocks = text.split("\n\n")
    blocks = list(filter(lambda x: x, map(lambda x: x.strip(), blocks)))
    return blocks

def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    elif block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    elif block[0] == ">":
        return BlockType.QUOTE
    elif block[0] == "-":
        return BlockType.UNORDERED_LIST
    elif block[0].isdigit() and block[1] == ".":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
        





if __name__ == "__main__":
    main()
