# github-green-box

This python script can submit your GitHub block to fake all green.

## Usage

Be careful, you need create a new folder and initialization git, then run script in floder.

The script create log.txt file and write it when you commit.

```shell
python github-green-box.py
```
You can run that python script and start a loop.
```
Please enter you want to commit date (like 20190902): 20190813
Please enter the number of times you want to commit, it must be a number value: 3
[master 1b60f7f] Update 2019-08-13T19:49:10.
 Date: Tue Aug 13 19:49:10 2019 +0800
 1 file changed, 1 insertion(+)
[master 6ad6bf6] Update 2019-08-13T22:33:00.
 Date: Tue Aug 13 22:33:00 2019 +0800
 1 file changed, 1 insertion(+)
[master bcc06d0] Update 2019-08-13T04:00:12.
 Date: Tue Aug 13 04:00:12 2019 +0800
 1 file changed, 1 insertion(+)
```

- First you should enter you want change day at console.
- The second step is to enter the number of commit you want.
- Last step just push it to your GitHub cloud repository.

**This script can change your previous commit records, If you want to restore, you can delete this repository.**

**I hope it's just for entertainment, We should use it correctly !**
