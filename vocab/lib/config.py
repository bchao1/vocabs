# Please change PATH to the ABSOLUTE path to the local dictionary file.
import os
import vocab

module_path = os.path.abspath(vocab.__file__) 
module_path = os.path.split(module_path)[0]
DICT_DIR = os.path.join(module_path, "local")
DICT_PATH = os.path.join(module_path, "local/dict")