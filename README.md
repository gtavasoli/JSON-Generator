# JSON Generator
JSON Generator has a simple and convenient syntax. JSON Generator allowing users to generate fake data based on a template. It has been designed for simplicity. For this reason we do not follow JSON schema standard! 

[![Website gtavasoli.com](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://gtavasoli.com/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://t.me/gtavasoli_me)

## Table of Contents
- [Usage](#usage)

## Usage
Using of JSON Generator is straightforward. First, you must define your JSON template by our simple API. This template is in JSON format. Then, you must call generate function with your JSON template as input. Generate function makes a random JSON object based on your JSON template as the return value. 

For your convenience, we provide a script (main.py) that load template from file and generate random JSON object. There is multiple template file in this repository.

## API

| Name | Description | Usage | Params | Returns |
| --- | --- | --- | --- | --- |
| bool | Random boolean | ```{{bool}}``` | | Boolean |
| city | Random city name | ```{{city}}``` | | String |
| company | Random company name | ```{{company}}``` | | String |
| country | Random country name | ```{{country}}``` | | String |
| first_name | Random first name | ```{{first_name}}``` | | String |
| floating | Random float number in specified range. | ```{{floating([min], [max])}}``` | ```min``` Minimum number of in the range, ```max``` Maximum number in the range | Float |


## ToDo
- Date function
- Time Zone
- Gender for first name
- Format for floating

## LICENSE
All of the codebase are MIT licensed unless otherwise specified. 

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)