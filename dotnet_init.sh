#!/bin/sh

rm allure-results/* -y

MAIN_PRJ_FILE=src/main/main.csproj
TEST_PRJ_FILE=src/test/test.csproj
TEST_PRJ_TMP_FILE=src/test/test.tmp

rm -f "${TEST_PRJ_FILE}"
rm -f src/test/Class1.cs
rm -f "${MAIN_PRJ_FILE}"
rm -f src/main/Class1.cs
rm -f testAlgo.sln

dotnet new sln --name testAlgo
dotnet new classlib --name main --framework net7.0 --output src/main
dotnet new classlib --name test --framework net7.0 --output src/test
dotnet sln add "${MAIN_PRJ_FILE}"
dotnet sln add "${TEST_PRJ_FILE}"
dotnet add "${TEST_PRJ_FILE}" reference "${MAIN_PRJ_FILE}"

rm -f src/test/Class1.cs
rm -f src/main/Class1.cs

dotnet add src/test package Microsoft.NET.Test.Sdk
dotnet add src/test package MSTest.TestFramework
dotnet add src/test package MSTest.TestAdapter
dotnet add src/test package xunit
dotnet add src/test package xunit.runner.visualstudio
dotnet add src/test package Allure.XUnit
dotnet add src/test package coverlet.collector
dotnet add src/test package NUnit
dotnet add src/test package NUnit3TestAdapter
dotnet add src/test package NUnit.Allure
dotnet add src/test package NUnit.Allure.Steps
dotnet add src/test package Allure.Commons
dotnet add src/test package NUnit.Analyzers

export PROJECT_TAG="</Project>"
export ITEM_GROUP="\n  <ItemGroup>\n    <Content Include=\"allureConfig.json\">\n      <CopyToOutputDirectory>Always</CopyToOutputDirectory>\n    </Content>\n  </ItemGroup>\n\n</Project>"

echo "============================="
echo "${ITEM_GROUP}"
echo "============================="
echo "${PROJECT_TAG}"

sed '$d' "${TEST_PRJ_FILE}"
tail -r "${TEST_PRJ_FILE}" | tail -n +3 | tail -r >"${TEST_PRJ_TMP_FILE}"
echo "${ITEM_GROUP}" >>"${TEST_PRJ_TMP_FILE}"
mv "${TEST_PRJ_TMP_FILE}" "${TEST_PRJ_FILE}"

dotnet clean
dotnet restore
dotnet build
dotnet test
