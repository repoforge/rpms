# $Id$
# Authority: dag


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Desktop session recorder with audio and video
Name: recordmydesktop
Version: 0.3.8.1
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://recordmydesktop.iovar.org/

Source: http://dl.sourceforge.net/recordmydesktop/recordmydesktop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: alsa-lib-devel
BuildRequires: libtheora-devel
BuildRequires: libvorbis-devel
BuildRequires: zlib-devel
%{!?_without_modxorg:BuildRequires: libSM-devel, libXdamage-devel, libXext-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
recordMyDesktop is a desktop session recorder for linux that attempts to be 
easy to use, yet also effective at it's primary task.

As such, the program is separated in two parts; a simple command line tool that
performs the basic tasks of capturing and encoding and an interface that 
exposes the program functionality in a usable way.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="%{__install} -c -p"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Jul 21 2009 Dag Wieers <dag@wieers.com> - 0.3.8.1-1
- Initial package. (using DAR)
