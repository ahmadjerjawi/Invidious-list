# Invidious Instance Checker

## Overview

The `check_invidious_instances.py` script is a tool designed to fetch, analyze, and categorize instances of the Invidious frontend for YouTube. Invidious is an alternative front-end to YouTube that provides enhanced privacy features and customization options. This script helps users find and monitor Invidious instances based on various metrics like uptime, API response success rate, and user activity.

## Purpose

YouTube’s official interface has limited flexibility and customization options, especially for users who prioritize privacy and performance. Invidious offers a more flexible front-end that can be customized to suit user needs. This script makes it easier to discover and keep track of the status of various Invidious instances, allowing users to choose the best instance based on real-time data.

## Features

- **Fetch and Analyze Invidious Instances**: Retrieves a list of Invidious instances from a central API.
- **Categorize Instances**: Sorts and categorizes instances based on metrics like uptime, API request success rates, and user activity.
- **Filter and Save**: Excludes specific types of URLs (e.g., `.onion`, `.i2p`) and saves relevant data into categorized text files.
- **Scheduled Updates**: Updates the data regularly using GitHub Actions to ensure the information remains current.

## How It Works

1. **Fetch Instances**: The script starts by retrieving a list of Invidious instances from the Invidious API.
2. **Filter URLs**: Excludes URLs that match unwanted patterns (e.g., `.onion`, `.i2p`).
3. **Categorize**: Sorts the instances based on various metrics such as uptime, API success ratio, and total user count.
4. **Save Data**: Outputs the categorized data into text files within an `output` directory. Each file represents a different category, such as most active users or best API success ratio.
