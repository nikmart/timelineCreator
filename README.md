# timelineCreator
Create stacked bar timelines from a CSV using matplotlib

## Instructions
Create a CSV with the following columns:

`label,duration,time,color`

`label` - the text label for the section of the timeline
`duration` - how long in minutes the section is
`time` - the end time of each section (not used but helpful for planning)
`color` - color of the section in either hex (`#ffffff`) or named (`'red', 'green'`)

Once you have created the CSV, run

`python makeTimeline.py [datafile.csv]`

## Requirements
`Python`
`matplotlib`
