dnl MMX stuff
AC_DEFUN([AC_HAS_MMX],
[AC_MSG_CHECKING([for MMX (only works on linux)])
MMXBOOL=`grep mmx /proc/cpuinfo | wc -l`
if test -z MMXBOOL; then
	AC_MSG_RESULT([not mmx])
	$2
else
	AC_MSG_RESULT([mmx])
	$1
fi
])# AC_HAS_MMX
