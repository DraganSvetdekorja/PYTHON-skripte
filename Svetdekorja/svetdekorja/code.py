from bs4 import BeautifulSoup

# Assuming you have the HTML content in a variable named 'html_content'
soup = BeautifulSoup(html_content, 'html.parser')

def calculate():
    # Get dimension values
    wall_width = int(soup.select_one('#wall-width').get('value') or soup.select_one('#wall-width').get('placeholder'))
    wall_height = int(soup.select_one('#wall-height').get('value') or soup.select_one('#wall-height').get('placeholder'))
    roll_width = int(soup.select_one('#roll-width').get('value') or soup.select_one('#roll-width').get('placeholder'))
    roll_length = int(soup.select_one('#roll-length').get('value') or soup.select_one('#roll-length').get('placeholder'))

    # Get matching values
    match = soup.select_one('.match:checked').get('value') or 'no'
    matching = 0
    delay = 0
    if match == 'no':
        matching = 0
        delay = 0
    elif match == 'yes':
        matching = int(soup.select_one('#matching').get('value') or soup.select_one('#matching').get('placeholder'))
        delay = 0
    elif match == 'yes_delay':
        matching = int(soup.select_one('#matching').get('value') or soup.select_one('#matching').get('placeholder'))
        delay = int(soup.select_one('#delay').get('value') or soup.select_one('#delay').get('placeholder'))

    # Get other values
    trimming = int(soup.select_one('#trimming').get('value') or soup.select_one('#trimming').get('placeholder'))
    spare = soup.select_one('.spare:checked').get('value') or 'no'

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
    if match == 'no':
        tape_length = wall_height + trimming
    elif match == 'yes':
        tape_length = math.ceil(repeating) * matching + trimming
    elif match == 'yes_delay':
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
    if spare == 'yes':
        required_rolls += 1

    # Set result in the equation
    soup.select_one('#required-rolls').string = str(required_rolls)

# Open popup
kalkulator_button = soup.select_one('#kalkulator-button')
kalkulator_button.on('click', lambda _: soup.select_one('#kalkulator-rol').toggle())

# Change roll matching type
for element in soup.select('.match_yes'):
    element.hide()
for element in soup.select('.match_yes_delay'):
    element.hide()
for roll_radio in soup.select('.roll-radio'):
    roll_radio.on('change', lambda _: calculate())

# When user inputs data
for element in soup.select('.roll-input, .roll-radio'):
    element.on('input change', lambda _: calculate())

# Call calculate initially to populate the result
calculate()

# Print the modified HTML content
print(soup.prettify())
