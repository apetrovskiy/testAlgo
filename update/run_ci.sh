#!/bin/sh

. ./update.env
cd ..

dotnet clean
dotnet restore
dotnet format --verify-no-changes -v d
dotnet build --no-restore
dotnet test --no-build --verbosity normal