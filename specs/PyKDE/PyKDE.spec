# $Id$

# Authority: dries

Summary: Python bindings for the KDE desktop environment
Name: PyKDE
Version: 3.11rc1
Release: 1
License: MIT
Group: Development/Languages
URL: http://www.riverbankcomputing.co.uk/pykde/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.river-bank.demon.co.uk/download/PyKDE2/PyKDE-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python, python-devel, sip, sip-devel, PyQt, PyQt-devel, qt, qt-devel, kdelibs-devel, gcc-c++
Requires: sip, python, PyQt, PyQt-devel

%description
PyKDE is a set of Python bindings for the KDE desktop environment. The
bindings are implemented as a set of Python modules: dcop, kdecore, kdesu,
kdefx, kdeui, kio, kfile, kparts, khtml, kjs, kspell and kdeprint. The
modules correspond to libraries in the kdelibs package. PyKDE supports
nearly all classes and methods in these libraries. 

%package devel
Summary: PyKDE development files
Group: Development/Languages
Requires: PyKDE = %{version}-%{release}

%description devel
Development files for PyKDE.

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
. /etc/profile.d/qt.sh
export KDEDIR=/usr
python configure.py
sed -i "s/-lDCOP -lkdecore/-lDCOP -lkdeui -lkdecore/g;" kdecore/Makefile
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
%makeinstall DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files devel
%defattr(-,root,root,0755)
%{_datadir}/sip

%files
%defattr(-,root,root, 0755)
%doc README AUTHORS BUGS ChangeLog COPYING INSTALL importTest.py NEWS THANKS doc
%{_libdir}/python*/site-packages/*.so
%{_libdir}/python*/site-packages/*.py
%{_libdir}/python*/site-packages/*.pyc

%changelog
* Wed May 26 2004 Dries Verachtert <dries@ulyssis.org> 3.11rc1-1
- update to 3.11rc1

* Fri Apr 23 2004 Dries Verachtert <dries@ulyssis.org> 3.11alpha5-1
- update to newer version: 3.11alpha5

* Thu Apr 22 2004 Dries Verachtert <dries@ulyssis.org> 3.8.0-4
- rebuild

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 3.8.0-3
- cleanup of spec file
- added a devel package

* Sat Dec 27 2003 Dries Verachtert <dries@ulyssis.org> 3.8.0-2
- finished the packaging
- stripping of libs

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 3.8.0-1
- first packaging for Fedora Core 1
