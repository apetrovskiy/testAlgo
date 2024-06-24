#!/bin/bash

FULL_RESTORE=1
# 0 - runs code operations without the Internet
# 1 - reloads packages

. ./update.env
cd ..

rm allure-results/* -y

SOLUTION_NAME=${PROJECT_NAME}
ROOT_FOLDER=src

MAIN_PRJ_NAME=main
MAIN_PRJ_FOLDER="${ROOT_FOLDER}/${MAIN_PRJ_NAME}"
# shellcheck disable=SC2001
MAIN_PRJ_FOLDER=$(echo "$MAIN_PRJ_FOLDER" | sed -e 's%\.%/%g')
echo "$MAIN_PRJ_FOLDER"
MAIN_PRJ_FILE="${MAIN_PRJ_FOLDER}/${MAIN_PRJ_NAME}.csproj"
MAIN_PRJ_TMP_FILE="${MAIN_PRJ_FOLDER}/main.tmp"

TEST_PRJ_NAME=test
TEST_PRJ_FOLDER="${ROOT_FOLDER}/${TEST_PRJ_NAME}"
# shellcheck disable=SC2001
TEST_PRJ_FOLDER=$(echo "$TEST_PRJ_FOLDER" | sed -e 's%\.%/%g')
echo "$TEST_PRJ_FOLDER"
TEST_PRJ_FILE="${TEST_PRJ_FOLDER}/${TEST_PRJ_NAME}.csproj"
TEST_PRJ_TMP_FILE="${TEST_PRJ_FOLDER}/test.tmp"

# the allure config item
ALLURE_CONFIG_FILE_NAME=allureConfig.json
ALLURE_CONFIG_FILE_PATH=${TEST_PRJ_FOLDER}/${ALLURE_CONFIG_FILE_NAME}
read -r -d '' ALLURE_CONFIG_CONTENT <<EOM
{
  "allure": {
    "directory": "../../../../../allure-results"
  }
}

EOM
read -r -d '' ALLURE_ITEM_GROUP <<EOM

  <ItemGroup>
    <Content Include="allureConfig.json">
      <CopyToOutputDirectory>Always</CopyToOutputDirectory>
    </Content>
  </ItemGroup>

EOM
# NLog
NLOG_CONFIG_FILE_NAME=NLog.config
NLOG_CONFIG_FILE_PATH=${MAIN_PRJ_FOLDER}/${NLOG_CONFIG_FILE_NAME}
read -r -d '' NLOG_CONFIG_CONTENT <<EOM
<?xml version="1.0" encoding="utf-8" ?>
<nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

    <targets>
        <target name="logfile" xsi:type="File" fileName="../../../../../../../../../testing.txt" />
        <target name="logconsole" xsi:type="Console" />
    </targets>

    <rules>
        <logger name="*" minlevel="Info" writeTo="logconsole" />
        <logger name="*" minlevel="Debug" writeTo="logfile" />
    </rules>
</nlog>

EOM
read -r -d '' NLOG_ITEM_GROUP <<EOM

  <ItemGroup>
    <Content Include="NLog.config">
      <CopyToOutputDirectory>Always</CopyToOutputDirectory>
    </Content>
  </ItemGroup>

EOM
# stylecop #
read -r -d '' STYLECOP_ITEM_GROUP <<EOM
  <ItemGroup>
      <AdditionalFiles Include="../stylecop.json" />
  </ItemGroup>
EOM
PROJECT_END_TAG="</Project>"

rm -f "${TEST_PRJ_FILE}"
rm -f "${TEST_PRJ_FOLDER}/Class1.cs"
rm -f "${MAIN_PRJ_FILE}"
rm -f "${MAIN_PRJ_FOLDER}/Class1.cs"
rm -f "${SOLUTION_NAME}.sln"

dotnet new sln --name "${SOLUTION_NAME}"
dotnet new classlib --name "${MAIN_PRJ_NAME}" --framework net8.0 --output "${MAIN_PRJ_FOLDER}"
dotnet new classlib --name "${TEST_PRJ_NAME}" --framework net8.0 --output "${TEST_PRJ_FOLDER}"
dotnet sln add "${MAIN_PRJ_FILE}"
dotnet sln add "${TEST_PRJ_FILE}"
dotnet add "${TEST_PRJ_FILE}" reference "${MAIN_PRJ_FILE}"

rm -f "${TEST_PRJ_FOLDER}/Class1.cs"
rm -f "${MAIN_PRJ_FOLDER}/Class1.cs"

# formatting
dotnet add "${MAIN_PRJ_FOLDER}" package Stylecop.Analyzers --prerelease
dotnet add "${TEST_PRJ_FOLDER}" package Stylecop.Analyzers --prerelease

# logging
dotnet add "${MAIN_PRJ_FOLDER}" package NLog --prerelease

# testing
dotnet add "${TEST_PRJ_FOLDER}" package Microsoft.NET.Test.Sdk --prerelease
dotnet add "${TEST_PRJ_FOLDER}" package coverlet.collector --prerelease
dotnet add "${TEST_PRJ_FOLDER}" package NUnit --prerelease
dotnet add "${TEST_PRJ_FOLDER}" package NUnit3TestAdapter --prerelease
dotnet add "${TEST_PRJ_FOLDER}" package xunit --prerelease
dotnet add "${TEST_PRJ_FOLDER}" package xunit.assert --prerelease
dotnet add "${TEST_PRJ_FOLDER}" package xunit.analyzers --prerelease
dotnet add "${TEST_PRJ_FOLDER}" package xunit.core --prerelease
# temporary
dotnet add "${TEST_PRJ_FOLDER}" package NUnit.Allure
# dotnet add "${TEST_PRJ_FOLDER}" package NUnit.Allure.Steps
dotnet add "${TEST_PRJ_FOLDER}" package Allure.Xunit --prerelease
dotnet add "${TEST_PRJ_FOLDER}" package Allure.Xunit.StepExtensions --prerelease
#
dotnet add "${TEST_PRJ_FOLDER}" package Allure.Commons --prerelease
dotnet add "${TEST_PRJ_FOLDER}" package NUnit.Analyzers --prerelease
#
dotnet add "${TEST_PRJ_FOLDER}" package FluentAssertions --prerelease

echo "${ALLURE_CONFIG_CONTENT}" >"${ALLURE_CONFIG_FILE_PATH}"
echo "${NLOG_CONFIG_CONTENT}" >"${NLOG_CONFIG_FILE_PATH}"

echo "============================="
cat "${ALLURE_CONFIG_FILE_PATH}"
echo "============================="
echo "${ALLURE_ITEM_GROUP}"
echo "============================="
cat "${NLOG_CONFIG_FILE_PATH}"
echo "============================="
echo "${NLOG_ITEM_GROUP}"
echo "============================="
echo "${STYLECOP_ITEM_GROUP}"
echo "============================="
echo "${PROJECT_END_TAG}"

# main prj
sed '$d' "${MAIN_PRJ_FILE}"
cat "${MAIN_PRJ_FILE}" >"${MAIN_PRJ_TMP_FILE}"
echo "sed -i -e \"s~${PROJECT_END_TAG}~~g\" \"${MAIN_PRJ_TMP_FILE}\""
sed -i -e "s~${PROJECT_END_TAG}~~g" "${MAIN_PRJ_TMP_FILE}"
{
  echo "${NLOG_ITEM_GROUP}"
  echo "${STYLECOP_ITEM_GROUP}"
  echo "${PROJECT_END_TAG}"
} >>"${MAIN_PRJ_TMP_FILE}"
mv "${MAIN_PRJ_TMP_FILE}" "${MAIN_PRJ_FILE}"

# test prj
sed '$d' "${TEST_PRJ_FILE}"
cat "${TEST_PRJ_FILE}" >"${TEST_PRJ_TMP_FILE}"
echo "sed -i -e \"s~${PROJECT_END_TAG}~~g\" \"${TEST_PRJ_TMP_FILE}\""
sed -i -e "s~${PROJECT_END_TAG}~~g" "${TEST_PRJ_TMP_FILE}"
{
  echo "${ALLURE_ITEM_GROUP}"
  echo "${STYLECOP_ITEM_GROUP}"
  echo "${PROJECT_END_TAG}"
} >>"${TEST_PRJ_TMP_FILE}"
mv "${TEST_PRJ_TMP_FILE}" "${TEST_PRJ_FILE}"

if [ "${FULL_RESTORE}" = 1 ]; then
  echo "cleanin... ==========="
  dotnet clean
  dotnet restore
fi
# install from here: dotnet tool install dotnet-format --version "7.*" --add-source https://pkgs.dev.azure.com/dnceng/public/_packaging/dotnet7/nuget/v3/index.json
# dotnet tool restore
dotnet format -v d
dotnet build --no-restore
dotnet test --no-build --verbosity normal
