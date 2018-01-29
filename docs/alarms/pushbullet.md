# Pushbullet

## Overview

* [Prerequisites](#prerequisites)
* [Introduction](#introduction)
* [Basic Config](#basic-config)
  * [Required Parameters](#required-parameters)
  * [Example: Basic Alarm Configuration using Required Parameters](#example-basic-alarm-configuration-using-required-parameters)
* [Advanced Config](#advanced-config)
  * [Optional Parameters](#optional-parameters)
  * [Example: Alarm Configuration Using Optional Parameters](#example-alarm-configuration-using-optional-parameters)
* [How to Get a Pushbullet API Key](#how-to-get-a-pushbullet-api-key)

## Prerequisites
This guide assumes:

1. You are familiar with [JSON formatting](https://www.w3schools.com/js/js_json_intro.asp)
2. You have read and understood the [Alarms](alarms) Wiki
3. You are comfortable with the layout of `alarms.json`.

Please familiarize yourself with all of the above before proceeding.

## Introduction

PokeAlarm offers the following for Pushbullet:

* Notifications to multiple Pushbullet channels
* Customizable Google Map image of the pokemon, gym, pokestop, egg and/or raid location
* Personalized notifications via [Dynamic Text Substitution](dynamic-text-substitution)

## Basic Config

### Required Parameters

These `alarm.json` parameters are required to enable the Pushbullet alarm service:

| Parameters     | Description                            |
|:-------------- |:---------------------------------------|
|`type`          | must be `pushbullet`                   |
|`active`        |`True` for alarm to be active           |
|`api_key`       | Your Pushbullet API key                |

### Example: Basic Alarm Configuration using Required Parameters

Below is how a basic Pushbullet alarm configuration would appear in `alarms.json`.

```json
{
	"active":"True",
	"type":"pushbullet",
	"api_key":"YOUR_API_KEY"
}
```

**Note:** The above code is to be inserted into the alarms section of
alarms.json. It does not represent the entire alarms.json file.

## Advanced Config

### Optional Parameters

In addition to the required parameters, several `alarm.json` optional
parameters are available to personalize your notifications.  Below is an
example of these optional parameters and how they are incorporated into a
functional alarm layout.


These optional parameters are entered at the same level as `"type":"pushbullet"`.

| Parameters         | Description                                                | Default                      |
|:-------------------|:-----------------------------------------------------------|:-----------------------------|
| `startup_message`  | Confirmation post when PokeAlarm initialized               | `True`                       |

These optional parameters below are applicable to the `pokemon`, `pokestop`, `gym`, `egg`, and `raid` sections of the JSON file.

| Parameters     | Description                                       | Default                                       |
|:-------------- |:--------------------------------------------------|:----------------------------------------------|
|`channel`       | Channel tag of the target channel                 | Sends to all devices                          |
|`title`         | Notification title  attached to the push          | `A wild <mon_name> has appeared!`             |
|`url`           | Link to be attached to the push                   | `<gmaps>`                                     |
|`body`          | Message attached to the push                       | `Available until <24h_time> (<time_left>).`  |

### Example: Alarm Configuration Using Optional Parameters

```json
{
    "active":"True",
    "type":"pushbullet",
    "api_key":"YOUR_API_KEY",
    "channel":"DEFAULT_CHANNEL",
    "pokemon":{
        "title":"A wild <mon_name> has appeared!",
        "url":"<gmaps>",
        "body":"Available until <24h_time> (<time_left>).",
        "channel":"OVERRIDES_DEFAULT_CHANNEL"
    },
    "pokestop":{
        "title":"Someone has placed a lure on a Pokestop!",
        "url":"<gmaps>",
        "body":"Lure will expire at <24h_time> (<time_left>).",
        "channel":"OVERRIDES_DEFAULT_CHANNEL"
    },
    "gym":{
        "title":"A Team <old_team> gym has fallen!",
        "url":"<gmaps>",
        "body":"It is now controlled by <new_team>.",
        "channel":"OVERRIDES_DEFAULT_CHANNEL"
    },
    "egg": {
        "title": "A level <egg_lvl> raid is incoming!",
        "url": "<gmaps>",
        "body": "The egg will hatch <24h_hatch_time> (<hatch_time_left>).",
        "channel":"OVERRIDES_DEFAULT_CHANNEL"
    },
    "raid": {
        "title": "Level <raid_lvl> raid is available against <mon_name>!",
        "url": "<gmaps>",
        "body": "The raid is available until <24h_raid_end> (<raid_time_left>)."
    }
}
```
**Note:** The above code is to be inserted into the alarms section of
alarms.json. It does not represent the entire alarms.json file.

## How to get a Pushbullet API Key

1. Go to [Pushbullet](https://www.pushbullet.com/) and click one of the 'Sign up' options.

2. In the top right corner, click on the letter and select 'My Account'.

3. Scroll down to 'Create Access Token`. Copy this token and place it in api_key parameter.
