# $Id$
# Authority: dag

Summary: Extract headers from rpm in a old yum repository
Name: yum-arch
Version: 2.2.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL:  http://linux.duke.edu/yum/

Source: http://linux.duke.edu/projects/yum/download/2.2/yum-%{version}.tar.gz
Patch0: yum-arch-2.2.2-folder.patch
Patch1: yum-arch-2.2.2-unwarn.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gettext
BuildRequires: python
Requires: libxml2-python
Requires: python
Requires: rpm >= 0:4.1.1
Requires: rpm-python

%description
Extract headers from rpm in a old yum repository.

This package only provides the old yum-arch command from yum-%{version}
It should be used to generate repository informations for Fedora Core  < 3
and RedHat Enterprise Linux < 4.

%prep
%setup -n yum-%{version}
%patch0 -p0 -b .folder
%patch1 -p1 -b .unwarn

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man8/yum-arch.8*
%{_datadir}/yum-arch/
%{_bindir}/yum-arch

%changelog
* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Initial package. (based on Fedora)
