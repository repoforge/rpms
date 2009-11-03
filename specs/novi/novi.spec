# $Id$
# Authority: dries

Summary: Find the latest rpms by version in a tree
Name: novi
Version: 1.1.5
Release: 2%{?dist}
License: Apache License 2.0
Group: Applications/System
URL: http://www.exmachinatech.net/01/novi/

Source: http://downloads.exmachinatech.net/novi/%{version}/novi-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: rpm-devel, gcc-c++

%description
novi is a tool for finding the latest-version RPMs in a tree. It can be used 
to create Kickstart trees or yum repositories that contain the updated RPMS. 
In the case of Kickstart, this means machines come to life with the updates 
already applied. Using novi for a yum repository trims the size of the 
repodata files, which reduces client download and processing time.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install ALT_ROOT_DIR="%{buildroot}" INSTALL_MAN_DIR="%{buildroot}%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE* *.TXT doc/*.html
%doc %{_mandir}/man1/novi.1*
%doc %{_mandir}/man1/novi_examples.1*
%{_bindir}/novi

%changelog
* Fri Mar 09 2007 Dag Wieers <dag@wieers.com> - 1.1.5-2
- Fixed group.

* Sat May 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.5-1
- Initial package.
