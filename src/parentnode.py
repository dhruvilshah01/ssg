from htmlnode import HTMLNode   

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children= children, props = props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Parent Node requires a tag")
        
        if not self.children:
            raise ValueError("Parent Node requires children")

        return self.__print_html()
    

    def __print_html(self):
        children_string = ""
        for child in self.children:
            if(isinstance(child,ParentNode)):
                children_string += child.__print_html() 
               
            else:
                children_string = children_string + child.to_html()

        ## it will eventually get to this base case. add tags for this until we reach the end of the children essentially
        return f"<{self.tag}>{children_string}</{self.tag}>"

        
            

        
        
    



