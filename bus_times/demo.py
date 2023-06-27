def submit_input(e):
    input_box = Element("input_box")
    player_input = input_box.select(".value")
    main_description = Element("main_description")
    main_description.write(player_input)