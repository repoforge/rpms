# $Id$

# Authority: dag
# Upstream: Ian Macdonald <ian@caliban.org>

%define rname bash_completion

Summary: Programmable completion for Bash
Name: bash-completion
Version: 20040214
Release: 1
License: GPL
Group: System Environment/Shells
URL: http://www.caliban.org/bash/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.caliban.org/files/bash/bash-completion-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
Requires: bash >= 2.05-12, grep, textutils, sed, fileutils

%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash 2.04 and later.

%prep
%setup -n %{rname}

### TODO: Remove this line the next release !
%{__perl} -pi -e 's|_comp-dpkg-hold-packages|_comp_dpkg_hold_packages|g' bash_completion

### FIXME: Make this script work with other shells too !!
%{__cat} <<'EOF' >bash_completion.sh
#!/bin/sh

### Check for Bash
if [ -z "$BASH_VERSION" ]; then
	return
fi

### Check for correct version of Bash
if [ "${BASH_VERSINFO[0]}" -ne 2 -o "${BASH_VERSINFO[1]}" \< 05 ]; then
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
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/profile.d \
			%{buildroot}%{_sysconfdir}/bash_completion.d
%{__install} -m0755 bash_completion %{buildroot}%{_sysconfdir}
%{__install} -m0755 bash_completion.sh %{buildroot}%{_sysconfdir}/profile.d/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS Changelog COPYING README contrib/
%config %{_sysconfdir}/bash_completion
%config %{_sysconfdir}/bash_completion.d/
%config %{_sysconfdir}/profile.d/*

%changelog
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
