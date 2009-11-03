# $Id$
# Authority: dag
# Upstream: Ian Macdonald <ian$caliban,org>

%define real_name bash_completion

Summary: Programmable completion for Bash
Name: bash-completion
Version: 20060301
Release: 1%{?dist}
License: GPL
Group: System Environment/Shells
URL: http://www.caliban.org/bash/

Source: http://www.caliban.org/files/bash/bash-completion-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: bash >= 2.05-12, grep, textutils, sed, fileutils

%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash 2.04 and later.

%prep
%setup -n %{real_name}

### FIXME: Remove this line the next release !
%{__perl} -pi.orig -e 's|_comp-dpkg-hold-packages|_comp_dpkg_hold_packages|g' bash_completion

### FIXME: TODO: Make this script work with other shells too !!
%{__cat} <<'EOF' >bash_completion.sh
#!/bin/sh

### Check for Bash
if [ -z "$BASH_VERSION" ]; then
	return
fi

### Check for correct version of Bash (use \< instead of -lt because of 2.05b)
if [ \( "${BASH_VERSINFO[0]}" -eq 2 -a "${BASH_VERSINFO[1]}" \< 05 \) -o "${BASH_VERSINFO[0]}" -lt 2 ]; then
	return
fi

### Source Bash completions
if [ -r "%{_sysconfdir}/bash_completion" ]; then
	source "%{_sysconfdir}/bash_completion"
fi
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bash_completion %{buildroot}%{_sysconfdir}/bash_completion
%{__install} -Dp -m0755 bash_completion.sh %{buildroot}%{_sysconfdir}/profile.d/bash_completion.sh
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/bash_completion.d/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS Changelog contrib/ COPYING README
%config %{_sysconfdir}/bash_completion
%config %{_sysconfdir}/profile.d/*
%config %{_sysconfdir}/bash_completion.d/

%changelog
* Mon Dec 18 2006 Dag Wieers <dag@wieers.com> - 20060301-1
- Updated to release 20060301.

* Sat Jul 23 2005 Dag Wieers <dag@wieers.com> - 20050721-1
- Updated to release 20050721.

* Wed Jul 20 2005 Dag Wieers <dag@wieers.com> - 20050720-1
- Updated to release 20050720.

* Wed Jul 13 2005 Dag Wieers <dag@wieers.com> - 20050712-1
- Updated to release 20050712.

* Sat Jan 22 2005 Dag Wieers <dag@wieers.com> - 20050121-1
- Updated to release 20050121.

* Fri Jan 21 2005 Dag Wieers <dag@wieers.com> - 20050120-1
- Updated to release 20050120.

* Sun Jan 16 2005 Dag Wieers <dag@wieers.com> - 20050112-1
- Updated to release 20050112.

* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 20050103-1
- Updated to release 20050103.

* Mon Nov 29 2004 Dag Wieers <dag@wieers.com> - 20041017-3
- Reverted wrong change to Bash version check. (Juergen Moellenhoff)

* Tue Nov 23 2004 Dag Wieers <dag@wieers.com> - 20041017-2
- Correct version check for Bash 3. (Matteo Corti)

* Sun Nov 21 2004 Dag Wieers <dag@wieers.com> - 20041017-1
- Updated to release 20041017.

* Sun Jul 11 2004 Dag Wieers <dag@wieers.com> - 20040711-1
- Updated to release 20040711.

* Sun Jul 04 2004 Dag Wieers <dag@wieers.com> - 20040704-1
- Updated to release 20040704.

* Thu May 27 2004 Dag Wieers <dag@wieers.com> - 20040526-1
- Updated to release 20040526.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 20040331-1
- Updated to release 20040331.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 20040214-1
- Fix for bash-completion problem with gdm. (Rudolf Kastl)

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 20040214-0
- Updated to release 20040214.

* Wed Feb 11 2004 Dag Wieers <dag@wieers.com> - 20040210-0
- Updated to release 20040210.

* Fri Jan 02 2004 Dag Wieers <dag@wieers.com> - 20040101-0
- Updated to release 20040101.

* Mon Dec 15 2003 Dag Wieers <dag@wieers.com> - 20031215-0
- Updated to release 20031215.

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 20031112-0
- Updated to release 20031112.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 20031022-0
- Updated to release 20031022.

* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 20030803-0
- Updated to release 20030803.

* Mon Jul 21 2003 Dag Wieers <dag@wieers.com> - 20030721-0
- Updated to release 20030721.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 20030713-0
- Fixed a problem with bash_completion.sh.
- Updated to release 20030713.

* Sun Jun 08 2003 Dag Wieers <dag@wieers.com> - 20030607-0
- Updated to release 20030607.

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 20030527-0
- Updated to release 20030527.

* Mon May 05 2003 Dag Wieers <dag@wieers.com> - 20030505-0
- Updated to release 20030505.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.06.20030501-0
- Updated to release 20030501.

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 0.06.20030419-0
- Initial package. (using DAR)
