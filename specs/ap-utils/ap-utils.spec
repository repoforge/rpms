# $Id$
# Authority: dag
# Upstream: <ap-utils$lists,polesye,net>

Summary: Configure and monitor Wireless Access Points
Name: ap-utils
Version: 1.5
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://ap-utils.polesye.net/

Source: ftp://linux.zhitomir.net/ap-utils/ap-utils-%{version}.tar.bz2
#Source: http://dl.sf.net/ap-utils/ap-utils-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: ncurses-devel, gettext

%description
Wireless Access Point Utilities for Unix is a set of utilities
to configure and monitor Wireless Access Points using SNMP.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc Documentation/*.html Documentation/FAQ
%doc %{_mandir}/man8/ap-auth.8*
%doc %{_mandir}/man8/ap-config.8*
%doc %{_mandir}/man8/ap-gl.8*
%doc %{_mandir}/man8/ap-mrtg.8*
%doc %{_mandir}/man8/ap-tftp.8*
%doc %{_mandir}/man8/ap-trapd.8*
%{_bindir}/ap-auth
%{_bindir}/ap-config
%{_bindir}/ap-gl
%{_bindir}/ap-mrtg
%{_bindir}/ap-rrd
%{_bindir}/ap-tftp
%{_sbindir}/ap-trapd

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-1.2
- Rebuild for Fedora Core 5.

* Mon Mar 07 2005 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Sun May 30 2004 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Updated to release 1.4.1.

* Mon Feb 23 2004 Dag Wieers <dag@wieers.com> - 1.4-0
- Initial package. (using DAR)
