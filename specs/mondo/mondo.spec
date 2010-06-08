# $Id$
# Authority: dag

Summary: Create system image for bare-metal disaster recovery from CD, DVD or tape
Name: mondo
Version: 2.2.9.3
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://www.mondorescue.org/

Source: ftp://ftp.mondorescue.org/src/mondo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExcludeArch: ppc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: newt-devel >= 0.50
Requires: afio
Requires: binutils
Requires: buffer
Requires: bzip2 >= 0.9
Requires: cdrecord
Requires: mindi >= 2.0.7
Requires: mkisofs
Requires: newt >= 0.50
%ifarch ia64
Requires: elilo
Requires: parted
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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc docs/en/mondorescue-howto.html docs/en/mondorescue-howto.pdf
%doc %{_mandir}/man8/mondoarchive.8*
%doc %{_mandir}/man8/mondorestore.8*
%{_datadir}/mondo/
%{_localstatedir}/cache/mondo/
%{_sbindir}/mondoarchive
%{_sbindir}/mondorestore
%{_sbindir}/mrtest_mountlist
%{_sbindir}/mrtest_truncname

%changelog
* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 2.2.9.3-1
- Updated to release 2.2.9.3.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 2.2.4-1
- Initial package. (using DAR)
