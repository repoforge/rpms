# $Id$
# Authority: dries
# Upstream: <pport-developement@lists.sf.net>

Summary: Utility for accessing the output pins of a parallel port
Name: pport
Version: 0.6.5
Release: 1
License: GPL
Group: Applications/System
URL: http://sf.net/projects/pport/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/pport/pport-%{version}.tar.bz2
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
#%{__install} -D -m0755 src/pport %{buildroot}%{_sbindir}/pport
#%{__install} -D -m0644 man/pport.8.gz %{buildroot}%{_mandir}/man8/pport.8.gz

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS THANKS README
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/pportd.conf
%{_bindir}/*
%exclude %{_prefix}/doc/pport/

%changelog
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
