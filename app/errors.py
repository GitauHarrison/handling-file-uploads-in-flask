from app import app


@app.errorhandler(413)
def file_too_large(error):
    return 'File is too large', 413
