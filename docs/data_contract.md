# Core Data Contract

## ProductModel

This contract defines the normalized internal representation of product data.
All agents in the system must consume or produce data strictly adhering to this structure.

{
  "name": string,
  "active_concentration": number,
  "skin_type": [string],
  "ingredients": [string],
  "benefits": [string],
  "usage": string,
  "side_effects": string,
  "price_inr": number
}

