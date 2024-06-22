#!/bin/sh

. update.env
cd ..

dotnet clean
dotnet restore
dotnet format -v d
dotnet build --no-restore
dotnet test --no-build --verbosity normal
