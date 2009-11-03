# $Id$
# Authority: dag

Summary: tool for figuring out network masks
Name: netmask
Version: 2.3.7
Release: 3.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://packages.qa.debian.org/n/netmask.html

Source: http://http.us.debian.org/debian/pool/main/n/netmask/netmask_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake, autoconf

%description
This is a tiny program handy if you work with firewalls or routers
or are a network admin of sorts.  It can determine the smallest set of
network masks to specify a range of hosts.  It can also convert between
common IP netmask and address formats.

%prep
%setup

%build
### FIXME: Doesn't build for RH80 or RH90 ;(
#%{__aclocal}
#%{__automake} --add-missing
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/netmask*
%doc %{_infodir}/netmask.info*
%{_bindir}/netmask

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.3.7-3.2
- Rebuild for Fedora Core 5.

* Sat Nov 12 2005 Dries Verachtert <dries@ulyssis.org> - 2.3.7-3
- Cleanup of spec file.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 2.3.7-2
- Added build requirements.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 2.3.7-1
- Updated to release 2.3.7.

* Sun Jul 13 2003 Dag Wieers <dag@wieers.com> - 2.3.5-0
- Initial package. (using DAR)
