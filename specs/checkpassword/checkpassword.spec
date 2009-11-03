# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Provides a simple, uniform password-checking interface
Name: checkpassword
Version: 0.90
Release: 2.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://cr.yp.to/checkpwd.html

Source: http://cr.yp.to/checkpwd/checkpassword-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
checkpassword provides a simple, uniform password-checking interface
to all root applications. It is suitable for use by applications such
as login, ftpd, and pop3d.

There are checkpassword-compatible tools that support alternate
password databases, secret login names, long passwords, subaccounts,
one-time passwords, detailed accounting, and many other features.

Applications that use the checkpassword interface will work with all
of these tools. Several tools have been specifically designed to
support POP toasters.

%prep
%setup

### FIXME: Fix the errno problem on RH9, RHEL3 and RHFC1
%{__perl} -pi.orig -e 's|^(#include "error.h")$|$1\n#include <errno.h>|' *.c

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 checkpassword %{buildroot}%{_bindir}/checkpassword

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES FILES README SYSDEPS TARGETS TODO VERSION
%{_bindir}/checkpassword

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.90-2.2
- Rebuild for Fedora Core 5.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.90-2
- Fixed a problem with _bindir.

* Thu Oct 04 2001 Dag Wieers <dag@wieers.com> - 0.90-1
- Initial package.
