# $Id$

# Authority: dries

Summary: Python bindings for the KDE desktop environment
Name: PyKDE
Version: 3.8.0
Release: 4
License: MIT
Group: Development/Languages
URL: http://www.riverbankcomputing.co.uk/pykde/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.river-bank.demon.co.uk/download/PyKDE2/PyKDE-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Patch0: searchsipfiles.patch.bz2
BuildRequires: python, sip, PyQt, qt-devel, sip-devel, kdelibs-devel
Requires: kdelibs, sip, python, PyQt, PyQt-devel

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
%patch -p1

%build
. /etc/profile.d/qt.sh
export KDEDIR=/usr
python build.py
sed -i "s/-lDCOP -lkdecore/-lDCOP -lkdeui -lkdecore/g;" kdecore/Makefile
%{__make} %{?_smp_mflags}
(cd pythonize; %{__make} ../libs/libpythonize.so.1.0.0)

%install
. /etc/profile.d/qt.sh
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
#make install
# the make install doesn't use DESTDIR, the varname DESTDIR 
# is already used by the Makefile for the dir where the 
# compiled/linked libs have to be placed.. not good.

mkdir -p ${DESTDIR}/usr/lib
mkdir -p ${DESTDIR}/usr/lib/python2.2/site-packages
mkdir -p ${DESTDIR}/usr/lib/kde3

## pythonize
%{__mv} pythonize/../libs/libpythonize* ${DESTDIR}/usr/lib/python2.2/site-packages
#%{__chown} 0:0 ${DESTDIR}/usr/lib/python2.2/site-packages/libpythonize*
rm -f ${DESTDIR}/usr/lib/libpythonize*
ln -s /usr/lib/python2.2/site-packages/libpythonize.so.1.0.0 ${DESTDIR}/usr/lib/libpythonize.so
ln -s /usr/lib/python2.2/site-packages/libpythonize.so.1.0.0 ${DESTDIR}/usr/lib/libpythonize.so.1
ln -s /usr/lib/python2.2/site-packages/libpythonize.so.1.0.0 ${DESTDIR}/usr/lib/libpythonize.so.1.0
ln -s /usr/lib/python2.2/site-packages/libpythonize.so.1.0.0 ${DESTDIR}/usr/lib/libpythonize.so.1.0.0

## dcop
for name in dcop kdecore kdesu kdefx kdeui kio kfile kparts khtml kjs kspell kdeprint; do \
%{__cp} ${name}/${name}.py ${DESTDIR}/usr/lib/python2.2/site-packages
%{__cp} ${name}/${name}.pyc ${DESTDIR}/usr/lib/python2.2/site-packages
%{__mv} ${name}/../libs/lib${name}* ${DESTDIR}/usr/lib/python2.2/site-packages
#%{__chown} 0:0 ${DESTDIR}/usr/lib/python2.2/site-packages/lib${name}*
done

%{__mv} pykpanelapplet/../libs/libpykpanelapplet* ${DESTDIR}/usr/lib/kde3
#%{__chown} 0:0 ${DESTDIR}/usr/lib/kde3/libpykpanelapplet*
%{__rm} -f ${DESTDIR}/usr/lib/libpykpanelapplet*
ln -s /usr/lib/kde3/libpykpanelapplet.so.1.0.0 ${DESTDIR}/usr/lib/libpykpanelapplet.so
ln -s /usr/lib/kde3/libpykpanelapplet.so.1.0.0 ${DESTDIR}/usr/lib/libpykpanelapplet.so.1
ln -s /usr/lib/kde3/libpykpanelapplet.so.1.0.0 ${DESTDIR}/usr/lib/libpykpanelapplet.so.1.0
ln -s /usr/lib/kde3/libpykpanelapplet.so.1.0.0 ${DESTDIR}/usr/lib/libpykpanelapplet.so.1.0.0

for name in qt qtxml dcop kdecore kdefx kdeui ; do \
rm -f ${DESTDIR}/usr/lib/lib${name}cmodule*
ln -s /usr/lib/python2.2/site-packages/lib${name}cmodule.so.1.0.0 ${DESTDIR}/usr/lib/lib${name}cmodule.so
ln -s /usr/lib/python2.2/site-packages/lib${name}cmodule.so.1.0.0 ${DESTDIR}/usr/lib/lib${name}cmodule.so.1
ln -s /usr/lib/python2.2/site-packages/lib${name}cmodule.so.1.0.0 ${DESTDIR}/usr/lib/lib${name}cmodule.so.1.0
ln -s /usr/lib/python2.2/site-packages/lib${name}cmodule.so.1.0.0 ${DESTDIR}/usr/lib/lib${name}cmodule.so.1.0.0
done

