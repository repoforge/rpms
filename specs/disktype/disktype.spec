# $Id$
# Authority: dag

Summary: Disk and disk image format analyzer
Name: disktype
Version: 9
Release: 1%{?dist}
License: MIT/X
Group: Applications/System
URL: http://disktype.sourceforge.net/

Source: http://dl.sf.net/disktype/disktype-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glibc-kernheaders

%description
The purpose of disktype is to detect the content format of a disk or
disk image. It knows about common file systems, partition tables, and
boot codes.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 disktype %{buildroot}%{_bindir}/disktype
%{__install} -Dp -m0644 disktype.1 %{buildroot}%{_mandir}/man1/disktype.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HISTORY LICENSE README TODO
%doc %{_mandir}/man1/disktype.1*
%{_bindir}/disktype

%changelog
* Thu Nov 01 2007 Dag Wieers <dag@wieers.com> - 9-1
- Initial package. (using DAR)
