import os

class GDrive:
    
    @staticmethod
    def folder():
        return os.environ.get('GOOGLE_DRIVE_FOLDER')