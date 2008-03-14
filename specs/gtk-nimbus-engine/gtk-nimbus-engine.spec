# $Id$
# Authority: hadams

%define real_name nimbus

Summary: Nimbus GTK2 engine
Name: gtk-nimbus-engine
Version: 0.0.12
Release: 1
License: GPL
Group: User Interface/X
URL: http://dlc.sun.com/osol/jds/downloads/extras/

Source: http://dlc.sun.com/osol/jds/downloads/extras/nimbus-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, automake, autoconf
BuildRequires: intltool >= 0.23
BuildRequires: gnome-common >= 1.2.4
BuildRequires: icon-naming-utils >= 0.8.1

%description
Nimbus is the default gtk engine from Open Solaris.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure.in
#configure \
./autogen.sh \
    --enable-animation \
    --enable-macmenu \
    --prefix="%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
#find_lang %{real_name}

%clean
%{__rm} -rf %{buildroot}

#files -f %{name}.lang
%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS
%{_datadir}/icons/nimbus/
%{_datadir}/themes/nimbus/
%{_libdir}/gtk-2.0/*/engines/libnimbus.so
%exclude %{_libdir}/gtk-2.0/*/engines/libnimbus.a
%exclude %{_libdir}/gtk-2.0/*/engines/libnimbus.la

%changelog
* Fri Mar 14 2008 Heiko Adams <info-2007 [at] fedora-blog [dot] de> 0.0.12-1
- update to 0.0.12

* Sat Nov 24 2007 Heiko Adams <info-2007 [at] fedora-blog [dot] de> 0.0.10-1
- update to 0.0.10

* Wed Nov 21 2007 Heiko Adams <info-2007 [at] fedora-blog [dot] de> 0.0.9-1
- update to 0.0.9

* Sun Sep 30 2007 Heiko Adams <info [at] fedora-blog [dot] de> - 0.0.8-1
- update to 0.0.8

* Wed Jun 27 2007 Heiko Adams <info@fedora-blog.de> - 0.0.6-1
- Initial build.
