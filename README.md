# LibreTime RaBe Development Fork

Hello, you have found the [Radio Bern RaBe](http://rabe.ch) development fork of [LibreTime](http://libretime.org).

Please refer to the main repository at [LibreTime/libretime](https://github.com/LibreTime/libretime) for more
information and if you wish to contribute to LibreTime.

This repository contains branches that are being prepared to PR into the main repo. See what we are working on
at the [list of feature branches](https://github.com/radiorabe/libretime/branches/all?utf8=%E2%9C%93&query=feature).

Feel free to comment on the main LibreTime repo it you would like us to prioritize any of those branches and
we will look what we can do.

This README.md is on the orphan branch `rabe` in this fork. Any changes to the branch will never get merged to upstream.

This fork does not have a `master` branch you want to clone upstream and then add this as remote:

```bash
git clone -b master -o upstream --depth=1  git@github.com:LibreTime/libretime.git
cd libretime
git remote add origin git@github.com:radiorabe/libretime.git
git fetch origin
```

This also creates a shallow clone only containing the last 100 refs, that way the initial clone is much faster. If you ever want the complete history locally, you need to unshallow your working copy:

```bash
git fetch --unshallow
```
