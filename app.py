from wm_app import create_app, socketio


app = create_app()


if __name__ == '__main__':
    # If SocketIO is available, run via it so websocket transport is enabled.
    if socketio is not None:
        socketio.run(app, debug=True, host='0.0.0.0', port=80)
    else:
        # Fallback to standard Flask run when flask_socketio is not installed
        app.run(debug=True, host='0.0.0.0', port=80)
