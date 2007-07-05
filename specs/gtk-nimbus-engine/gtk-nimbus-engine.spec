# $Id$
# Authority: hadams

%define real_name nimbus

Summary: Nimbus GTK2 engine
Name: gtk-nimbus-engine
Version: 0.0.6
Release: 1
License: GPL
Group: User Interface/X
URL: http://dlc.sun.com/osol/jds/downloads/extras/

Source: http://dlc.sun.com/osol/jds/downloads/extras/nimbus-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel
BuildRequires: intltool >= 0.23
BuildRequires: gnome-common >= 1.2.4
BuildRequires: icon-naming-utils >= 0.8.1

%description
Nimbus is the default gtk engine from Open Solaris.

%prep
%setup -n %{real_name}-%{version}

%build
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
* Wed Jun 27 2007 Heiko Adams <info@fedora-blog.de> - 0.0.6-1
- Initial build.
