# $Id$
# Authority: dag

Summary: Tool to investigate deleted content on ext3 filesystem for recovery
Name: ext3grep
Version: 0.10.0
Release: 1
License: GPL
Group: Applications/File
URL: http://code.google.com/p/ext3grep/

Source: http://ext3grep.googlecode.com/files/ext3grep-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: e2fsprogs-devel
BuildRequires: gcc-c++

%description
ext3grep is a tool to investigate an ext3 filesystem for deleted content and
possibly recover it.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL LICENSE.GPL2 NEWS README
%{_bindir}/ext3grep

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 0.10.0-1
- Initial package. (using DAR)
