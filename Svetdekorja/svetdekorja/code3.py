import math

def calculate_rolls():
    # Open popup
    def toggle_popup():
        if kalkulator_rol.is_visible:
            kalkulator_rol.hide()
        else:
            kalkulator_rol.show()

    # Change roll matching type
    def change_matching_type():
        match_yes.hide()
        match_yes_delay.hide()
        selected_radio = roll_radio.filter(":checked")
        if selected_radio.length > 0:
            selected_radio_class = selected_radio.attr("class")
            if selected_radio_class:
                match_yes_delay.show() if "yes_delay" in selected_radio_class else match_yes.show()

    # When user inputs data
    def on_input_change():
        # Get dimension values
        wall_width = int(wall_width_input.val() or wall_width_input.attr("placeholder"))
        wall_height = int(wall_height_input.val() or wall_height_input.attr("placeholder"))
        roll_width = int(roll_width_input.val() or roll_width_input.attr("placeholder"))
        roll_length = int(roll_length_input.val() or roll_length_input.attr("placeholder"))

        # Get matching values
        match = match_checkbox.filter(":checked").val() or "no"
        matching = 0
        delay = 0
        if match == "no":
            matching = 0
            delay = 0
        elif match == "yes":
            matching = int(matching_input.val() or matching_input.attr("placeholder"))
            delay = 0
        elif match == "yes_delay":
            matching = int(matching_input.val() or matching_input.attr("placeholder"))
            delay = int(delay_input.val() or delay_input.attr("placeholder"))

        # Get other values
        trimming = int(trimming_input.val() or trimming_input.attr("placeholder"))
        spare = spare_checkbox.filter(":checked").val() or "no"

        # Calculate lines per wall
        lines_wall = 0
        if roll_width > 0:
            lines_wall = wall_width / roll_width

        # Calculate repeating of pattern
        repeating = 0
        if matching + delay > 0:
            repeating = wall_height / (matching + delay)

        # Calculate tape length
        tape_length = 0
        if match == "no":
            tape_length = wall_height + trimming
        elif match == "yes":
            tape_length = math.ceil(repeating) * matching + trimming
        elif match == "yes_delay":
            tape_length = math.ceil(repeating) * (matching + delay) + trimming

        # Calculate tapes per roll
        tapes_rolls = 0
        if tape_length > 0:
            tapes_rolls = roll_length / tape_length

        # Calculate required rolls
        required_rolls = 0
        if math.floor(tapes_rolls) > 0:
            required_rolls = math.ceil(math.ceil(lines_wall) / math.floor(tapes_rolls))

        # Add spare roll
        if spare == "yes":
            required_rolls += 1

        # Set result in the equation
        required_rolls_label.text(required_rolls)

    # DOM elements
    kalkulator_button = jQuery("#kalkulator-button")
    kalkulator_rol = jQuery("#kalkulator-rol")
    roll_radio = jQuery(".roll-radio")
    match_yes = jQuery(".match_yes")
    match_yes_delay = jQuery(".match_yes_delay")
    wall_width_input = jQuery("#wall-width")
    wall_height_input = jQuery("#wall-height")
    roll_width_input = jQuery("#roll-width")
    roll_length_input = jQuery("#roll-length")
    match_checkbox = jQuery(".match")
    matching_input = jQuery("#matching")
    delay_input = jQuery("#delay")
    trimming_input = jQuery("#trimming")
    spare_checkbox = jQuery(".spare")
    required_rolls_label = jQuery("#required-rolls")

    # Event listeners
    kalkulator_button.on("click", toggle_popup)
    roll_radio.on("change", change_matching_type)
    inputs = jQuery(".roll-input, .roll-radio")
    inputs.on("input change", on_input_change)

# Run the function on document ready
calculate_rolls()
