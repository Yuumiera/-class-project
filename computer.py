# -class-project
import time
class Computer:
    def __init__(self,os,RAM,processor,storage):
        self.os = os
        self.RAM = RAM
        self.processor = processor
        self.storage = storage
    def open_the_info(self):
        print("""
        İnfo About Computer
        OS : {}
        RAM : {}
        Processor : {}
        Storage : {}        
        """.format(self.os,self.RAM,self.processor,self.storage))
    def change_os_info(self,info):
        print("İnfo os is changing...")
        time.sleep(2)
        self.os = info
    def change_RAM_info(self,info):
        print("İnfo RAM is changing...")
        time.sleep(2)
        self.RAM = info
    def change_processor_info(self,info):
        print("İnfo processor is changing...")
        time.sleep(2)
        self.processor = info
    def change_storage_info(self,info):
        print("İnfo storage is changing...")
        time.sleep(2)
        self.storage = info
