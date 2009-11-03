# $Id$
# Authority: dag
# Upstream: Thomas Krennwallner <krennwallner$aon,at>

Summary: The Wake On Lan client
Name: wol
Version: 0.7.1
Release: 2.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://ahh.sourceforge.net/wol/

Source: http://dl.sf.net/ahh/wol-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
wol is the Wake On Lan client. It wakes up magic packet compliant machines
such as boxes with wake-on-lan ethernet-cards. Some workstations provides
SecureON which extends wake-on-lan with a password. This feature is also
provided by wol.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_infodir}/*.info*
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.1-2.2
- Rebuild for Fedora Core 5.

* Mon May 03 2004 Dag Wieers <dag@wieers.com> - 0.7.1-2
- Fixed ownership by adding missing defattr(). (Alain Rykaert)

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Thu Aug 21 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Initial package. (using DAR)
