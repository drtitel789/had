while True:
    try:
        import had
    except SystemExit:      
        pass
    except KeyboardInterrupt:
        print("Exit")
        break