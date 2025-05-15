from blocks import markdown_to_blocks, block_to_block_type, BlockType
from parentnode import ParentNode
from textnode import TextNode, TextType
from convert_nodes import text_to_textnodes, text_node_to_html_node



def generate_list_nodes(block, num_spaces):
    split_block = block.split("\n")
    nodes = []
    for list_item in split_block:
        children = text_to_children(list_item[num_spaces:])
        nodes.append(ParentNode("li", children))
    return nodes
        

def text_to_children(block):
    # convert to text_nodes
    text_node_list = text_to_textnodes(block)
    node_list = []
    #convert to leafnodes adn return the children
    for node in text_node_list:
        node_list.append(text_node_to_html_node(node))
    return node_list

def generate_html_nodes(block_type, block):
    match block_type:
        case BlockType.HEADING:
            num_pounds = block.count("#")
            children = text_to_children(block[num_pounds + 1:])
            return ParentNode(f"h{num_pounds}", children)
        case BlockType.UNORDERED_LIST:
            children = generate_list_nodes(block, 2)
            return ParentNode("ul", children)
        
        case BlockType.ORDERED_LIST:
            children = generate_list_nodes(block, 3)
            return ParentNode("ol", children)
        
        case BlockType.CODE:
            content = block[3:-3]
            if content[0] == "\n":
                content = content[1:]

            textNode = TextNode(content, TextType.CODE)
            child = text_node_to_html_node(textNode)
            return ParentNode("pre", [child])
            
        case BlockType.QUOTE:
            blocks_arr = block.split('\n')
            blocks_arr = [block[2:] for block in blocks_arr]
            block = ('\n'.join(blocks_arr))
            children = text_to_children(block)
            return ParentNode("blockquote", children)
        
        case BlockType.PARAGRAPH:
            #remove the new lines since we don't preserve them in paragraphs
            block.split('\n')
            children = text_to_children(" ".join(block.split("\n")))
            return ParentNode("p", children)



def markdown_to_html_node(markdown):
    nodes = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        generated_nodes = generate_html_nodes(block_type, block)
        nodes.append(generated_nodes)
    
    return ParentNode("div", nodes)
        