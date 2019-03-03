#!/usr/bin/env python
import pickle
import os.path
import os

class Pickling:
    def __call__(self, path, file_name, var_to_ser):
        if os.path.isdir(path) is True:
            try:
                full_path = os.path.join(path, file_name)
                with open(full_path, "wb") as file:
                    file.write(pickle.dumps(var_to_ser))

            except pickle.PickleError : print("During the serialization unexpected error occurred, repeat the operation "
                        "several times, in case  you don’t succeed, please write to the developer  happycloud2012@gmail.com")
        else: print(f"Your path {path} is not correct, pleasy try again")

pickling = Pickling()

class UnPickling:
    def __call__(self, path):
        if os.path.isfile(path) is True:
            try:
                with open(path, "rb") as file:
                    pickle.load(file)
            except pickle.UnpicklingError: print(f"Error during the deserialization of file, most likely you indicated"
                                f" the wrong path {path} to the deserialization file")

un_pickling = UnPickling()
