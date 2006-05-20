# $Id$
# Authority: dries

Summary: Find the latest rpms by version in a tree
Name: novi
Version: 1.1.5
Release: 1
License: Apache License 2.0
Group: Applications/Utilities
URL: http://www.exmachinatech.net/01/novi/

Source: http://downloads.exmachinatech.net/novi/%{version}/novi-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: rpm-devel

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
%makeinstall INSTALL_BIN_DIR=%{buildroot}%{_bindir} INSTALL_BASE=%{buildroot}%{_prefix} INSTALL_MAN_DIR=%{buildroot}%{_mandir} INSTALL_MAN1_DIR=%{buildroot}%{_mandir}/man1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.TXT doc/*.html
%doc %{_mandir}/man1/novi*
%{_bindir}/novi

%changelog
* Sat May 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.5-1
- Initial package.
