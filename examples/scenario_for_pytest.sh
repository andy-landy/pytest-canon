Let TEST_CMD be any command you use to run tests, like `python -m pytest tests`
Let COMMIT be command set to commit all added or modified dumps

# the first commit
PYTEST_UPDATE_REFS=1 TEST_CMD
COMMIT


# at later commits, after you updated some code

    # Option A, for manual or auto testing

        TEST_CMD
        ...inspect differences in failed tests...

        # once differences are considered valid
        PYTEST_UPDATE_REFS=1 TEST_CMD
        COMMIT


    # Option B, for manual testing

        PYTEST_UPDATE_REFS=1 pytest
        ...inspect differences by `git diff`...

        # once differences are considered valid
        COMMIT
