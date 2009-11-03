# $Id$
# Authority: hadams

%define real_name blueprint

Summary: Blueprint GTK2 engine
Name: gtk-blueprint-engine
Version: 0.9.20
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: http://dlc.sun.com/osol/jds/downloads/extras/

Source: http://dlc.sun.com/osol/jds/downloads/extras/blueprint-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel
BuildRequires: intltool >= 0.23
BuildRequires: gnome-common >= 1.2.4
BuildRequires: icon-naming-utils >= 0.8.1
BuildRequires: gettext

%description
Blueprint is a GTK engine from Open Solaris.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --enable-animation \
    --enable-macmenu
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{real_name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS
%{_datadir}/icons/blueprint/
%{_datadir}/themes/blueprint/
%{_datadir}/themes/blueprint-Green/
%{_datadir}/themes/blueprint-Ice/
%{_datadir}/themes/blueprint-Sand/
%{_libdir}/gtk-2.0/*/engines/libblueprint.so
%exclude %{_libdir}/gtk-2.0/*/engines/libblueprint.a
%exclude %{_libdir}/gtk-2.0/*/engines/libblueprint.la

%changelog
* Sun Sep 30 2007 Heiko Adams <info [at] fedora-blog [dot] de> - 0.9.20-1
- version update

* Wed Jun 27 2007 Heiko Adams <info@fedora-blog.de> - 0.9.18-1
- Initial build.
