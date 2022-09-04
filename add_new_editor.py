from sportblog import create_app, create_new_editor


app = create_app()

if __name__ == '__main__':
    create_new_editor(app)