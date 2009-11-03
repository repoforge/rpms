# $Id$

# Authority: dag
# Upstream: Marcus Schneider <marcus,schneider$gmx,net>

Summary: Realtime Video4Linux recording software
Name: v4lgrab
Version: 0.2.2
Release: 0.2%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://v4lgrab.sourceforge.net/

Source: http://dl.sf.net/v4lgrab/v4lgrab-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libjpeg-devel, libtool, kdelibs-devel, arts-devel
BuildRequires: avifile-devel, SDL-devel

%description
This project is a realtime Video4Linux recording software. It makes it
possible to record AVI DivX files in realtime from any Video4Linux device.

%prep
%setup

%build
%configure \
	--with-xinerama
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README THANKS VERSION docs/*.doxygen
%config %{_sysconfdir}/v4lgrab/
%{_bindir}/*
%{_libdir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.2-0.2
- Rebuild for Fedora Core 5.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 0.2.2
- Initial package. (using DAR)
