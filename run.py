from rpibebecam import application

app = application.create_app()

app.run(debug = True, host = '0.0.0.0')
