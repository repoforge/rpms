# Authority: dag
# Upstream: <miros-discuss@mirbsd.org>

%define _bindir /bin

Name: mksh
Summary: MirBSD enhanced version of the Korn Shell
Version: 38b
Release: 1%{?dist}
License: BSD with advertising
Group: System Environment/Shells
URL: http://www.mirbsd.de/mksh/

Source0: http://www.mirbsd.org/MirOS/dist/mir/mksh/mksh-R%{version}.cpio.gz
Source1: http://www.mirbsd.org/MirOS/dist/hosted/other/arc4random.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ed
BuildRequires: util-linux
Requires: coreutils
Requires: grep

%description
mksh is the MirBSD enhanced version of the Public Domain Korn shell (pdksh),
a bourne-compatible shell which is largely similar to the original AT&T Korn
shell. It includes bug fixes and feature improvements in order to produce a
modern, robust shell good for interactive and especially script use, being a
bourne shell replacement, pdksh successor and an alternative to the C shell.

%prep
%setup -T -c

zcat %{SOURCE0} | cpio -imd
%{__mv} mksh/* .
%{__rm} -rf mksh
%{__cp} -f %{SOURCE1} .

%build
CFLAGS="%{optflags}" sh Build.sh -r -combine

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 mksh %{buildroot}%{_bindir}/mksh
%{__install} -Dp -m0644 mksh.1 %{buildroot}%{_mandir}/man1/mksh.1

%post
if ! grep -q "^%{_bindir}/mksh$" %{_sysconfdir}/shells; then
    echo "%{_bindir}/mksh" >>%{_sysconfdir}/shells
fi

%postun
if [ ! -x %{_bindir}/mksh ]; then
    sed -i -e '/^\/bin\/mksh$/d' %{_sysconfdir}/shells
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc dot.mkshrc
%doc %{_mandir}/man1/mksh.1*
%{_bindir}/mksh

%changelog
* Thu Jun 25 2009 Dag Wieers <dag@wieers.com> - 38b-1
- Initial package. (based on fedora)
