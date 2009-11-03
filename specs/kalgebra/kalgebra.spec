# $Id$
# Authority: dries

%define real_version 20051121

Summary: MathML-based graph calculator
Name: kalgebra
Version: 0.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://kalgebra.berlios.de

Source: http://download.berlios.de/kalgebra/kalgebra-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gettext, gcc-c++

%description
KAlgebra is a MathML-based graph calculator.
Besides it was initially mathml oriented now it
can be used by everyone with little mathematic
knowledge.

%prep
%setup -n %{name}

%build
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
cd src
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd src
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/kalgebra
%{_datadir}/icons/crystalsvg/*/*/kalgebra.png
%{_datadir}/applnk/Utilities/kalgebra.desktop
%{_datadir}/apps/kalgebra/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-1.2
- Rebuild for Fedora Core 5.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Initial package.
