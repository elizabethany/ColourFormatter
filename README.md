# ColourFormatter

Takes the colour you picked and converts it to the format used in .entities and .decls. Optional mode for use with recolourHelper.

## Usage
0. You will be prompted to choose if you want to clear the output files (configurable)
1. Select the name for the colour field. For example, I'd select 'color' for an idParticleEmitter's renderModelInfo. An option to enter a custom name is also available.
2. A colour selection window will open up. Pick a colour, then hit "Okay".
3. The formatted colour will now be written to FormattedColours.txt (configurable). By default, the formatted colour should also be printed to the console.

## Configuration
config.ini lets you edit a couple settings, as well as changing the output file or template paths. The templates themselves can also be edited, ex. to adjust indentation.
* `clearSetting` : allows you to disable the prompt to clear the output files or change it to automatically clear without prompting you
* `loopFormatting` : enable/disable the ability to continously select and format colours.
* `printToConsole` : lets you stop the formatted colour from being printed to the console.
* `namingScheme` : change this if you want the RGB colour parameters to switch from `rgb` to `xyz`.
* `recolourHelperMode` : if this is set to `1`, then colour field naming is skipped, and colours will be formatted for use in recolorHelper instead.
