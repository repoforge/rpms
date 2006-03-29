# $Id$
# Authority: dries
# Upstream:
# Screenshot: http://giftoxic.sourceforge.net/data/images/screenie-transfer.png
# ScreenshotURL: http://giftoxic.sourceforge.net/index.php?screenshots

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}


%define real_name giFToxic

Summary: GUI for the peer2peer tool gift
Name: giftoxic
Version: 0.0.10
Release: 1
License: GPL
Group: Applications/Internet
URL: http://giftoxic.sourceforge.net/

Source: http://dl.sf.net/giftoxic/giFToxic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gift-devel, gtk2-devel, gettext, bison
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}
Requires: gift

%description
giFToxic is a GTK2-based client for giFT. At the moment it is under heavy
development.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{real_name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
%{_datadir}/giFToxic/logo.png

%changelog
* Mon Jun 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.0.10-1
- Initial package.
