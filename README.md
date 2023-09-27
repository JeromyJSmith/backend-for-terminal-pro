# Backend template for the OpenBB Terminal Pro

Backend template to bring your own data into the OpenBB Terminal Pro using FastAPI.

Data returned should be in json non-nested format.

Example :

```json
[
	{
		"color": "red",
		"value": "#f00"
	},
	{
		"color": "green",
		"value": "#0f0"
	},
	{
		"color": "blue",
		"value": "#00f"
	}
]
```

## Templates available

Each folder contains an example of a different implementation, the goal is to increase the amount of different use cases so that each customer can start from the one that is most relevant.

#### public_endpoint

This utilizes data from https://api.llama.fi/v2/chain without any modification. This could have been added to the Terminal Pro directly using the "Add Single Widget" functionality - but using the widgets.json file we have more control over the widget.

TBD: Add image of widget to be added.

#### endpoint with API key

tbd

####  readfile_example : process csv or json file

Example of reading some local file from your computer in csv or json format.

#### plotly_example : render plotly chart in a widget

Useful if you want to visualize the data in a unique way that isn't in our charting abilities.

## How to run

1. Go into the folder you want to test
2. Run `uvicorn main:app --port 5050`

(add image of what it looks in console)

3. Add steps for Data Connectors in the Terminal Pro

(add steps according to Terminal Pro)

## Code explained

### main.py

This is responsible by running the FastAPI with endpoints that will be consumed by the Terminal Pro.

This file:

* Enables cross-origin resource sharing (CORS) and configures it according to the domain where FastAPI is running and Terminal Pro link.

* Initializes FastAPI with `app = FastAPI()`

* Ensures that there's a `/widgets.json` file that the OpenBB Terminal Pro can use to configure the widgets configured

```python
@app.get("/widgets.json")
def get_widgets():
    """Widgets configuration file for the OpenBB Terminal Pro"""
    file_path = "widgets.json"
    with open(file_path, "r") as file:
        data = json.load(file)
    return JSONResponse(content=data)
```

* Creates remaining endpoints that retrieve data that will be consumed by the Terminal Pro

### widgets.json

This contains the settings for all the widgets that the backend contains.

This file is a dictionary, and each dictionary within represents a widget.

Each widget will have the following properties:

# Widget Type Definition

widgets.json definitions

TODO - organize this better

