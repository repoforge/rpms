# $Id$
# Authority: dag

Summary: Fast, multi-threaded bzip2 utility
Name: lbzip2
Version: 0.20
Release: 2%{?dist}
License: GPL
Group: Applications/File
URL: http://lacos.hu/

Source: http://lacos.web.elte.hu/pub/lbzip2/lbzip2-%{version}.tar.gz
Patch0: Makefile.patch
Patch1: lfs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bzip2-devel

%description
lbzip2 is a multi-threaded implementation of bzip2, suited for serial and
parallel processing.  On a multi-core computer, lbzip2 is commonly the fastest
bzip2 decompressor for most bz2 files found on the internet.  (On dual-core
computers, the 7za utility from the p7zip package may prove more efficient.)

lbzip2 integrates nicely with GNU tar. Even on single-core computers, lbzip2
can speed up archiving in combination with tar, because lbzip2 allows
compression to overlap with disk usage to a greater extent than bzip2 does.

%prep
%setup -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 lbzip2 %{buildroot}%{_bindir}/lbzip2
%{__ln_s} -f libzip2 %{buildroot}%{_bindir}/lbunzip2
%{__ln_s} -f libzip2 %{buildroot}%{_bindir}/lbzcat

%{__install} -Dp -m0644 lbzip2.1 %{buildroot}%{_mandir}/man1/lbzip2.1
%{__ln_s} -f lbzip2.1 %{buildroot}%{_mandir}/man1/lbunzip2.1
%{__ln_s} -f lbzip2.1 %{buildroot}%{_mandir}/man1/lbzcat.1

%{__install} -Dp -m0644 malloc_trace.pl %{buildroot}%{_datadir}/lbzip2/malloc_trace.pl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog GPL-2.0 GPL-3.0 README
%doc %{_mandir}/man1/lbunzip2.1*
%doc %{_mandir}/man1/lbzcat.1*
%doc %{_mandir}/man1/lbzip2.1*
%{_bindir}/lbunzip2
%{_bindir}/lbzcat
%{_bindir}/lbzip2
%{_datadir}/lbzip2/malloc_trace.pl

%changelog
* Wed Feb 10 2010 Dag Wieers <dag@wieers.com> - 0.20-2
- Improvements to package metadata.
- Get rid of oldgcc patch.
- Added patches from upstream (Laszlo Ersek)

* Thu Dec 31 2009 Dag Wieers <dag@wieers.com> - 0.20-1
- Updated to release 0.20.

* Sat Dec 26 2009 Dag Wieers <dag@wieers.com> - 0.19-1
- Initial package. (using DAR)
