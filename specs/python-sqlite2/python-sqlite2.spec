# $Id$
# Authority: hadams

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pysqlite

Summary: DB-API 2.0 interface for SQLite 3.x
Name: python-sqlite2
Version: 2.3.3
Release: 1%{?dist}
License: zlib/libpng
Group: Development/Languages
URL: http://pysqlite.org/

Source: http://initd.org/pub/software/pysqlite/releases/2.3/%{version}/pysqlite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel, sqlite-devel >= 3.3.3, dos2unix
Requires: sqlite >= 3.3.3

%description
pysqlite is an interface to the SQLite 3.x embedded relational database
engine. It is almost fully compliant with the Python database API version
2.0 also exposes the unique features of SQLite.

%prep
%setup -n %{real_name}-%{version}
sed -i -e '/\/usr\/include/d; /\/usr\/lib/d' setup.cfg

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
dos2unix doc/code/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE doc/usage-guide.txt doc/code/
%{python_sitearch}/pysqlite2
%ghost %{python_sitearch}/pysqlite2/*.pyo
%ghost %{python_sitearch}/pysqlite2/test/*.pyo
%exclude %{_prefix}/pysqlite2-doc/

%changelog
* Sat Jul 07 2007 Heiko Adams <info@fedora-blog.de> - 2.3.3-1
- Rebuild for RPMforge.

* Tue Mar 13 2007 Dawid Gajownik <gajownik[AT]gmail.com> - 1:2.3.3-1
- Update to 2.3.3 (#231848)

* Fri Sep  8 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 1:2.3.2-2
- Don't %%ghost *.pyo files (#205425)
- Fix mixed-use-of-spaces-and-tabs rpmlint warning

* Sun Jul  2 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 1:2.3.2-1
- Update to 2.3.2

* Wed Jun 21 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 1:2.3.1-1
- Update to 2.3.1

* Tue Jun 13 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 1:2.3.0-1
- Update to 2.3.0
- Change e-mail address in ChangeLog

* Thu Apr 20 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 1:2.2.2-1
- Update to 2.2.2

* Wed Apr 19 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 1:2.2.1-1
- Update to 2.2.1

* Fri Apr 14 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 1:2.2.0-1
- Update to 2.2.0

* Tue Feb 14 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 1:2.1.3-4
- Rebuild for Fedora Extras 5

* Sun Feb  5 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 1:2.1.3-3
- python-sqlite2 in FC-4 was downgraded -> Epoch had to be bumped.
  We need to do the same in development branch

* Thu Feb  2 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.1.3-2
- Run tests in %%check section

* Thu Feb  2 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.1.3-1
- Update to 2.1.3

* Tue Jan 17 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.1.0-1
- Update to 2.1.0

* Sat Jan 14 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.0.5-2
- Fix missing BR: sqlite-devel (Chris Chabot, #176653)

* Wed Dec 28 2005 Dawid Gajownik <gajownik[AT]gmail.com> - 2.0.5-1
- Initial RPM release.

