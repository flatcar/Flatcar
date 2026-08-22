# CIS Benchmarking

These reports are from points in time and have notes with remediation and applicability for Flatcar Container Linux.
The CIS benchmarks are usually tailored to specific Linux distributions, as well as generic Linux hosts.
Flatcar Container Linux being a narrow use-case distribution causes many results to be not applicable.

## Report Generation

Running the CIS benchmark suite can be done either using Docker/Podman (recommended, no local Ruby installation required) or via a local Ruby/InSpec setup.

### Option A: Containerized Execution (Recommended)

1. Clone the benchmark repository:
   ```shell
   git clone https://github.com/dev-sec/cis-dil-benchmark.git
   ```
2. Start a [Flatcar QEMU image](https://www.flatcar.org/docs/latest/reference/developer-guides/sdk-modifying-flatcar/) and copy authorized SSH keys to root.
3. Run InSpec using Docker/Podman (connecting to the host QEMU SSH port `2222`):
   ```shell
   # Level 1 Benchmark Scan
   docker run -it --rm -v $(pwd):/share chef/inspec exec /share/cis-dil-benchmark \
     -t ssh://root@host.docker.internal:2222 --input=cis_level=1 > inspec-report-level1.txt

   # Level 2 Benchmark Scan
   docker run -it --rm -v $(pwd):/share chef/inspec exec /share/cis-dil-benchmark \
     -t ssh://root@host.docker.internal:2222 > inspec-report-level2.txt
   ```

### Option B: Local Ruby/InSpec Execution

1. Install InSpec via gem: `gem install inspec-bin --user-install`
2. Clone the benchmark repo: `git clone https://github.com/dev-sec/cis-dil-benchmark.git`
3. Start a [Flatcar QEMU image](https://www.flatcar.org/docs/latest/reference/developer-guides/sdk-modifying-flatcar/) and copy authorized SSH keys to root.
4. Run the test suite against QEMU:

```shell
 inspec exec --no-color ./cis-dil-benchmark/ -t ssh://root@localhost:2222 --input=cis_level=1 > inspec-report-level1.txt
 inspec exec --no-color ./cis-dil-benchmark/ -t ssh://root@localhost:2222 > inspec-report-level2.txt
```

Results:

Level 1:

```text
Profile Summary: 65 successful controls, 83 control failures, 82 controls skipped
Test Summary: 593 successful, 258 failures, 88 skipped
```

Level: 2

```text
Profile Summary: 68 successful controls, 118 control failures, 43 controls skipped
Test Summary: 606 successful, 344 failures, 50 skipped
```

I'm looking at the failures and many of them are rather arbitrary decisions, and we'll need to evaluate which ones we want to consider to adopt in Flatcar.  There's a bunch of filesystems that are recommended to be disabled, some of them, we might go ahead and disable (like hfs), others we actually need (like vfat).

But then there are things that should be fixed in the benchmark, because they fail because of our file-system layout. For example:

```text
     ×  File /etc/pam.d/common-password content is expected to match /^password(\s+\S+\s+)+pam_unix\.so\s+(\S+\s+)*sha512/
     expected nil to match /^password(\s+\S+\s+)+pam_unix\.so\s+(\S+\s+)*sha512/
```

## Reports

Here are the two reports, and the corresponding notes we have produced:

* [2020-12-08 level1 report](./inspec-report-level1-root-2020-12-08.txt) -- [remediation notes](./level1-remediation_notes-2020-12-08.md)
* [2020-12-08 level2 report](./inspec-report-level2-root-2020-12-08.txt) -- _(no remediation notes yet)_
