# $Id$
# Authority: dag

Summary: Gaim plugin to block messages from certain contacts in a protocol-independent way
Name: gaim-blocky
Version: 0.1.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.desire.ch/tools/gaim-blocky.php/

Source: http://tools.desire.ch/data/gaim-blocky/files/gaim-blocky-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gaim-devel

%description
gaim-blocky is a gaim plugin to block messages from certain contacts in
a protocol-independent way.

%prep
%setup

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
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_libdir}/gaim/
%exclude %{_libdir}/gaim/libgaim-blocky.la
%{_libdir}/gaim/libgaim-blocky.so

%changelog
* Mon Mar 20 2006 Dag Wieers <dag@wieers.com> - 0.1.1-1
- Initial package. (using DAR)
