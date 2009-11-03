# $Id$

# Authority: dries

Summary: GNU PIC Utilities
Name: gputils
Version: 0.13.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://gputils.sourceforge.net/

Source: http://dl.sf.net/gputils/gputils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, bison

%description
GPUTILS is a collection of tools for the Microchip (TM) PIC
microcontrollers. It includes gpasm, gplink, and gplib.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/gpal
%{_bindir}/gplink
%{_bindir}/gplib
%{_bindir}/gpvo
%{_bindir}/gpasm
%{_bindir}/gpdasm
%{_bindir}/gpvc
%{_datadir}/gputils

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.13.0-1.2
- Rebuild for Fedora Core 5.

* Mon Jan 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.13.0-1
- Initial package.
