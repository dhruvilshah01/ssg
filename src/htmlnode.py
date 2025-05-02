

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return ""
        return " " + " ".join(list(map(lambda item:'='.join(item),self.props.items())))
        

    def __repr__(self):
        return f"HTML_NODE({self.tag}, {self.value}, {self.children}, {self.props})"
    




