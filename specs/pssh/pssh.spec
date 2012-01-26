# $Id$
# Authority: shuff
# Upstream: Andrew McNabb <amcnabb$mcnabbs,org>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(0)')

%{?el5:%define _without_egg_info 1}
%{?el4:%define _without_egg_info 1}
%{?el3:%define _without_egg_info 1}
%{?el2:%define _without_egg_info 1}

Summary: Parallel version of OpenSSH and related tools
Name: pssh
Version: 2.3
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://code.google.com/p/parallel-ssh/

Source: http://parallel-ssh.googlecode.com/files/pssh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.4
BuildRequires: python-setuptools
Requires: openssh
Requires: python >= 2.4

Provides: psshlib = %{version}

%description
PSSH (Parallel SSH) provides parallel versions of OpenSSH and related tools,
including pssh, pscp, prsync, pnuke, and pslurp.  The project includes psshlib
which can be used within custom applications.

%prep
%setup

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}" --install-data="%{_datadir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL
%doc %{_mandir}/man1/pssh.1*
%{_bindir}/pnuke
%{_bindir}/prsync
%{_bindir}/pscp
%{_bindir}/pslurp
%{_bindir}/pssh
%{_bindir}/pssh-askpass
%{python_sitelib}/psshlib/
%{!?_without_egg_info:%{python_sitelib}/*.egg-info}

%changelog
* Thu Jan 26 2012 Dag Wieers <dag@wieers.com> - 2.3-1
- Updated to release 2.3.

* Thu Feb 04 2010 Steve Huff <shuff@vecna.org> - 2.0-1
- Updated to release 2.0.

* Sat Aug 30 2008 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Updated to release 1.4.1.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Updated to release 1.3.0.

* Mon Jun 19 2006 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Updated to release 1.2.2.

* Wed Nov 10 2004 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Initial package. (using DAR)
