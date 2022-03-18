# CIS Benchmarking

These reports are from points in time and have notes with remediation and applicability for Flatcar Container Linux.
The CIS benchmarks are usually tailored to specific Linux distributions, as well as generic Linux hosts.
Flatcar Container Linux being a narrow use-case distribution causes many results to be not applicable.

## Report Generation

After some annoyance dealing with [ruby](https://www.ruby-lang.org/) and [inspec](https://www.inspec.io/downloads/), I was able to run the report. Documenting here what I did and what I got.

1. Installed inspec via gem: `gem install inspec-bin --user-install`
2. Cloned the benchmark repo: `git clone https://github.com/dev-sec/cis-dil-benchmark.git`
3. Started a [Flatcar QEMU image](https://www.flatcar.org/docs/latest/reference/developer-guides/sdk-modifying-flatcar/), copied the authorized keys to root.
4. Ran the test suite in the image, for level 1 and 2 (the default):

```shell
 ~/.gem/ruby/2.7.0/bin/inspec exec --no-color ./cis-dil-benchmark/ -t ssh://root@localhost:2222 --input=cis_level=1 > ../debug/inspec-report-level1.txt
 ~/.gem/ruby/2.7.0/bin/inspec exec --no-color ./cis-dil-benchmark/ -t ssh://root@localhost:2222 >  ../debug/inspec-report.txt
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

Here the too reports, and the corresponding notes we have produced:

* [2020-12-08 level1 report](./inspec-report-level1-root-2020-12-08.txt) -- [remediation notes](./level1-remediation_notes-2020-12-08.md)
* [2020-12-08 level2 report](./inspec-report-level2-root-2020-12-08.txt) -- _(no remediation notes yet)_
