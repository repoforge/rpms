# $Id: $
# Authority: dries


%{?rh9:%define _without_php 1}

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define php_extdir %(php-config --extension-dir || echo %{_libdir}/php)
%{!?php_version:%define php_version %(php-config --version || echo bad)}

Summary: Extension for reading and writing YAML
Name: syck
Version: 0.55
Release: 4%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.whytheluckystiff.net/syck/

Source: http://rubyforge.org/frs/download.php/4492/syck-%{version}.tar.gz
Patch0: syck-0.55-libtool.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: autoconf >= 2.50
BuildRequires: byacc, flex, bison, libtool
BuildRequires: python-devel
%{!?_without_php:BuildRequires: php-devel}

%description
Syck is an extension for reading and writing YAML swiftly in popular
scripting languages. As Syck loads the YAML, it stores the data directly in
your language's symbol table.

%package devel
Summary: Extension for reading and writing YAML
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Syck is an extension for reading and writing YAML swiftly in popular
scripting languages. As Syck loads the YAML, it stores the data directly in
your language's symbol table.

%package -n php-syck
Summary: YAML module for php
Group: Development/Languages
Requires: php = %{php_version}
Obsoletes: syck-php <= %{version}-%{release}
Provides: syck-php = %{version}-%{release}

%description -n php-syck
Syck is an extension for reading and writing YAML swiftly in popular
scripting languages. As Syck loads the YAML, it stores the data directly in
your language's symbol table.

The php-syck package contains the syck php extension.

%package -n python-syck
Summary: YAML module for python
Group: Development/Languages
Requires: python
Obsoletes: syck-python <= %{version}-%{release}
Obsoletes: PySyck <= %{version}-%{release}
Provides: syck-python = %{version}-%{release}
Provides: PySyck = %{version}-%{release}

%description -n python-syck
Syck is an extension for reading and writing YAML swiftly in popular
scripting languages. As Syck loads the YAML, it stores the data directly in
your language's symbol table.

%prep
%setup
%patch0 -p1 -b .orig

%build
libtoolize --force --copy && aclocal && automake --add-missing && autoconf
%configure
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%{__rm} -f lib/*.la lib/.libs/*.la lib/.libs/*.lai

%if %{!?_without_php:1}0
pushd ext/php
phpize
export php_cv_cc_rpath=no
export CFLAGS="%{optflags} -I../../lib -L../../lib/.libs"
%configure --with-syck="."
%{__make} %{?_smp_mflags}
popd
%endif

pushd ext/python
CFLAGS="%{optflags}" %{__python} setup.py build
popd

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%if %{!?_without_php:1}0
%{__make} install -C ext/php INSTALL_ROOT="%{buildroot}"
%endif

pushd ext/python
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING README* TODO
%{_libdir}/libsyck.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/syck.h
%{_includedir}/syck_st.h
%{_libdir}/libsyck.a
%exclude %{_libdir}/libsyck.la
%{_libdir}/libsyck.so

%if %{!?_without_php:1}0
%files -n php-syck
%defattr(-, root, root, 0755)
%{php_extdir}/syck.so
%endif

%files -n python-syck
%defattr(-, root, root, 0755)
%{python_sitearch}/syck.so
%{python_sitearch}/yaml2xml.py
%{python_sitearch}/yaml2xml.pyc
%ghost %{python_sitearch}/yaml2xml.pyo
%{python_sitearch}/ydump.py
%{python_sitearch}/ydump.pyc
%ghost %{python_sitearch}/ydump.pyo
%{python_sitearch}/ypath.py
%{python_sitearch}/ypath.pyc
%ghost %{python_sitearch}/ypath.pyo

%changelog
* Sat May 05 2007 Dag Wieers <dag@wieers.com> - 0.55-4
- Fixed syck-devel require syck.
- Added missing README* documentation.
- Obsoletes jbj's PySyck.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.55-3
- Added php and python extensions.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.55-2
- Fixed the source url.

* Thu Oct 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.55-1
- Updated to release 0.55.

* Sat Apr 02 2005 Dag Wieers <dag@wieers.com> - 0.51-2
- Renamed package syck to syck-devel.
- Added -fPIC to the compile options for x86_64.

* Mon Mar 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Update to version 0.51.

* Tue Feb 08 2005 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Update to version 0.50.

* Mon Sep 13 2004 Dries Verachtert <dries@ulyssis.org> - 0.45-1
- Update to version 0.45.

* Sat Jul 31 2004 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Initial package.
