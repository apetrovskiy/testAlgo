/*
 * This file was generated by the Gradle 'init' task.
 *
 * This generated file contains a sample Java project to get you started.
 * For more details take a look at the Java Quickstart chapter in the Gradle
 * User Manual available at https://docs.gradle.org/6.6.1/userguide/tutorial_java_projects.html
 */

import io.qameta.allure.gradle.AllureExtension

val versions = mapOf(
    "gatling" to "3.5.1",
    "junit-jupiter" to "5.7.1",
    "junit-platform" to "1.7.1",
    "jackson" to "2.12.2",
    "snakeyaml" to "1.28",
    "jooq" to "3.14.8",
    "allure" to "2.13.9",
    "postgresql" to "42.2.19",
    "rest-assured" to "4.3.3",
    "hamcrest" to "2.2",
    "javafaker" to "1.0.2",
    "awaitility" to "4.0.3",
    "cucumber" to "6.8.1",
    "cucumber-junit" to "6.10.2",
    "allure" to "2.13.9",
    "allure-gradle" to "2.8.1",
    "java-version" to "16",
    "ktlint" to "0.41.0"
)

plugins {
    // Apply the java plugin to add support for Java
    java

    // Apply the java-library plugin for API and implementation separation.
    `java-library`

    // Apply the application plugin to add support for building a CLI application.
    application

    // Apply the org.jetbrains.kotlin.jvm Plugin to add support for Kotlin.
    // kotlin("multiplatform") version "1.4.10"
    kotlin("jvm") version "1.4.32"

    // Apply the scala Plugin to add support for Scala.
    scala

    // Apply the cpp-library plugin to add support for building C++ libraries
    // `cpp-library`

    // Apply the cpp-unit-test plugin to add support for building and running C++ test executables
    // `cpp-unit-test`

    // Apply the groovy Plugin to add support for Groovy.
    groovy

    // Apply the swift-library plugin to add support for building Swift libraries
    // `swift-library`

    // Apply the xctest plugin to add support for building and running Swift test executables (Linux) or bundles (macOS)
    // xctest

    id("io.qameta.allure") version "2.8.1"

    // checkstyle

    id("org.jlleitschuh.gradle.ktlint") version ("10.0.0")
}

/*
library {
    // Set the target operating system and architecture for this library
    targetMachines.add(machines.windows.x86_64)

    // Swift tool chain does not support Windows. The following targets macOS and Linux:
    targetMachines.add(machines.macOS.x86_64)

    targetMachines.add(machines.linux.x86_64)
}
*/

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(versions["java-version"]!!.toInt()))
    }
}

sourceSets.main {
    java.srcDirs("src/main/java", "src/main/kotlin", "src/main/scala", "src/main/groovy")
}

sourceSets.test {
    java.srcDirs("src/test/java", "src/test/kotlin", "src/test/scala", "src/test/groovy")
}

repositories {
    // Use jcenter for resolving dependencies.
    // You can declare any Maven/Ivy/file repository here.
    jcenter()
    mavenCentral()
    /*maven {
        url = uri("https://mvnrepository.com")
    }*/
}

