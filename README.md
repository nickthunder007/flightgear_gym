# FlightGear Gym Environment for Reinforcement Learning

Welcome to the FlightGear Gym Environment repository! This project involves creating a custom reinforcement learning (RL) environment using the popular open-source flight simulator, FlightGear, with a focus on training RL agents to control military jets such as the F-15C Eagle. This environment is designed for tasks such as takeoff, flight maneuvering, and eventually, aerial dogfights.
Project Overview

This repository aims to create a flexible and scalable environment for training RL agents in flight simulations. Initially, the environment and reward is configured to train an F-15C Eagle taking off from the BIKF (Keflavík International Airport).

![Training Process](gifs/training.gif)

Key Features

    FlightGear Integration: Uses FlightGear for high-fidelity flight simulation.
    Custom Gym Environment: Based on OpenAI's Gym framework for seamless integration with RL algorithms.
    Modular Design: Easily extendable to add more aircraft models and airport locations.
    Future Plans: Extend the environment to support complex tasks such as dogfighting and aerial combat scenarios.

Prerequisites

    FlightGear: Download and install FlightGear from the official website.
    Python 3.x: Ensure you have Python 3.x installed on your system.
    FlightGear Python Bindings: Install the necessary Python bindings for FlightGear. (pip install flightgear-python)


FlightGear Configuration

    Aircraft: The current configuration uses the F-15C Eagle. Ensure this aircraft is installed in your FlightGear setup.
    Airport: The environment is currently configured for BIKF (Keflavík International Airport). You can change the airport code in the environment configuration.
    FlightGear Command: Run the following command to start FlightGear with the necessary settings:(fgfs --fg-aircraft=~/.fgfs/aircraft-data --aircraft=f15c --telnet=socket,bi,60,localhost,5500,tcp --geometry=480x480 --airport=BIKF)


Future Work
Adding More Jets and Airports

    Aircraft: Support for other fighter jets such as the F-22 Raptor, Su-27 Flanker, and MiG-29.
    Airports: Additional airports will be added, with different runway layouts and weather conditions.

Dogfight Training

    The environment will be extended to include dogfight scenarios, where agents are trained to engage in air-to-air combat.
    Reward structures will be designed for both offensive and defensive maneuvers.
    Advanced tasks like missile evasion, targeting, and aerobatics will be added.
