#!/bin/bash

# Get the list of installed packages
packages=$(pip list)

# Iterate over each package and uninstall it
for package in $packages; do
  # Extract the package name
  package_name=$(echo "$package" | awk '{print $1}')

  # Uninstall the package
  echo "Uninstalling $package_name..."
  sudo pip3 uninstall $package_name
done