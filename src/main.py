from textnode import TextNode, TextType

def main():
    text_node = TextNode("Some url", TextType.LINK, "www.google.com")
    print(text_node)

if __name__ == "__main__":
    main()
