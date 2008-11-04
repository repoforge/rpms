# $Id$
# Authority: dag

Summary: Binary diff/patch utility
Name: bsdiff
Version: 4.3
Release: 1
License: BSD
Group: Development/Tools
URL: http://www.daemonology.net/bsdiff/

Source: http://www.daemonology.net/bsdiff/bsdiff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bzip2-devel

%description
bsdiff and bspatch are tools for building and applying patches to binary files.
By using suffix sorting (specifically, Larsson and Sadakane's qsufsort) and
taking advantage of how executable files change, bsdiff routinely produces
binary patches 50-80% smaller than those produced by Xdelta, and 15% smaller
than those produced by .RTPatch.

%prep
%setup

%build
%{__cc} %{optflags} -lbz2 -o bsdiff bsdiff.c
%{__cc} %{optflags} -lbz2 -o bspatch bspatch.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bsdiff %{buildroot}%{_bindir}/bsdiff
%{__install} -Dp -m0755 bspatch %{buildroot}%{_bindir}/bspatch
%{__install} -Dp -m0644 bsdiff.1 %{buildroot}%{_mandir}/man1/bsdiff.1
%{__install} -Dp -m0644 bspatch.1 %{buildroot}%{_mandir}/man1/bspatch.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/bsdiff.1*
%doc %{_mandir}/man1/bspatch.1*
%{_bindir}/bsdiff
%{_bindir}/bspatch

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 4.3-1
- Initial package. (using DAR)
