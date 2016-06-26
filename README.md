# Install Dependencies

```
$ sudo apt install python3-pytest
$ pip3 install splinter
$ pip3 install pytest-splinter
$ pip3 install pytest-bdd
$ pip3 install pytest-xvfb  # optional, to avoid opening browser windows
```

# Run Plinth

*Warning*: Plinth-tester will change the configuration of the system
 under test, including changing the hostname and users. Therefore you
 should run the tests using Plinth running on a throw-away VM.

The VM should have NAT port-forwarding enabled so that 4430 on the
host forwards to 443 on the guest. Plinth should be accessible from
the host system at https://localhost:4430/.

# Setup Plinth

Create a new user as follows:

* Username: tester
* Password: tester

This step is optional if a fresh install of Plinth is being
tested. Plinth-tester will create the required user using Plinth's
first boot process.

# Run Plinth Tests

```
$ py.test-3
```

The full test suite can take a long time to run (over 15 minutes). You
can also specify which tests to run, by tag or keyword:

```
$ py.test-3 -k essential
```
