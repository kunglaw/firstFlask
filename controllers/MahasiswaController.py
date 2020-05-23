from models.Mahasiswa import Mahasiswa
from flask import render_template

class MahasiswaController:
    def __init__(self):
        super()
    
    @staticmethod
    def listMahasiswa(mysql):
        
        return Mahasiswa.showAll(mysql)
        