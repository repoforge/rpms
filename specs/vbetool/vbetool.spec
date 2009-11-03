# $Id$
# Authority: koenraad
# Upstream: Matthew Garrett <mjg59-yes,this,is,a,valid,email,address$srcf,ucam,org>

Summary: Real-mode video BIOS utility to alter hardware state
Name: vbetool
Version: 0.2
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.srcf.ucam.org/~mjg59/vbetool/

Source: http://www.srcf.ucam.org/~mjg59/vbetool/vbetool_%{version}.orig.tar.gz
Patch: vbetool-0.2-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: i386
BuildRequires: autoconf, pciutils-devel, automake

%description
vbetool allows you to run real-mode video BIOS code to alter
hardware state. It uses lrmi in order to run code from the video BIOS.
Currently, it is able to alter DPMS states, save/restore video card state
and attempts to initialize the video card from scratch.

%prep
%setup
%patch

%build
autoreconf --force --install --symlink
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%doc %{_mandir}/man1/vbetool.1*
%{_sbindir}/vbetool

%changelog
* Fri Mar 18 2005 Koenraad Heijlen <krpms@heijlen.be> - 0.2-1
- Initial package based on the debian package by Matthew Garrett.
- Patched the Makefile.
