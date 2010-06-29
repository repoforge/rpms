# $Id$
# Authority: dag

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Fast command line image viewer using Imlib2
Name: feh
Version: 1.8
Release: 1%{?dist}
License: MIT
Group: Applications/Multimedia
URL: http://linuxbrit.co.uk/feh/

Source: https://derf.homelinux.org/projects/feh/feh-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: giblib-devel
BuildRequires: imlib2-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
%{!?_without_modxorg:BuildRequires: libXt-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
feh is a versatile and fast image viewer using imlib2, the
premier image file handling library. feh has many features,
from simple single file viewing, to multiple file modes using
a slideshow or multiple windows. feh supports the creation of
montages as index prints with many user-configurable options.

%prep
%setup

%{__perl} -pi.orig -e 's|-Wextra||g' config.mk

%build
#configure
export CFLAGS="%{optflags}"
%{?_without_modxorg:export LDLIBS="-L/usr/X11R6/%{_lib}"}
%{__make} %{?_smp_mflags} PREFIX="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%doc %{_mandir}/man1/feh.1*
%doc %{_mandir}/man1/feh-cam.1*
%doc %{_mandir}/man1/gen-cam-menu.1*
%{_bindir}/feh
%{_bindir}/feh-cam
%{_bindir}/gen-cam-menu
%{_datadir}/feh/
%exclude %{_docdir}/feh/

%changelog
* Mon Jun 28 2010 Dag Wieers <dag@wieers.com> - 1.8-1
- Initial package. (using DAR)
