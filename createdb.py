from sportblog import create_app, create_database


app = create_app()

if __name__ == '__main__':
    create_database(app)
    print('Created Database!')
