import os
import shutil

OPTIMIZED_FOLDERS = ['css', 'js', 'image']


class ReplaceSpeed(object):
    def __init__(self, find_dirs=[], optimized_dir=None, exclude_dirs=[]):
        self.find_dirs = find_dirs
        self.optimized_dir = optimized_dir
        self.exclude_dirs = exclude_dirs
        self.optimized_files,  self.optimized_group_files = self.get_optimized_files()

    def get_optimized_files(self):
        if self.optimized_dir is None:
            raise ValueError("None no es un ruta")
        elif not os.path.isdir(self.optimized_dir):
            raise ValueError("Debe asignar una ruta valida {}".format(self.optimized_dir))
        else:
            optimized_files = []
            optimized_group_files = {}
            for dir_name in OPTIMIZED_FOLDERS:
                dir_path = os.path.join(self.optimized_dir, dir_name)
                if os.path.isdir(dir_path):
                    container_files = os.listdir(dir_path)
                    optimized_files += container_files
                    optimized_group_files.update({dir_name: container_files})
            return optimized_files, optimized_group_files

    def recursive_search_replace(self, name, name_path):
        if os.path.isdir(name_path):
            if name_path not in self.exclude_dirs:
                for d in os.listdir(name_path):
                    self.recursive_search_replace(d, os.path.join(name_path, d))
        else:
            if name in self.optimized_files:
                dir_opt = [k for k, v in self.optimized_group_files.items() if name in v][0]
                os.remove(name_path)
                shutil.copy(os.path.join(self.optimized_dir, dir_opt, name), os.path.dirname(name_path))
                print("archivo {} optimizado aplicado".format(name))

    def apply(self):
        for find_dir in self.find_dirs:
            self.recursive_search_replace('', find_dir)