dependencies {
    // https://mvnrepository.com/artifact/org.jetbrains.kotlin/kotlin-stdlib
    // implementation("org.jetbrains.kotlin:kotlin-stdlib:1.4.20")

    // Align versions of all Kotlin components
    implementation(platform("org.jetbrains.kotlin:kotlin-bom"))

    // Use the Kotlin JDK 8 standard library.
    implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8")

    implementation("org.clojure:clojure:1.10.2-alpha4")

    // Use Scala 2.13 in our library project
    implementation("org.scala-lang:scala-library:2.13.3")

    // This dependency is exported to consumers, that is to say found on their compile classpath.
    api("org.apache.commons:commons-math3:3.6.1")

    // This dependency is used by the application.
    // implementation("com.google.guava:guava:29.0-jre")
    // This dependency is used internally, and not exposed to consumers on their own compile classpath.
    implementation("com.google.guava:guava:29.0-jre")

    // Use the latest Groovy version for building this library
    implementation("org.codehaus.groovy:groovy-all:2.5.12")

    // https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter
    testImplementation("org.junit.jupiter:junit-jupiter:5.7.0")

    // Use JUnit Jupiter API for testing.
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.7.0")

    // Use JUnit Jupiter Engine for testing.
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine:5.7.0")
    // testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine")

    // https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter-params
    testImplementation("org.junit.jupiter:junit-jupiter-params:5.7.0")

    // https://mvnrepository.com/artifact/org.jetbrains.kotlin/kotlin-test
    // testImplementation("org.jetbrains.kotlin:kotlin-test:1.4.20")

    // Use the Kotlin test library.
    testImplementation("org.jetbrains.kotlin:kotlin-test")

    // Use the Kotlin JUnit integration.
    testImplementation("org.jetbrains.kotlin:kotlin-test-junit")

    testImplementation("org.junit.jupiter:junit-jupiter-api:${versions["junit-jupiter"]}")
    testImplementation("org.junit.jupiter:junit-jupiter-engine:${versions["junit-jupiter"]}")
    testImplementation("org.junit.jupiter:junit-jupiter-params:${versions["junit-jupiter"]}")
    testImplementation("org.junit.platform:junit-platform-launcher:${versions["junit-platform"]}")
    testImplementation("org.junit.platform:junit-platform-runner:${versions["junit-platform"]}")
    testImplementation("org.junit.platform:junit-platform-engine:${versions["junit-platform"]}")
    testImplementation("org.junit.platform:junit-platform-suite-api:${versions["junit-platform"]}")

    // https://mvnrepository.com/artifact/junit/junit
    // testImplementation("junit:junit:4.13.1")

    // Use the awesome Spock testing and specification framework even with Java
    testImplementation("org.spockframework:spock-core:1.3-groovy-2.5")
    // testImplementation("junit:junit:4.13")

    // Use Scalatest for testing our library
    // testImplementation("junit:junit:4.12")
    testImplementation("org.scalatest:scalatest_2.13:3.2.0")
    testImplementation("org.scalatestplus:junit-4-12_2.13:3.2.0.0")
    testImplementation("org.scalatest:scalatest-freespec_2.13:3.2.0")
    testImplementation("org.scalatest:scalatest-funsuite_2.13:3.2.0")

    // Need scala-xml at test runtime
    testRuntimeOnly("org.scala-lang.modules:scala-xml_2.13:1.2.0")

    testImplementation("io.qameta.allure:allure-java-commons:${versions["allure"]}")

    runtimeOnly("com.pinterest.ktlint:ktlint-core:${versions["ktlint"]}")
    runtimeOnly("com.pinterest.ktlint:ktlint-ruleset-standard:${versions["ktlint"]}")
    runtimeOnly("com.pinterest.ktlint:ktlint-reporter-plain:${versions["ktlint"]}")
}

/*application {
    // Define the main class for the application.
    // mainClassName = "testLeCo.App"
    mainClass.set("testLeCo.App")
}*/

configure<AllureExtension> {
    autoconfigure = true
    aspectjweaver = true
    version = versions["allure"]
    allureJavaVersion = versions["java-version"]

    clean = true

    resultsDir = file("../../allure-results")
    reportDir = file("../../allure-reports")

    useJUnit5 {
        version = versions["allure"]
    }
}

val test by tasks.getting(Test::class) {
    ignoreFailures = true
    // Use junit platform for unit tests
    useJUnitPlatform()
    testLogging.showStandardStreams = true
    systemProperty("junit.jupiter.execution.parallel.enabled", "true")
    systemProperty("junit.jupiter.execution.parallel.config.strategy", "dynamic")
    systemProperty("junit.jupiter.extensions.autodetection.enabled", "true")
    // systemProperty("allure.results.directory", "../../allure-results")
}

/*tasks.withType<Checkstyle>().configureEach {
    reports {
        xml.isEnabled = false
        html.isEnabled = true
        html.stylesheet = resources.text.fromFile("config/xsl/checkstyle-custom.xsl")
    }
}*/

tasks.named<Wrapper>("wrapper") {
    gradleVersion = "7.0"
    distributionType = Wrapper.DistributionType.ALL
}
