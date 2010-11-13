# $Id$
# Authority: dag

### EL6 ships with intltool-0.41.0-1.1.el6
### EL5 ships with intltool-0.35.0-2
### EL4 ships with intltool-0.31.2-1
### EL3 ships with intltool-0.26-1
%{?el3:# Tag: rfx}
# ExclusiveDist: el2 el3

Summary: Utility for internationalizing various kinds of data files
Name: intltool
Version: 0.28
Release: 0.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.gnome.org/

Source: http://ftp.gnome.org/pub/GNOME/sources/intltool/%{version}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: patch
Obsoletes: xml-i18n-tools
Provides: xml-i18n-tools = 0.11

%description
This tool automatically extracts translatable strings from oaf, glade,
bonobo ui, nautilus theme, .desktop, and other data files and puts
them in the po files.

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
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/intltool/
%{_datadir}/aclocal/*.m4

%changelog
* Sun Dec 21 2003 Dag Wieers <dag@wieers.com> - 0.28-0
- Initial package. (using DAR)
