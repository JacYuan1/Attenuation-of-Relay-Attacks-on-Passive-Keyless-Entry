# Attenuation of Relay Attacks on Passive Keyless Entry

## About the Project

This capstone project is a culmination of our knowledge in the Cyber Security degree program at Sheridan College in which our goals are to enhance the security measures of Passive Keyless Entry (PKE) systems in vehicles. Inspired by Abel Valko's research paper, we have crafted an innovative solution blending both hardware and software to substantiate our security vision.

## Technical Background

While PKE systems offer unparalleled convenience, they are still susceptible to relay attacks that can bypass their encryption leading to unauthorized access. To address these vulnerabilities, our project emphasizes two key defense mechanisms:

- **Immobility Detection:** Leveraging an accelerometer connected to the Raspberry Pi, this method determines if the simulated key fob is stationary. Stationary states result in denied access requests, thwarting potential relay attacks.
  
- **Distance Bounding Protocols:** Incorporating a radio transceiver operating at 915 MHz with the Raspberry Pi, this approach gauges the actual physical distance between the simulated vehicle and key fob, ensuring the key is within a predefined range.

## Project Objectives

Our objectives encompass:
- Simulating the interplay between a vehicle and its key fob using Raspberry Pi.
- Provid a proof of concept solution primed for integration into real-world PKE systems to bolster security.

## Setup & Execution

For a detailed guide on project setup and execution, kindly refer to our [research paper](https://github.com/JacYuan1/Attenuation-of-Relay-Attacks-on-Passive-Keyless-Entry/blob/main/Capstone%20-%20Final%20Paper.pdf).

## Contributors

Other contributors to the project:

- [Cristian Di Bartolomeo](https://www.linkedin.com/in/dibarc/)
- [Luca Di Bartolomeo](https://www.linkedin.com/in/dibartolomeoluca/)
- [Renee Tyra Evangelista](https://www.linkedin.com/in/rtyraevangelista/)
- [Julian Lee](https://www.linkedin.com/in/julianlee1111/)

## References

- [Abel Valko's research paper](https://www.researchgate.net/publication/351761565_Relay_Attack_Resistant_Passive_Keyless_Entry_Securing_PKE_Systems_with_Immobility_Detection)
