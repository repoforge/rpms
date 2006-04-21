# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag$wieers,com>

Summary: Set up a Yum/Apt mirror from various sources (ISO, RHN, rsync, http, ftp, ...)
Name: yam
Version: 0.8.0
Release: 2.2
License: GPL
Group: System Environment/Base
URL: http://dag.wieers.com/home-made/yam/

Source: http://dag.wieers.com/home-made/yam/yam-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: /usr/bin/python2
Requires: python >= 2.0, createrepo >= 0.4.3

%description
Yam builds a local Apt/Yum RPM repository from local ISO files,
downloaded updates and extra packages from RHN and 3rd party
repositories.

It can download all updates and extras automatically, creates
the repository structure and meta-data, enables HTTP access to
the repository and creates a directory-structure for remote
network installations using PXE/TFTP.

With Yam, you can enable your laptop or a local server to provide
updates for the whole network and provide the proper files to
allow installations via the network.

%prep
%setup

%{__perl} -pi.orig -e 's|^(VERSION)\s*=\s*.+$|$1 = "%{version}"|' yam

%build

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -D -m0755 gensystemid %{buildroot}%{_bindir}/gensystemid

%preun
if [ $1 -eq 0 ]; then
	/service yam stop &>/dev/null || :
	/sbin/chkconfig --del yam
fi

%post
/sbin/chkconfig --add yam

#%postun
#/sbin/service yam condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README* THANKS TODO WISHLIST *.conf
%config(noreplace) %{_sysconfdir}/yam.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/yam.conf
%config %{_initrddir}/yam
%{_bindir}/gensystemid
%{_bindir}/yam
%{_datadir}/yam/
%{_localstatedir}/cache/yam/
%{_localstatedir}/www/yam/
%{_localstatedir}/yam/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.0-2.2
- Rebuild for Fedora Core 5.

* Fri Mar 10 2006 Dag Wieers <dag@wieers.com> - 0.8.0-2
- Added gensystemid to installation. (Ian Forde)

* Thu Mar 09 2006 Dag Wieers <dag@wieers.com> - 0.8.0-1
- Updated to release 0.8.0.

* Fri Mar 25 2005 Dag Wieers <dag@wieers.com> - 0.7.3-1
- Updated to release 0.7.3.

* Fri Jan 07 2005 Dag Wieers <dag@wieers.com> - 0.7.2-2
- Add %%post and %%postun scripts. (Bert de Bruijn)

* Fri Dec 31 2004 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Sun Nov 07 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Sun Oct 10 2004 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Fri Aug 27 2004 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.6-2
- Updated to release 0.6.
- Fix a version problem.

* Thu Aug 19 2004 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Wed May 19 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
