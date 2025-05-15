import sys
from generate_page import copy_static_files, generate_pages_recursive


def main():
    # copy static files from static to public
    copy_static_files("./docs")

    # generate a page
    basepath = "/"
    if(len(sys.argv)>1):
        basepath = sys.argv[1]
    
    print(basepath)
    
    generate_pages_recursive("./content", "template.html", "./docs", basepath)


        
if __name__ == "__main__":
    main()