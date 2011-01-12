#!/usr/bin/env python
import commands
import datetime

date = datetime.date.today().strftime("%d %b %Y")
tag = commands.getoutput("git tag").split("\n")[-1]
log = commands.getoutput("git log --reverse --pretty=format:'- %%s' %s.. sources" % tag)
print "%s (Khaled Hosny) <XITS> Version %s" %(date, tag.replace("v", ""))
print log
print
