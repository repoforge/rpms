# $Id$
# Authority: dag
# Upstream: Bastian Kleineidam <calvin$users,sf,net>

%define python_dir %(python -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Check HTML documents for broken links
Name: linkchecker
Version: 4.6
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://linkchecker.sourceforge.net/

Source: http://dl.sf.net/linkchecker/linkchecker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, gettext
BuildRequires: python-devel >= 2.4
Requires: python >= 2.4

%description
LinkChecker checks HTML documents for broken links.

%prep
%setup

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install \
	--root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0775)
%doc ChangeLog INSTALL README TODO
%doc %{_mandir}/man1/linkchecker*
%doc %{_mandir}/*/man1/linkchecker*
%{_bindir}/linkchecker
%{_datadir}/linkchecker/
%{python_dir}/linkcheck/
%{python_dir}/_linkchecker_configdata.py*


%changelog
* Mon Dec 18 2006 Dries Verachtert <dries@ulyssis.org> - 4.6-1
- Updated to release 4.6.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 4.4-1
- Updated to release 4.4.

* Mon Aug 07 2006 Dries Verachtert <dries@ulyssis.org> - 4.2-1
- Updated to release 4.2.

* Tue May 29 2006 Dries Verachtert <dries@ulyssis.org> - 4.1-1
- Updated to release 4.1.

* Sat May 20 2006 Dries Verachtert <dries@ulyssis.org> - 4.0-1
- Updated to release 4.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.3-1.2
- Rebuild for Fedora Core 5.

* Sat Oct 15 2005 Dries Verachtert <dries@ulyssis.org> - 3.3-1
- Updated to release 3.3.

* Mon Jul 11 2005 Dries Verachtert <dries@ulyssis.org> - 3.0-1
- Updated to release 3.0.

* Wed Feb 09 2005 Dries Verachtert <dries@ulyssis.org> - 2.4-1
- Updated to release 2.4.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 1.13.5-1
- Updated to release 1.13.5.

* Sun Feb 29 2004 Dag Wieers <dag@wieers.com> - 1.12.1-0
- Initial package. (using DAR)
