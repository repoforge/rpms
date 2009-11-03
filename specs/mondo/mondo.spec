# $Id$
# Authority: dag

Summary: Create system image for bare-metal disaster recovery from CD, DVD or tape
Name: mondo
Version: 2.2.4
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://www.mondorescue.org/

Source: ftp://ftp.mondorescue.org/src/mondo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExcludeArch: ppc
BuildRequires: newt-devel >= 0.50

Requires: mindi >= 1.2.1, bzip2 >= 0.9, afio, mkisofs, binutils, newt >= 0.50, buffer, cdrecord
%ifarch ia64
Requires: elilo, parted
%else
Requires: syslinux >= 1.52
%endif

%description
Mondo is a GPL disaster recovery solution to create backup media 
(CD, DVD, tape, network images) that can be used to redeploy the 
damaged system, as well as deploy similar or less similar systems.

%prep
%setup

%build
%configure \
    --program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags} VERSION="%{version}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -dp -m0755 %{buildroot}%{_localstatedir}/cache/mondo/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README svn.log TODO
%doc docs/en/mondorescue-howto.html docs/en/mondorescue-howto.pdf
%doc %{_mandir}/man8/mondoarchive.8*
%doc %{_mandir}/man8/mondorestore.8*
%{_datadir}/mondo/
%{_localstatedir}/cache/mondo/
%{_sbindir}/mondoarchive
%{_sbindir}/mondorestore

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 2.2.4-1
- Initial package. (using DAR)
