lc3grade
========

lc3grade is a Python **3.5+** autograder for CS 2110 homeworks in LC-3
or C. After you run `SubmissionFix.py`, run it in the directory of
student submission subdirectories to run students' code against a set of
test cases defined in `lc3grade.config`. It saves tester output in each
student directory as `gradeLog.txt`.

There is a a backend named `LC-3` for running Brandon's lc3test and another
named `C` for running [libcheck][1] test cases. To enable a backend, uncommment
its section in `lc3grade.config`.

Building
--------

To build the [Python Zip Application][2], run

    make

Then you can run it with

    ./lc3grade

Getting Started
---------------

 1. Download a bulk submission for your section from T-Square, but *don't*
    extract it.
 2. Run `python SubmissionFix.py bulk_download.zip tsquare` to extract the bulk
    download.
 3. Copy `lc3grade` and `lc3grade.config` to the same directory.
 4. Copy your tests to the same directory and add them to `lc3grade.config`.
 5. Run `./lc3grade`, entering T-Square grades as you go. Each student directory
    contains tester output in `gradeLog.txt` if they want to see which tests
    they failed.

Grading with libcheck
---------------------

Grading with libcheck is a little more involved than lc3test because you have
to write unit tests in C. The `tests/` directory contains an example of how to
write them. Each libcheck test corresponds to a section in `lc3grade.config`.
In the case of the example in `tests/`, `lc3grade.config` could contain the
following sections (in addition to `[META]`):


    ; Configure the C backend
    [C]
    ; Use a big ol' timeout for the sake of slower VMs. Make this smaller to speed
    ; up grading if your students like writing infinite loops, but watch out for
    ; valgrind timeouts
    timeout=30
    cfiles=my_malloc.c
    tests_dir=tests
    build_cmd=make
    testcase_fmt=test_malloc_{category}_{test}
    run_cmd=./tests {test} {logfile}
    valgrind_cmd=valgrind --quiet --leak-check=full --error-exitcode=1 --show-leak-kinds=all --errors-for-leak-kinds=all ./tests {test} {logfile}

    [add]
    tests=positive,zero,negative
    weight=25

    [multiply]
    tests=positive,zero,negative
    weight=75

[1]: https://libcheck.github.io/check/
[2]: https://www.python.org/dev/peps/pep-0441/#improving-python-zip-application-support
