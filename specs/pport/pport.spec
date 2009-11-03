# $Id$
# Authority: dries
# Upstream: <pport-developement$lists,sourceforge,net>

Summary: Utility for accessing the output pins of a parallel port
Name: pport
Version: 0.6.9
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://sourceforge.net/projects/pport/

Source: http://dl.sf.net/pport/pport-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
PPort is a simple yet handy program for accessing the output pins of a
parallel port. Using this bundle, one can successfully control any
household appliance or electronic device with minimal hassle and
practically no changes.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#%{__install} -Dp -m0755 src/pport %{buildroot}%{_sbindir}/pport
#%{__install} -Dp -m0644 man/pport.8.gz %{buildroot}%{_mandir}/man8/pport.8.gz

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS
%doc %{_mandir}/man1/pport*
#%config(noreplace) %{_sysconfdir}/pportd.conf
%{_bindir}/pport*
#%exclude %{_prefix}/doc/pport/

%changelog
* Mon Sep 25 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.9-1
- Updated to release 0.6.9.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.8-1.2
- Rebuild for Fedora Core 5.

* Thu Nov 04 2004 Dries Verachtert <dries@ulyssis.org> 0.6.8-1
- Updated to release 0.6.8.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 0.6.7-1
- Updated to release 0.6.7.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.6.6-1
- Updated to release 0.6.6.

* Fri Jul 09 2004 Dag Wieers <dag@wieers.com> - 0.6.5-1
- Updated to release 0.6.5.

* Sun Jul 04 2004 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Updated to release 0.6.4.

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 0.6.3-1
- Updated to release 0.6.3.

* Thu Jun 03 2004 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Mon May 31 2004 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.
- Cosmetic changes.

* Sun Feb 1 2004 Dries Verachtert <dries@ulyssis.org> 0.5g-1
- first packaging for Fedora Core 1
