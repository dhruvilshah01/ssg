import shutil
import os

from convert_markdown import markdown_to_blocks, block_to_block_type, markdown_to_html_node
from blocks import BlockType


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir_list = os.listdir(dir_path_content)
    for directory in dir_list:
        curr_content_path = os.path.join(dir_path_content,directory)

        #it is an index file
        if(os.path.isfile(curr_content_path)):

            #update destination path
            curr_dir_path = os.path.join(dest_dir_path, "index.html")
            #print new destination directory path

            #call generate page
            generate_page(curr_content_path,template_path,curr_dir_path, basepath)
        #it is a directory
        else:
            curr_dir_path = os.path.join(dest_dir_path, directory)
            os.mkdir(curr_dir_path)
            generate_pages_recursive(curr_content_path, template_path, curr_dir_path, basepath)
    return

    

def generate_page(from_path, template_path, dest_path, basepath):
    #print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_path_file = open(from_path, "r")
    from_content = from_path_file.read()

    template_path_file = open(template_path, "r")
    template_content = template_path_file.read()

    node = markdown_to_html_node(from_content)
    content = node.to_html()
    title = extract_title(from_content)
   

    replaced_title = template_content.replace("{{ Title }}", title)
    content = replaced_title.replace("{{ Content }}", content)
    content = template_content.replace('href="/',f'href="{basepath}')
    content = template_content.replace('src="/', f'src="{basepath}')

    
    
    with open(dest_path, "w+") as file:
        file.write(content)
    

    from_path_file.close()
    template_path_file.close()


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            num_pounds = block.count("#")
            if num_pounds == 1:
                return block[2:]
    raise Exception("No Header")
        


def copy_static_files(copy_to_dir):
    #purge and recreate public directory
    if(os.path.exists(copy_to_dir)):
        shutil.rmtree(copy_to_dir)
    os.makedirs(copy_to_dir)
    copy_static_files_helper("./static",copy_to_dir)

def copy_static_files_helper(src_path, dest_path):
    dir_list = os.listdir(src_path)
    #loop through directory list
    for dir in dir_list:
        curr_src_path = os.path.join(src_path, dir)
        curr_dest_path = os.path.join(dest_path, dir)
        if(os.path.isfile(curr_src_path)):
            # copy into public
            shutil.copy(curr_src_path,os.path.join(dest_path, dir))
        #it is a directory
        else:
            os.mkdir(curr_dest_path)
            copy_static_files_helper(curr_src_path,curr_dest_path)
    
    return
    

