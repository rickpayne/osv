#!/bin/sh

GITDIR=$(dirname $0)/../.git
echo `git --git-dir $GITDIR describe --tags --match 'v[0-9]*'`-rebar3
