class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("Not Implemented yet")

    def props_to_html(self):
        if not self.props:
            return ""
        html_string = ""
        for key, value in self.props.items():
            html_string += f"{key}=\"{value}\" "
        html_string = html_string.strip()
        return html_string
                
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.tag == "img":
            return f"<{self.tag} {self.props_to_html()}>"
        elif not self.tag:
            return self.value
        elif not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
            
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode should has a tag")
        if not self.children:
            raise ValueError("ParentNode should has children")
        children_to_html = ""
        for child in self.children:
            children_to_html += child.to_html()
        return f"<{self.tag}>{children_to_html}</{self.tag}>"










