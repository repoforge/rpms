# $Id: $

# Authority: dries
# Upstream: 
# Screenshot: http://giftoxic.sourceforge.net/data/images/screenie-transfer.png
# ScreenshotURL: http://giftoxic.sourceforge.net/index.php?screenshots
 
%define real_name giFToxic

Summary: GUI for the peer2peer tool gift
Name: giftoxic
Version: 0.0.10
Release: 1
License: GPL
Group: Applications/Internet
URL: http://giftoxic.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/giftoxic/giFToxic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gift, gtk2-devel, XFree86-devel, gettext, bison
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
