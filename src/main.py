from generate_page import copy_static_files, generate_pages_recursive

def main():
    # copy static files from static to public
    copy_static_files()
    # generate a page
    generate_pages_recursive("./content", "template.html", "./public")


        
if __name__ == "__main__":
    main()