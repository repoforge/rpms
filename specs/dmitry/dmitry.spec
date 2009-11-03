# $Id$
# Authority: dag

%define real_name DMitry

Summary: Deepmagic Information Gathering Tool
Name: dmitry
Version: 1.3a
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.mor-pah.net/

Source: http://mor-pah.net/code/DMitry-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Provides: DMitry = %{version}-%{release}
Obsoletes: DMitry <= %{version}-%{release}

%description
DMitry (Deepmagic Information Gathering Tool) is a UNIX/Linux command line 
program coded purely in C with the ability to gather as much information as 
possible about a host.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/dmitry.1*
%{_bindir}/dmitry

%changelog
* Wed Aug 22 2007 Dag Wieers <dag@wieers.com> - 1.3a-1
- Initial package. (using DAR)
