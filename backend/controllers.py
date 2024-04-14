from model import read_pdf


def get_home():
    return {'message': 'Welcome to the home page!'}


def upload(filename):
    return read_pdf(file_name=filename)
