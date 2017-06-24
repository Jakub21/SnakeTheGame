def execute():
    #Static Settings
    settings_file_name = "settings.wdf"

    #Modifiable Settings
    try:
        from wdf_test_package import wdf
        settings = wdf.load(settings_file_name)
    except:
        print("\n", "Error: Couldnt load required file (WDF-Package)", "\n")
        return

    #Imports
    try:
        import msvcrt
        import iocontrol
        import menu
        import time
        import game
    except:
        print("\n", settings["err_import"], "\n")
        return


    #Menu loop
    returned = int
    while True:
        returned = menu.main(settings)
        if returned == 0:
            break
        if returned == int(settings["mm_pos_play"]):
            game.init(settings)
        elif returned == int(settings["mm_pos_reload_settings"]):
            print(settings["settings_reload"])
            settings = wdf.load(settings_file_name)
            time.sleep(float(settings["normal_sleep_time"]))
        elif returned == int(settings["mm_pos_exit"]):
            iocontrol.message(settings, "leave")
            break
    #
