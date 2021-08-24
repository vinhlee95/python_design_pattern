# Example of factory method pattern for integrations with external services

## Problem
Imagine our application has integration with different streaming service:
* Spotify
* Apple Music

We want to have a factory for each streaming service.
We also want to register and retrieve services easily.

## Specs
* Should have a factory builder for each service
* Should have a centralized place to register all services
* Should have a centralized place to create all services