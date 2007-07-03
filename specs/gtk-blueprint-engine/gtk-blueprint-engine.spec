# $Id$
# Authority: hadams

Summary: Blueprint GTK2 engine
Name: gtk-blueprint-engine
Version: 0.9.18
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://dlc.sun.com/osol/jds/downloads/extras/
Source0: http://dlc.sun.com/osol/jds/downloads/extras/blueprint-%{version}.tar.bz2
BuildRequires: gtk2-devel
BuildRequires: intltool >= 0.23
BuildRequires: gnome-common >= 1.2.4
BuildRequires: icon-naming-utils >= 0.8.1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Blueprint is a gtk engine from Open Solaris

%prep
%setup -q -n blueprint-%{version}

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
* Wed Jun  27 2007 Heiko Adams <info@fedora-blog.de> 0.9.18-1
- Initial build.

