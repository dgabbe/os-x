#! /usr/bin/env bash
# reference: https://sourcegear.com/diffmerge/webhelp/sec__git__mac.html

echo ""
echo "git global configuration to use DiffMerge app..."
echo ""
git config --global diff.tool diffmerge
git config --global difftool.diffmerge.cmd \
    "/usr/local/bin/diffmerge \"\$LOCAL\" \"\$REMOTE\""

git config --global merge.tool diffmerge
git config --global mergetool.diffmerge.trustExitCode true
git config --global mergetool.diffmerge.cmd \
    "/usr/local/bin/diffmerge --merge --result=\"\$MERGED\" \
        \"\$LOCAL\" \"\$BASE\" \"\$REMOTE\""
