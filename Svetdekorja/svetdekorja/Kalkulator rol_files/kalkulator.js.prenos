jQuery(document).ready(function()
{
    // Open popup
    jQuery('#kalkulator-button').on('click', function()
    {
        jQuery('#kalkulator-rol').toggle();
    });
    
    // Change roll matching type
    jQuery('.match_yes').hide();
    jQuery('.match_yes_delay').hide();
    jQuery('.roll-radio').on('change', function()
    {
        var id = jQuery(this).attr('id');
        jQuery('.match_yes').hide();
        jQuery('.match_yes_delay').hide();
        jQuery('.'+id).show();
    });
    
    // When user inputs data
    jQuery('.roll-input, .roll-radio').on('input change', function()
    {
        // Get dimension values
        var wall_width = parseInt(jQuery('#wall-width').val() || jQuery('#wall-width').attr('placeholder'));
        var wall_height = parseInt(jQuery('#wall-height').val() || jQuery('#wall-height').attr('placeholder'));
        var roll_width = parseInt(jQuery('#roll-width').val() || jQuery('#roll-width').attr('placeholder'));
        var roll_length = parseInt(jQuery('#roll-length').val() || jQuery('#roll-length').attr('placeholder'));
        
        console.log('Dimensions');
        console.log(wall_width);
        console.log(wall_height);
        console.log(roll_width);
        console.log(roll_length);
        
        // Get matching values
        var match = jQuery('.match:checked').val() || 'no';
        var matching = 0;
        var delay = 0;
        if (match === 'no')
        {
            matching = 0;
            delay = 0;
        }
        else if (match === 'yes')
        {
            matching = parseInt(jQuery('#matching').val() || jQuery('#matching').attr('placeholder'));
            delay = 0;
        }
        else if (match === 'yes_delay')
        {
            matching = parseInt(jQuery('#matching').val() || jQuery('#matching').attr('placeholder'));
            delay = parseInt(jQuery('#delay').val() || jQuery('#delay').attr('placeholder'));
        }
        
        console.log('Matching');
        console.log(match);
        console.log(matching);
        console.log(delay);
        
        // Get other values
        var trimming = parseInt(jQuery('#trimming').val() || jQuery('#trimming').attr('placeholder'));
        var spare = jQuery('.spare:checked').val() || 'no';
        
        console.log('Other');
        console.log(trimming);
        console.log(spare);
        
        // Calculate lines per wall
        var lines_wall = 0;
        if (roll_width > 0)
        {
            lines_wall = wall_width / roll_width;            
        }
        
        // Calculate repeating of pattern
        var repeating = 0;
        if ((matching + delay) > 0)
        {
            repeating = wall_height / (matching + delay);
        }
        
        // Calculate tape length
        var tape_length = 0;
        if (match === 'no')
        {
            tape_length = wall_height + trimming;
        }
        else if (match === 'yes')
        {
            tape_length = Math.ceil(repeating) * matching + trimming;
        }
        else if (match === 'yes_delay')
        {
            tape_length = Math.ceil(repeating) * (matching + delay) + trimming;
        }
        
        // Calculate tapes per roll
        var tapes_rolls = 0;
        if (tape_length > 0)
        {
            tapes_rolls = roll_length / tape_length;
        }
        
        // Calculate required rolls
        var required_rolls = 0;
        if (Math.floor(tapes_rolls) > 0)
        {
            required_rolls = Math.ceil(Math.ceil(lines_wall) / Math.floor(tapes_rolls));
        }
        
        // Add spare roll
        if (spare === 'yes')
        {
            required_rolls++;
        }
        
        console.log('Results');
        console.log(lines_wall);
        console.log(repeating);
        console.log(tape_length);
        console.log(tapes_rolls);
        console.log(required_rolls);
        
        // Set result in the equation
        jQuery('#required-rolls').html(required_rolls);
    });
});