%{__rm} -f ${DESTDIR}/usr/lib/libsip.*
ln -s /usr/lib/python2.2/site-packages/libsip.so ${DESTDIR}/usr/lib/libsip.so
ln -s /usr/lib/python2.2/site-packages/libsip.so.10 ${DESTDIR}/usr/lib/libsip.so.10
ln -s /usr/lib/python2.2/site-packages/libsip.so.10.1 ${DESTDIR}/usr/lib/libsip.so.10.1
ln -s /usr/lib/python2.2/site-packages/libsip.so.10.1.1 ${DESTDIR}/usr/lib/libsip.so.10.1.1
strip $(find ${DESTDIR} -type f | grep '.so')

%files devel
%defattr(-,root,root,0755)
%{_libdir}/python2.2/site-packages/libpythonize.so
%{_libdir}/python2.2/site-packages/libdcopcmodule.so
%{_libdir}/python2.2/site-packages/libkdecorecmodule.so
%{_libdir}/python2.2/site-packages/libkdesucmodule.so
%{_libdir}/python2.2/site-packages/libkdefxcmodule.so
%{_libdir}/python2.2/site-packages/libkdeuicmodule.so
%{_libdir}/python2.2/site-packages/libkiocmodule.so
%{_libdir}/python2.2/site-packages/libkfilecmodule.so
%{_libdir}/python2.2/site-packages/libkpartscmodule.so
%{_libdir}/python2.2/site-packages/libkhtmlcmodule.so
%{_libdir}/python2.2/site-packages/libkjscmodule.so
%{_libdir}/python2.2/site-packages/libkspellcmodule.so
%{_libdir}/python2.2/site-packages/libkdeprintcmodule.so
%{_libdir}/kde3/libpykpanelapplet.so
%{_libdir}/libpythonize.so
%{_libdir}/libpykpanelapplet.so
%{_libdir}/libqtcmodule.so
%{_libdir}/libqtxmlcmodule.so
%{_libdir}/libdcopcmodule.so
%{_libdir}/libkdecorecmodule.so
%{_libdir}/libkdefxcmodule.so
%{_libdir}/libkdeuicmodule.so
%{_libdir}/libsip.so

