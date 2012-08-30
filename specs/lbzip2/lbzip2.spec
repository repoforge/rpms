# $Id: lbzip2.spec 8698 2010-03-22 00:06:50Z dag $
# Authority: dag

Summary: Fast, multi-threaded bzip2 utility
Name: lbzip2
Version: 2.2
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://lacos.hu/

Source: http://cloud.github.com/downloads/kjn/lbzip2/lbzip2-%{version}.tar.gz
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
%setup

%build
%configure
%{__make} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/lbzip2 %{buildroot}%{_bindir}/lbzip2
%{__ln_s} -f libzip2 %{buildroot}%{_bindir}/lbunzip2
%{__ln_s} -f libzip2 %{buildroot}%{_bindir}/lbzcat

%{__install} -Dp -m0644 man/lbzip2.1 %{buildroot}%{_mandir}/man1/lbzip2.1
%{__ln_s} -f lbzip2.1 %{buildroot}%{_mandir}/man1/lbunzip2.1
%{__ln_s} -f lbzip2.1 %{buildroot}%{_mandir}/man1/lbzcat.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL NEWS COPYING README
%doc %{_mandir}/man1/lbunzip2.1*
%doc %{_mandir}/man1/lbzcat.1*
%doc %{_mandir}/man1/lbzip2.1*
%{_bindir}/lbunzip2
%{_bindir}/lbzcat
%{_bindir}/lbzip2

%changelog
* Thu Aug 30 2012 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Thu Nov 24 2011 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Thu Mar 04 2010 Dag Wieers <dag@wieers.com> - 0.23-1
- Updated to release 0.23.

* Wed Feb 10 2010 Dag Wieers <dag@wieers.com> - 0.20-2
- Improvements to package metadata.
- Get rid of oldgcc patch.
- Added patches from upstream (Laszlo Ersek)

* Thu Dec 31 2009 Dag Wieers <dag@wieers.com> - 0.20-1
- Updated to release 0.20.

* Sat Dec 26 2009 Dag Wieers <dag@wieers.com> - 0.19-1
- Initial package. (using DAR)
