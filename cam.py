def CamStream():
    with picamera.PiCamera(resolution='540x380', framerate=15) as camera:
        output = StreamingOutput()
        #Uncomment the next line to change your Pi's Camera rotation (in degrees)
        #camera.rotation = 90
        #camera.vflip = 180
        camera.start_recording(output, format='mjpeg')
        
        try:
            address = ('', 1654)
            server = StreamingServer(address, StreamingHandler)
            server.serve_forever()
        finally:
            camera.stop_recording()
