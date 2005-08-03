# $Id$
# Authority: dag
# Upstream: Bastian Kleineidam <calvin$users,sf,net>

%define python_dir %(python -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Check HTML documents for broken links
Name: linkchecker
Version: 3.0
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
# you can build and install on older python with the following line, 
# but the program will not run
# %{__perl} -pi -e 's|python2.4|python|g;' test/*.sh test/*.py
CFLAGS="%{optflags}" python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install \
	--root="%{buildroot}"
#%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files
# -f %{name}.lang
%defattr(-, root, root, 0775)
%doc ChangeLog INSTALL LICENSE README TODO
# %doc create.sql draft-gilman-news-url-00.txt
# %doc lconline/
%doc test/
%{_mandir}/man1/linkchecker*
%{_mandir}/*/man1/linkchecker*
%{_bindir}/linkchecker
%{_datadir}/linkchecker
%{python_dir}/linkcheck
%{python_dir}/_linkchecker_configdata.py


%changelog
* Mon Jul 11 2005 Dries Verachtert <dries@ulyssis.org> - 3.0-1
- Updated to release 3.0.

* Wed Feb 09 2005 Dries Verachtert <dries@ulyssis.org> - 2.4-1
- Updated to release 2.4.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 1.13.5-1
- Updated to release 1.13.5.

* Sun Feb 29 2004 Dag Wieers <dag@wieers.com> - 1.12.1-0
- Initial package. (using DAR)
