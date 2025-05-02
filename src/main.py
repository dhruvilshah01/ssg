from textnode import TextNode, TextType
from leafnode import LeafNode  


def main():
    textNode = TextNode("something", "link", "https://something.com")
    print(textNode)

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
            return LeafNode("img", value= "",props={"src":text_node.url,"alt": ""})
        case _:
            raise ValueError("not a valid text type")
        
if __name__ == "__main__":
    main()