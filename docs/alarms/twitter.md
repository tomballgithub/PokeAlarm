# Twitter

## Overview

* [Prerequisites](#prerequisites)
* [Introduction](#introduction)
* [Basic Config](#basic-config)
  * [Required Parameters](#required-parameters)
  * [Example: Basic Alarm Configuration using Required Parameters](#example-basic-alarm-configuration-using-required-parameters)
* [Advanced Config](#advanced-config)
  * [Optional Parameters](#optional-parameters)
  * [Example: Alarm Configuration Using Optional Parameters](#example-alarm-configuration-using-optional-parameters)
* [How to Get a Twitter API Key](#how-to-get-a-twitter-api-key)

## Prerequisites

This guide assumes:

1. You are familiar with [JSON formatting](https://www.w3schools.com/js/js_json_intro.asp)
2. You have read and understood the [Alarms](alarms) Wiki
3. You are comfortable with the layout of `alarms.json`.

Please familiarize yourself with all of the above before proceeding.

## Introduction

**Twitter** is an online social networking service that enables users to send
and read short 140-character messages called "tweets". Registered users can
read and post tweets, but those who are unregistered can only read them. Users
access Twitter through the website interface, SMS or mobile device app.

PokeAlarm offers the following for Twitter:

* Personalized notifications via [Dynamic Text Substitution](dynamic-text-substitution)

## Basic Config

### Required Parameters

These `alarm.json` parameters are required to enable the Twitter alarm service:

| Parameters       | Description                            |
|:-----------------|:---------------------------------------|
| `type`           | must be `twitter`                      |
| `active`         |`True` for alarm to be active           |
| `access_token`   | Your twitter access token              |
| `access_secret`  | Your twitter access secret             |
| `consumer_key`   | Your twitter consumer key              |
| `consumer_secret`| Your twitter consumer secret           |

### Example: Basic Alarm Configuration using Required Parameters

```json
{
	"active": "False",
	"type": "twitter",
	"access_token": "YOUR_ACCESS_TOKEN",
	"access_secret": "YOUR_ACCESS_SECRET",
	"consumer_key": "YOUR_CONSUMER_KEY",
	"consumer_secret": "YOUR_CONSUMER_SECRET"
}
```
**Note:** The above code is to be inserted into the alarms section of
`alarms.json`. It does not represent the entire `alarms.json` file.

## Advanced Config

### Optional Parameters

In addition to the required parameters, several `alarm.json` optional
parameters are available to personalize your notifications. Below is an
example of these optional parameters and how they are incorporated into a
functional alarm layout.

These optional parameters are entered at the same level as `"type":"twitter"`.

| Parameters         | Description                                        | Default                      |
|:-------------------|:---------------------------------------------------|:-----------------------------|
| `startup_message`  | Confirmation post when PokeAlarm initialized       | `True`                       |

These optional parameters below are applicable to the `pokemon`, `pokestop`,
`gym`, `egg`, and `raid` sections of the JSON file.


| Parameters      | Description                          | Default                                       |
|:----------------|:-------------------------------------|:----------------------------------------------|
| `status`        | Message to post as status            | `A wild <mon_name> has appeared! Available until <24h_time> (<time_left>). <gmaps>` |

### Example: Alarm Configuration Using Optional Parameters

```json
{
    "active": "False",
    "type": "twitter",
    "access_token": "YOUR_ACCESS_TOKEN",
    "access_secret": "YOUR_ACCESS_SECRET",
    "consumer_key": "YOUR_CONSUMER_KEY",
    "consumer_secret": "YOUR_CONSUMER_SECRET",
    "pokemon":{
        "status": "A wild <mon_name> has appeared! Available until <24h_time> (<time_left>). <gmaps>"
    },
    "pokestop":{
        "status": "Someone has placed a lure on a Pokestop! Lure will expire at <24h_time> (<time_left>). <gmaps>"
    },
    "gym":{
        "status":"A Team <old_team> gym has fallen! It is now controlled by <new_team>. <gmaps>"
    },
    "egg": {
        "status": "Level <egg_lvl> raid incoming! Hatches at <24h_hatch_time> (<hatch_time_left>). <gmaps>"
    },
    "raid": {
        "status": "Raid <raid_lvl> against <mon_name>! Available until <24h_raid_end> (<raid_time_left>). <gmaps>"
    }
}
```
**Note:** The above code is to be inserted into the alarms section of
`alarms.json`. It does not represent the entire `alarms.json` file.

For more information on text substitutions, please see the main
configuration page.

## How to get a Twitter API Key

### Step 1: Create a Twitter account
* Go to [Twitter's signup page](https://twitter.com/signup)
* Fill out all details, and **make sure to include your phone number**.
This is a requirement for remote access, and you will need that to make
the Twitter bot work.

### Step 2: Create a Twitter app
* Go to [apps.twitter.com](https://apps.twitter.com)
* Click 'Create New App' button
* Fill out the details on the form. You have to give your app a name,
description, and website. This can be a simple place holder like http://www.example.com
* Read the Developer Agreement, and check the box at the bottom if you agree.
Then click on the ‘Create your Twitter application’ button.

### Step 3: Keys and Access tokens
* After creating your new app, you were redirected to its own page. If you
weren’t, go to [apps.twitter.com](https://apps.twitter.com) and click on your
apps name.
* On the app’s page, click on the ‘Keys and Access Tokens’ page.
* At the bottom of this page, click on the ‘Create my access token’ button.
* Take note of **Consumer Key (API Key), Consumer Secret (API Secret), Access
Token, & Access Token Secret**. These are the are required in the Twitter Config.
