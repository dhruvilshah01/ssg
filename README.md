Static Site Generator written using Python.

Unit tests can be run using the test.sh script.

To test locally use the main.sh script.

The build.sh script is used for deployments to github pages. This is why we specifically use "docs" as our
file path.

The website built using this SSG can be seen at https://dhruvilshah01.github.io/ssg/.

## Not supported

Markdown within markdown like: **bolded_italicedwithinbold__**. Here the "italicizedwithinbold" should be italicized
due to double underscore but that is not supported yet.
