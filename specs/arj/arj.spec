# $Id$
# Authority: dag

Summary: Archiver for .arj files
Name: arj
Version: 3.10.22
Release: 2%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://arj.sourceforge.net/

Source0: http://dl.sf.net/sourceforge/arj/arj-%{version}.tar.gz
Source1: unarj.sh
Source2: unarj.1
Patch0: http://ftp.debian.org/debian/pool/main/a/arj/arj_%{version}-2.diff.gz
Patch1: arj-3.10.22-private_strnlen.patch
Patch2: arj-3.10.22-quotes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf >= 2.53
Provides: unarj = %{version}-%{release}
Obsoletes: unarj < 3

%description
This package is an open source version of the arj archiver.  This
version has been created with the intent to preserve maximum
compatibility and retain the feature set of original ARJ archiver as
provided by ARJ Software, Inc.

%prep
%setup
%patch0 -p1
for i in debian/patches/00*.patch; do
    patch -p1 < $i
done
%patch1 -p1
%patch2 -p1

%build
pushd gnu
    autoconf
    %configure
popd
%{__make} ADD_LDFLAGS=""

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0644 resource/rearj.cfg.example %{buildroot}%{_sysconfdir}/rearj.cfg
%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_bindir}/unarj
%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/unarj.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog* doc/COPYING doc/rev_hist.txt
%doc %{_mandir}/man1/arj.1*
%doc %{_mandir}/man1/arjdisp.1*
%doc %{_mandir}/man1/rearj.1*
%doc %{_mandir}/man1/unarj.1*
%config(noreplace) %{_sysconfdir}/rearj.cfg
%{_bindir}/arj
%{_bindir}/arjdisp
%{_bindir}/rearj
%{_bindir}/unarj
%{_libdir}/arj/
%exclude %{_mandir}/man1/arj-register.1*
%exclude %{_bindir}/arj-register

%changelog
* Fri Apr 13 2012 Tom G. Christensen <jrpms@jupiterrise.com> - 3.10.22-2
- Make sure that private strnlen is used when CUSTOM_PRINTF is defined

* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 3.10.22-1
- Initial package. (using DAR)
