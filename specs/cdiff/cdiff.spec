# $Id$
# Authority: dag

Summary: Diff readability enhancer for color terminals
Name: cdiff
Version: 1.5
Release: 1%{?dist}
License: BSD
Group: Applications/Text
URL: http://www.freshports.org/textproc/cdiff/

#Source: ftp://ftp.FreeBSD.org/pub/FreeBSD/ports/i386/packages-stable/All/cdiff-%{version}.tgz
Source: ftp://ftp.freebsd.org/pub/FreeBSD/ports/i386/packages-4-stable/textproc/cdiff-%{version}.tgz
Patch0: cdiff-1.5-fetch-bzip2.patch
Patch1: cdiff-1.5-utf8.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.0
Requires: perl >= 1:5.6.0, less, gzip, bzip2

%description
cdiff is a readability enhancer for context and unified diffs on color
terminals.  It uses less(1) as a backend.

%prep
%setup -c
%patch0 -p1
%patch1 -p0

%{__mv} -f \+DESC README

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bin/cdiff %{buildroot}%{_bindir}/cdiff
%{__install} -Dp -m0644 man/man1/cdiff.1.gz %{buildroot}%{_mandir}/man1/cdiff.1.gz

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man1/cdiff.1*
%{_bindir}/cdiff

%changelog
* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Initial package. (using DAR)
