;; Git VC backend
(add-to-list 'vc-handled-backends 'GIT t)
(autoload 'git-status "git" "GIT mode." t)
(autoload 'git-blame-mode "git-blame"
 	"Minor mode for incremental blame for Git." t)
