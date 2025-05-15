from textnode import TextType, TextNode
from leafnode import LeafNode
import re

def extract_markdown_images(text):
    images_markdown = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images_markdown

def extract_markdown_links(text):
    links_markdown = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return links_markdown

def split_nodes_image(old_nodes):
     new_nodes = []
    
     for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue 
            
        images = extract_markdown_images(node.text)

        if(len(images) > 0):
            curr_text = node.text
            for image in images:
                img_text = image[0]
                img_url = image[1]
                split_text = curr_text.split(f"![{img_text}]({img_url})", maxsplit = 1)
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                new_nodes.append(TextNode(img_text, TextType.IMAGES, img_url))

            
                curr_text = split_text[1]
            if(curr_text != ""):
                new_nodes.append(TextNode(curr_text, TextType.TEXT))

        else:
            new_nodes.append(node)


     return new_nodes
        

def split_nodes_link(old_nodes):
     new_nodes = []
    
     for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)

        if(len(links) > 0):
            curr_text = node.text
            for link in links:
                link_text = link[0]
                link_url = link[1]
                split_text = curr_text.split(f"[{link_text}]({link_url})", maxsplit = 1)
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINKS, link_url))
                curr_text = split_text[1]
        else:
            new_nodes.append(node)
        

     return new_nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        # Split the text by the delimiter
        pieces = node.text.split(delimiter)
        
        # Check if we have an even number of delimiters (odd number of pieces)
        if len(pieces) % 2 == 0:
            raise ValueError(f"Invalid markdown syntax: Odd number of '{delimiter}' delimiters")
        
     
        for i in range(len(pieces)):
            if(pieces[i]!=""):
                # we have a valid string. Split makes it so that if we have a valid string the odd indices will be the ones wrapped even
                # for edge cases where you start with the delimiter
                if i % 2 == 0:
                    new_nodes.append(TextNode(pieces[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(pieces[i], text_type))
        
    return new_nodes


def text_to_textnodes(text):
    images_nodes = split_nodes_image([TextNode(text,TextType.TEXT)])
    links_nodes = split_nodes_link(images_nodes)
    code_nodes = split_nodes_delimiter(links_nodes, "`", TextType.CODE)
    bold_nodes = split_nodes_delimiter(code_nodes, "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    return italic_nodes


def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case TextType.TEXT :
            return LeafNode(None,value=text_node.text)
        case TextType.BOLD:
            return LeafNode("b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", value=text_node.text)
        case TextType.CODE:
            return LeafNode("code", value=text_node.text)
        case TextType.LINKS:
            return LeafNode("a", value=text_node.text, props={"href":text_node.url})
        case TextType.IMAGES:
            return LeafNode("img", value= text_node.text,props={"src":text_node.url,"alt": ""})
        case _:
            raise ValueError("not a valid text type")