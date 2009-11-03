# $Id$
# Authority: dag
# Upstream: Tim Stadelmann <t,stadelmann1$physics,ox,ac,uk>

Summary: Hotswap peripherals in portable computers
Name: hotswap
Version: 0.4.0
Release: 2.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://users.ox.ac.uk/~univ1377/c600.html

Source: http://users.ox.ac.uk/~univ1377/hotswap-%{version}.tar.gz
Patch1: hotswap-example.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
hotswap allows you to register and unregister hotswappable IDE
devices, for example notebook computers modules, with the Linux
kernel.

%package kde
Summary: KDE frontend for the hotswap program
Group: Applications/System
Requires: hotswap

%description kde
khotswap is a simple KDE frontend for the hotswap utility and should
be fairly self-explanatory.  It simply calls the backend using
appropriate command line arguments.

%package motif
Summary: Motif frontend for the hotswap program
Group: Applications/System
Requires: hotswap

%description motif
xhotswap is a simple Motif frontend for the hotswap utility and should
be fairly self-explanatory.  It simply calls the backend using
appropriate command line arguments.

%prep
%setup
%patch1 -p0

%{__perl} -pi.orig -e 's|chown|# chown|' src/Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang hotswap
%find_lang khotswap
%find_lang xhotswap

%{__install} -Dp -m0644 doc/hotswaprc.example %{buildroot}%{_sysconfdir}/hotswaprc

%clean
%{__rm} -rf %{buildroot}

%files -f hotswap.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README doc/hotswaprc.example
%doc %{_mandir}/man1/hotswap.1*
%doc %{_mandir}/man5/hotswaprc.5*
%config(noreplace) %{_sysconfdir}/hotswaprc
%attr(4711, root, disk) %{_bindir}/hotswap

%files kde -f khotswap.lang
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/khotswap.1*
%doc %{_docdir}/HTML/en/khotswap/
%{_bindir}/khotswap
%{_datadir}/applnk/Utilities/khotswap.desktop
%{_datadir}/apps/khotswap/

%files motif -f xhotswap.lang
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/xhotswap.1*
%{_bindir}/xhotswap

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.0-2.2
- Rebuild for Fedora Core 5.

* Fri Dec 10 2004 Dag Wieers <dag@wieers.com> - 0.4.0-2
- Fixed Group tag.

* Thu Aug 05 2004 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Based on Jason Merrill's work.
- Initial package. (using DAR)
