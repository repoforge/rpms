# $Id$
# Authority: hadams

Summary: Nimbus GTK2 engine
Name: gtk-nimbus-engine
Version: 0.0.16
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://dlc.sun.com/osol/jds/downloads/extras/
Source0: http://dlc.sun.com/osol/jds/downloads/extras/nimbus-%{version}.tar.bz2
BuildRequires: gtk2-devel
BuildRequires: intltool >= 0.23
BuildRequires: gnome-common >= 1.2.4
BuildRequires: icon-naming-utils >= 0.8.1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Nimbus is the default gtk engine from Open Solaris

%prep
%setup -q -n nimbus-%{version}

%build
./autogen.sh --enable-animation --enable-macmenu
#%configure --enable-animation --enable-macmenu
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#remove .la files
find $RPM_BUILD_ROOT -name *.la | xargs rm -f || true

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS COPYING
%{_libdir}/gtk-2.0/*/engines/*
%{_datadir}/*

%changelog
* Sat Jun 07 2008 Heiko Adams <info-2007 [at] fedora-blog [dot] de> 0.0.16-1
- update to 0.0.16

* Fri Mar 14 2008 Heiko Adams <info-2007 [at] fedora-blog [dot] de> 0.0.12-1
- update to 0.0.12

* Wed Feb 06 2008 Heiko Adams <info-2007 [at] fedora-blog [dot] de> 0.0.11-1
- update to 0.0.11

* Sat Nov 24 2007 Heiko Adams <info-2007 [at] fedora-blog [dot] de> 0.0.10-1
- update to 0.0.10

* Wed Nov 21 2007 Heiko Adams <info-2007 [at] fedora-blog [dot] de> 0.0.9-1
- update to 0.0.9

* Sun Sep 30 2007 Heiko Adams <info [at] fedora-blog [dot] de> 0.0.8-1
- update to 0.0.8

* Wed Jun 27 2007 Heiko Adams <info@fedora-blog.de> 0.0.6-1
- Initial build.

