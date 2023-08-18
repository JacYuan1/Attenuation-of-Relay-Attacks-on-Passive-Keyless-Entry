# Attenuation of Relay Attacks on Passive Keyless Entry

## About the Project

This repository showcases the implementation of security enhancements for Passive Keyless Entry (PKE) systems in vehicles. Our work is inspired by the research paper "Relay Attack Resistant Passive Keyless Entry: Securing PKE Systems with Immobility Detection" by Abel Valko from the KTH Royal Institute of Technology. We employ the Raspberry Pi to simulate the interactions between a vehicle and its key fob.

## Technical Background

PKE systems, while offering unparalleled convenience, are susceptible to relay attacks that can bypass their encryption, leading to unauthorized access. To address these vulnerabilities, our project emphasizes two key defense mechanisms:

- **Immobility Detection:** Leveraging an accelerometer connected to the Raspberry Pi, this method determines if the simulated key fob is stationary. Stationary states result in denied access requests, thwarting potential relay attacks.
  
- **Distance Bounding Protocols:** Incorporating a radio transceiver operating at 915 MHz with the Raspberry Pi, this approach gauges the actual physical distance between the simulated vehicle and key fob, ensuring the key is within a predefined range.

## Project Objectives

Our objectives encompass:
- Simulating the interplay between a vehicle and its key fob using Raspberry Pi.
- Assessing the efficacy of Immobility Detection and Distance Bounding in countering relay attacks.
- Proposing a solution primed for integration into real-world PKE systems to bolster security.

## Setup & Execution

For a detailed guide on project setup and execution, kindly refer to our [research paper](link-to-installation-guide).

## Contributors

Other contributors to the project are the following:

-[Cristian Di Bartolomeo](https://www.linkedin.com/in/dibarc/)

-[Luca Di Bartolomeo](https://www.linkedin.com/in/dibartolomeoluca/)

-[Renee Tyra Evangelista](https://www.linkedin.com/in/rtyraevangelista/)

-[Julian Lee](https://www.linkedin.com/in/julianlee1111/)
