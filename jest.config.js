    module.exports = {
        modulePaths: ["src/"],
        verbose: true,
        testPathIgnorePatterns: ["fixtures"],
        globals: {},
        setupFilesAfterEnv: ["jest-allure/dist/setup"],
        reporters: ["default", "jest-allure"],
    };