%files
%defattr(-,root,root, 0755)
%doc README AUTHORS BUGS ChangeLog COPYING DETAILS INSTALL importTest.py NEWS THANKS doc
%{_libdir}/python2.2/site-packages/libpythonize.so.1
%{_libdir}/python2.2/site-packages/libpythonize.so.1.0
%{_libdir}/python2.2/site-packages/libpythonize.so.1.0.0
%{_libdir}/python2.2/site-packages/dcop.py
%{_libdir}/python2.2/site-packages/dcop.pyc
%{_libdir}/python2.2/site-packages/libdcopcmodule.so.1
%{_libdir}/python2.2/site-packages/libdcopcmodule.so.1.0
%{_libdir}/python2.2/site-packages/libdcopcmodule.so.1.0.0
%{_libdir}/python2.2/site-packages/kdecore.py
%{_libdir}/python2.2/site-packages/kdecore.pyc
%{_libdir}/python2.2/site-packages/libkdecorecmodule.so.1
%{_libdir}/python2.2/site-packages/libkdecorecmodule.so.1.0
%{_libdir}/python2.2/site-packages/libkdecorecmodule.so.1.0.0
%{_libdir}/python2.2/site-packages/kdesu.py
%{_libdir}/python2.2/site-packages/kdesu.pyc
%{_libdir}/python2.2/site-packages/libkdesucmodule.so.1
%{_libdir}/python2.2/site-packages/libkdesucmodule.so.1.0
%{_libdir}/python2.2/site-packages/libkdesucmodule.so.1.0.0
%{_libdir}/python2.2/site-packages/kdefx.py
%{_libdir}/python2.2/site-packages/kdefx.pyc
%{_libdir}/python2.2/site-packages/libkdefxcmodule.so.1
%{_libdir}/python2.2/site-packages/libkdefxcmodule.so.1.0
%{_libdir}/python2.2/site-packages/libkdefxcmodule.so.1.0.0
%{_libdir}/python2.2/site-packages/kdeui.py
%{_libdir}/python2.2/site-packages/kdeui.pyc
%{_libdir}/python2.2/site-packages/libkdeuicmodule.so.1
%{_libdir}/python2.2/site-packages/libkdeuicmodule.so.1.0
%{_libdir}/python2.2/site-packages/libkdeuicmodule.so.1.0.0
%{_libdir}/python2.2/site-packages/kio.py
%{_libdir}/python2.2/site-packages/kio.pyc
%{_libdir}/python2.2/site-packages/libkiocmodule.so.1
%{_libdir}/python2.2/site-packages/libkiocmodule.so.1.0
%{_libdir}/python2.2/site-packages/libkiocmodule.so.1.0.0
%{_libdir}/python2.2/site-packages/kfile.py
%{_libdir}/python2.2/site-packages/kfile.pyc
%{_libdir}/python2.2/site-packages/libkfilecmodule.so.1
%{_libdir}/python2.2/site-packages/libkfilecmodule.so.1.0
%{_libdir}/python2.2/site-packages/libkfilecmodule.so.1.0.0
%{_libdir}/python2.2/site-packages/kparts.py
%{_libdir}/python2.2/site-packages/kparts.pyc
%{_libdir}/python2.2/site-packages/libkpartscmodule.so.1
%{_libdir}/python2.2/site-packages/libkpartscmodule.so.1.0
%{_libdir}/python2.2/site-packages/libkpartscmodule.so.1.0.0
%{_libdir}/python2.2/site-packages/khtml.py
%{_libdir}/python2.2/site-packages/khtml.pyc
%{_libdir}/python2.2/site-packages/libkhtmlcmodule.so.1
%{_libdir}/python2.2/site-packages/libkhtmlcmodule.so.1.0
%{_libdir}/python2.2/site-packages/libkhtmlcmodule.so.1.0.0
%{_libdir}/python2.2/site-packages/kjs.py
%{_libdir}/python2.2/site-packages/kjs.pyc
%{_libdir}/python2.2/site-packages/libkjscmodule.so.1
%{_libdir}/python2.2/site-packages/libkjscmodule.so.1.0
%{_libdir}/python2.2/site-packages/libkjscmodule.so.1.0.0
%{_libdir}/python2.2/site-packages/kspell.py
%{_libdir}/python2.2/site-packages/kspell.pyc
%{_libdir}/python2.2/site-packages/libkspellcmodule.so.1
%{_libdir}/python2.2/site-packages/libkspellcmodule.so.1.0
%{_libdir}/python2.2/site-packages/libkspellcmodule.so.1.0.0
%{_libdir}/python2.2/site-packages/kdeprint.py
%{_libdir}/python2.2/site-packages/kdeprint.pyc
%{_libdir}/python2.2/site-packages/libkdeprintcmodule.so.1
%{_libdir}/python2.2/site-packages/libkdeprintcmodule.so.1.0
%{_libdir}/python2.2/site-packages/libkdeprintcmodule.so.1.0.0
%{_libdir}/kde3/libpykpanelapplet.so.1
%{_libdir}/kde3/libpykpanelapplet.so.1.0
%{_libdir}/kde3/libpykpanelapplet.so.1.0.0
%{_libdir}/libpythonize.so.1
%{_libdir}/libpythonize.so.1.0
%{_libdir}/libpythonize.so.1.0.0
%{_libdir}/libpykpanelapplet.so.1
%{_libdir}/libpykpanelapplet.so.1.0
%{_libdir}/libpykpanelapplet.so.1.0.0
%{_libdir}/libqtcmodule.so.1
%{_libdir}/libqtcmodule.so.1.0
%{_libdir}/libqtcmodule.so.1.0.0
%{_libdir}/libqtxmlcmodule.so.1
%{_libdir}/libqtxmlcmodule.so.1.0
%{_libdir}/libqtxmlcmodule.so.1.0.0
%{_libdir}/libdcopcmodule.so.1
%{_libdir}/libdcopcmodule.so.1.0
%{_libdir}/libdcopcmodule.so.1.0.0
%{_libdir}/libkdecorecmodule.so.1
%{_libdir}/libkdecorecmodule.so.1.0
%{_libdir}/libkdecorecmodule.so.1.0.0
%{_libdir}/libkdefxcmodule.so.1
%{_libdir}/libkdefxcmodule.so.1.0
%{_libdir}/libkdefxcmodule.so.1.0.0
%{_libdir}/libkdeuicmodule.so.1
%{_libdir}/libkdeuicmodule.so.1.0
%{_libdir}/libkdeuicmodule.so.1.0.0
%{_libdir}/libsip.so.10
%{_libdir}/libsip.so.10.1
%{_libdir}/libsip.so.10.1.1

%changelog
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
