# $Id$
# Authority: dries
# Upstream: Niklas Knutsson <nq$altern,org>

Summary: Versatile desktop calculator
Name: qalculate-kde
Version: 0.9.6
Release: 1%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://qalculate.sourceforge.net/

Source: http://dl.sf.net/qalculate/qalculate-kde-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gettext, gcc-c++, cln-devel
BuildRequires: gmp-devel
BuildRequires: libqalculate-devel >= 0.9.6

%description
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision and plotting.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang qalculate_kde

%clean
%{__rm} -rf %{buildroot}

%files -f qalculate_kde.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_datadir}/doc/HTML/*/qalculate_kde/
%{_bindir}/qalculate
%{_bindir}/qalculate-kde
%{_datadir}/applications/kde/qalculate_kde.desktop
%{_datadir}/apps/qalculate_kde/
%{_datadir}/icons/*/*/*/qalculate*.png

%changelog
* Sun Jun 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Updated to release 0.9.5.

* Mon Nov 13 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.4-1
- Updated to release 0.9.4.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1
- Updated to release 0.9.2.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Initial package.