```json
{
  // Basic props
  "id": "string", // Unique identifier for the widget.
  "innerTab": "string", // If it's from a template, it may have a tab assigned, e.g., equity template.
  "gridData": {
    // Grid data configuration for the widget.
    "x": 0, // Horizontal grid position.
    "y": 0, // Vertical grid position.
    "w": 0, // Width for the widget in the grid.
    "h": 0, // Height for the widget in the grid.
    "minH": 0, // Minimum height.
    "minW": 0, // Minimum width.
    "maxH": 0, // Maximum height.
    "maxW": 0, // Maximum width.
    "moved": true, // Indicates if the widget has been moved.
    "static": false, // Indicates if the widget is static and cannot be moved.
    "isDraggable": true // Specifies if the widget can be dragged.
  },
  "storage": {
    // Storage for the widget that doesn't fit in the other fields.
    "key": "value"
  },
  "aiHistory": [
    {
      // AI history for the widget.
      "question": "string", // Question for the AI.
      "answer": "string", // Answer from the AI.
      "ticker": "string" // Ticker at the time of the question.
    }
  ],
  "schema": {
    // Schema for the widget.
    "properties": {
      // Properties for the schema.
      "key": {
        "type": "string", // Type of property (object, array, string, number, boolean).
        "title": "string", // Title for the property.
        "description": "string", // Description for the property.
        "default": "value", // Default value for the property.
        "choices": ["option1", "option2"], // Choices for the property.
        "format": "string", // Format for the property (url, email, date, date-time, time, color).
        "mandatory": true, // Indicates if the property is mandatory.
        "specifics": {
          "min": 0, // Minimum value for the property.
          "max": 100 // Maximum value for the property.
        }
      }
    }
  },
  "external": false, // Indicates if the widget is external, i.e., if data is loaded from outside OpenBB API.
  "name": "string", // Name of the widget in the list the user sees. Displayed on top left of widget.
  "type": "string", // Main widget type (chart, table, note, custom).
  "description": "string", // Description to show to the user on the info button and on the search/add widget menu.
  "widgetId": "string", // Identifier for the specific widget instance. Used to map with openbb ui widgets.
  "data": {
    // Data configuration for the widget.
    "schemaData": {
      // Schema data for the widget.
      "key": "value"
    },
    "gridChart": {
      // Configuration for having a chart detached from aggrid table.
      "chartModel": "string", // The model of the aggrid chart.
      "fromTableId": "string" // Identifier for the source table of the chart data.
    },
    "values": [
      {
        // Array of x and y coordinate values.
        "x": 0,
        "y": 0
      }
    ],
    "mainTicker": {
      // Main ticker information. Displayed on top left after the widget name. Normally can be changed on this dropdown.
      "tickerProperty": "value"
    },
    "securities": ["security1", "security2"], // Array of security types.
    "secondaryTickers": ["ticker1", "ticker2"], // Array of secondary tickers.
    "hideControls": true, // Indicates if controls should be hidden.
    "color": "color", // Color configuration for the widget (used in Notes to store the color of the note).
    "html": "string", // HTML content to be displayed (used in Notes to save the note content).
    "dataKey": "string", // Key for the data.
    "table": {
      // Configuration for table columns.
      "columnState": {
        "key": "value"
      },
      "mode": "string", // Display mode for the table (light, dark).
      "density": "string", // Density mode for the table (compact, default).
      "transpose": true, // Indicates if the table should be transposed.
      "period": ["period1", "period2"], // Period information for the table.
      "showAll": true, // Indicates if all data should be shown.
      "columnsDefs": [
        {
          // Configuration for table columns.
          "field": "string", // Field name from the JSON data.
          "headerName": "string", // Header name for the column.
          "chartDataType": "string", // Chart data type (category, series, time, excluded).
          "cellDataType": "string", // Cell data type (text, number, boolean, date, dateString, object).
          "formatterFn": "string", // Formatter function (int, bigInt, etc.).
          "renderFn": "string", // Render function (green, red, titleCase, etc.).
          "width": 0, // Width of the column.
          "maxWidth": 0, // Maximum width of the column.
          "minWidth": 0, // Minimum width of the column.
          "hide": true, // Indicates if the column should be hidden.
          "rowGroup": true // Indicates if the column is a row group column.
        }
      ]
    },
    "chart": {
      // Chart instance that hits a callback for the JSON data.
      "callback": "string" // Callback function for the chart.
    }
  },
  "endpoint": "string", // Endpoint or endpoints for the widget data.
  "endpointMethod": "GET", // Endpoint method (GET, POST).
  "endpointHeaders": [
    {
      // Endpoint headers.
      "key": "string",
      "value": "string"
    }
  ],
  "params": {
    // URL params to send to the endpoint (e.g., callback endpoint in "analyst_upgrades_downgrades").
    "key": "value"
  },
  "options": {
    // Widget options.
    "size": "string", // Size configuration for the widget (normal, maximize).
    "chartType": "string", // Type of chart to display (line, candlestick, bar).
    "allowTickerChange": true, // Indicates if ticker change is allowed.
    "allowSecondaryTickersChange": true, // Indicates if secondary ticker change is allowed.
    "allowChartTypeChange": true, // Indicates if chart type change is allowed.
    "allowTimeframeChange": true, // Indicates if timeframe change is allowed.
    "allowRaw": true, // Indicates if raw data is allowed.
    "allowSettingsChange": true // Indicates if settings change is allowed.
  },
  "groupId": "string" // Identifier for a widget group.
}
```
