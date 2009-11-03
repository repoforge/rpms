# $Id$
# Authority: matthias

%define prever b7

Summary: DVD authoring tool
Name: dvdstyler
Version: 1.5
Release: 0.1.%{prever}%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.dvdstyler.de/
Source: http://dl.sf.net/dvdstyler/DVDStyler-%{version}%{prever}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: dvdauthor
Requires: mjpegtools
Requires: netpbm-progs
Requires: mpgtx
Requires: mkisofs
Requires: dvd+rw-tools
BuildRequires: wxGTK-devel
BuildRequires: wxsvg-devel
BuildRequires: libgnomeui-devel
BuildRequires: gettext
BuildRequires: dvdauthor
BuildRequires: mjpegtools
BuildRequires: netpbm-progs
BuildRequires: mpgtx
BuildRequires: mkisofs
BuildRequires: dvd+rw-tools
BuildRequires: libjpeg-devel

%description
DVDStyler is a DVD authoring System.


%prep
%setup -n DVDStyler-%{version}%{prever}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} _doc
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}
# Put docs back where we'll include them nicely
%{__mv} %{buildroot}%{_datadir}/doc/dvdstyler _doc


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc _doc/*
%{_bindir}/dvdstyler
%{_datadir}/dvdstyler/


%changelog
* Fri Jan 19 2007 Matthias Saou <http://freshrpms.net/> 1.5-0.1.b7
- Initial RPM release.

