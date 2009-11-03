# $Id$
# Authority: dag

# ExclusiveDist: el5

Summary: Useful things common to building gnome packages
Name: gnome-common
Version: 2.12.0
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://developer.gnome.org/

Source: http://ftp.gnome.org/pub/GNOME/sources/gnome-common/2.12/gnome-common-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig

%description
This package contains sample files that should be used to develop pretty much
every GNOME application.

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README doc/*.txt
%{_bindir}/gnome-autogen.sh
%{_bindir}/gnome-doc-common
%dir %{_datadir}/aclocal/
%{_datadir}/aclocal/gnome-common.m4
%{_datadir}/aclocal/gnome-compiler-flags.m4
%{_datadir}/gnome-common/

%changelog
* Thu Mar 13 2008 Dag Wieers <dag@wieers.com> - 2.12.0-1
- Updated to release 2.12.0.

* Tue Feb 25 2003 Dag Wieers <dag@wieers.com> - 1.2.4-0
- Initial package. (using DAR)
