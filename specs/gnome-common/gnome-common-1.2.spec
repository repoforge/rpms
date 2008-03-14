# $Id: gnome-common.spec 4303 2006-04-18 22:05:03Z dries $
# Authority: dag

# ExclusiveDist: el2 rh7 rh9 el3

Summary: Useful things common to building gnome packages
Name: gnome-common
Version: 1.2.4
Release: 1
License: GPL
Group: Development/Tools
URL: http://ftp.gnome.org/pub/GNOME/sources/gnome-common/

Source: http://ftp.gnome.org/pub/GNOME/sources/gnome-common/1.2/gnome-common-%{version}.tar.bz2
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
%{_bindir}/gnome-autogen.sh
%dir %{_datadir}/aclocal/
%{_datadir}/aclocal/gnome-macros/
%{_datadir}/aclocal/gnome2-macros/

%changelog
* Tue Feb 25 2003 Dag Wieers <dag@wieers.com> - 1.2.4-1
- Improved SPEC file.

* Tue Feb 25 2003 Dag Wieers <dag@wieers.com> - 1.2.4-0
- Initial package. (using DAR)
