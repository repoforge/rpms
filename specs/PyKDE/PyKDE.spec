# $Id$

# Authority: dries

Summary: Python bindings for the KDE desktop environment
Name: PyKDE
Version: 3.8.0
Release: 3
License: MIT
Group: Development/Languages
URL: http://www.riverbankcomputing.co.uk/pykde/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.river-bank.demon.co.uk/download/PyKDE2/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
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
/sbin/ldconfig

%postun
/sbin/ldconfig

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
/usr/lib/python2.2/site-packages/libpythonize.so
/usr/lib/python2.2/site-packages/libdcopcmodule.so
/usr/lib/python2.2/site-packages/libkdecorecmodule.so
/usr/lib/python2.2/site-packages/libkdesucmodule.so
/usr/lib/python2.2/site-packages/libkdefxcmodule.so
/usr/lib/python2.2/site-packages/libkdeuicmodule.so
/usr/lib/python2.2/site-packages/libkiocmodule.so
/usr/lib/python2.2/site-packages/libkfilecmodule.so
/usr/lib/python2.2/site-packages/libkpartscmodule.so
/usr/lib/python2.2/site-packages/libkhtmlcmodule.so
/usr/lib/python2.2/site-packages/libkjscmodule.so
/usr/lib/python2.2/site-packages/libkspellcmodule.so
/usr/lib/python2.2/site-packages/libkdeprintcmodule.so
/usr/lib/kde3/libpykpanelapplet.so
/usr/lib/libpythonize.so
/usr/lib/libpykpanelapplet.so
/usr/lib/libqtcmodule.so
/usr/lib/libqtxmlcmodule.so
/usr/lib/libdcopcmodule.so
/usr/lib/libkdecorecmodule.so
/usr/lib/libkdefxcmodule.so
/usr/lib/libkdeuicmodule.so
/usr/lib/libsip.so

%files
%defattr(-,root,root)
%doc README AUTHORS BUGS ChangeLog COPYING DETAILS INSTALL importTest.py NEWS THANKS doc
/usr/lib/python2.2/site-packages/libpythonize.so.1
/usr/lib/python2.2/site-packages/libpythonize.so.1.0
/usr/lib/python2.2/site-packages/libpythonize.so.1.0.0
/usr/lib/python2.2/site-packages/dcop.py
/usr/lib/python2.2/site-packages/dcop.pyc
/usr/lib/python2.2/site-packages/libdcopcmodule.so.1
/usr/lib/python2.2/site-packages/libdcopcmodule.so.1.0
/usr/lib/python2.2/site-packages/libdcopcmodule.so.1.0.0
/usr/lib/python2.2/site-packages/kdecore.py
/usr/lib/python2.2/site-packages/kdecore.pyc
/usr/lib/python2.2/site-packages/libkdecorecmodule.so.1
/usr/lib/python2.2/site-packages/libkdecorecmodule.so.1.0
/usr/lib/python2.2/site-packages/libkdecorecmodule.so.1.0.0
/usr/lib/python2.2/site-packages/kdesu.py
/usr/lib/python2.2/site-packages/kdesu.pyc
/usr/lib/python2.2/site-packages/libkdesucmodule.so.1
/usr/lib/python2.2/site-packages/libkdesucmodule.so.1.0
/usr/lib/python2.2/site-packages/libkdesucmodule.so.1.0.0
/usr/lib/python2.2/site-packages/kdefx.py
/usr/lib/python2.2/site-packages/kdefx.pyc
/usr/lib/python2.2/site-packages/libkdefxcmodule.so.1
/usr/lib/python2.2/site-packages/libkdefxcmodule.so.1.0
/usr/lib/python2.2/site-packages/libkdefxcmodule.so.1.0.0
/usr/lib/python2.2/site-packages/kdeui.py
/usr/lib/python2.2/site-packages/kdeui.pyc
/usr/lib/python2.2/site-packages/libkdeuicmodule.so.1
/usr/lib/python2.2/site-packages/libkdeuicmodule.so.1.0
/usr/lib/python2.2/site-packages/libkdeuicmodule.so.1.0.0
/usr/lib/python2.2/site-packages/kio.py
/usr/lib/python2.2/site-packages/kio.pyc
/usr/lib/python2.2/site-packages/libkiocmodule.so.1
/usr/lib/python2.2/site-packages/libkiocmodule.so.1.0
/usr/lib/python2.2/site-packages/libkiocmodule.so.1.0.0
/usr/lib/python2.2/site-packages/kfile.py
/usr/lib/python2.2/site-packages/kfile.pyc
/usr/lib/python2.2/site-packages/libkfilecmodule.so.1
/usr/lib/python2.2/site-packages/libkfilecmodule.so.1.0
/usr/lib/python2.2/site-packages/libkfilecmodule.so.1.0.0
/usr/lib/python2.2/site-packages/kparts.py
/usr/lib/python2.2/site-packages/kparts.pyc
/usr/lib/python2.2/site-packages/libkpartscmodule.so.1
/usr/lib/python2.2/site-packages/libkpartscmodule.so.1.0
/usr/lib/python2.2/site-packages/libkpartscmodule.so.1.0.0
/usr/lib/python2.2/site-packages/khtml.py
/usr/lib/python2.2/site-packages/khtml.pyc
/usr/lib/python2.2/site-packages/libkhtmlcmodule.so.1
/usr/lib/python2.2/site-packages/libkhtmlcmodule.so.1.0
/usr/lib/python2.2/site-packages/libkhtmlcmodule.so.1.0.0
/usr/lib/python2.2/site-packages/kjs.py
/usr/lib/python2.2/site-packages/kjs.pyc
/usr/lib/python2.2/site-packages/libkjscmodule.so.1
/usr/lib/python2.2/site-packages/libkjscmodule.so.1.0
/usr/lib/python2.2/site-packages/libkjscmodule.so.1.0.0
/usr/lib/python2.2/site-packages/kspell.py
/usr/lib/python2.2/site-packages/kspell.pyc
/usr/lib/python2.2/site-packages/libkspellcmodule.so.1
/usr/lib/python2.2/site-packages/libkspellcmodule.so.1.0
/usr/lib/python2.2/site-packages/libkspellcmodule.so.1.0.0
/usr/lib/python2.2/site-packages/kdeprint.py
/usr/lib/python2.2/site-packages/kdeprint.pyc
/usr/lib/python2.2/site-packages/libkdeprintcmodule.so.1
/usr/lib/python2.2/site-packages/libkdeprintcmodule.so.1.0
/usr/lib/python2.2/site-packages/libkdeprintcmodule.so.1.0.0
/usr/lib/kde3/libpykpanelapplet.so.1
/usr/lib/kde3/libpykpanelapplet.so.1.0
/usr/lib/kde3/libpykpanelapplet.so.1.0.0
/usr/lib/libpythonize.so.1
/usr/lib/libpythonize.so.1.0
/usr/lib/libpythonize.so.1.0.0
/usr/lib/libpykpanelapplet.so.1
/usr/lib/libpykpanelapplet.so.1.0
/usr/lib/libpykpanelapplet.so.1.0.0
/usr/lib/libqtcmodule.so.1
/usr/lib/libqtcmodule.so.1.0
/usr/lib/libqtcmodule.so.1.0.0
/usr/lib/libqtxmlcmodule.so.1
/usr/lib/libqtxmlcmodule.so.1.0
/usr/lib/libqtxmlcmodule.so.1.0.0
/usr/lib/libdcopcmodule.so.1
/usr/lib/libdcopcmodule.so.1.0
/usr/lib/libdcopcmodule.so.1.0.0
/usr/lib/libkdecorecmodule.so.1
/usr/lib/libkdecorecmodule.so.1.0
/usr/lib/libkdecorecmodule.so.1.0.0
/usr/lib/libkdefxcmodule.so.1
/usr/lib/libkdefxcmodule.so.1.0
/usr/lib/libkdefxcmodule.so.1.0.0
/usr/lib/libkdeuicmodule.so.1
/usr/lib/libkdeuicmodule.so.1.0
/usr/lib/libkdeuicmodule.so.1.0.0
/usr/lib/libsip.so.10
/usr/lib/libsip.so.10.1
/usr/lib/libsip.so.10.1.1

%changelog
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 3.8.0-3
- cleanup of spec file
- added a devel package

* Sat Dec 27 2003 Dries Verachtert <dries@ulyssis.org> 3.8.0-2
- finished the packaging
- stripping of libs

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 3.8.0-1
- first packaging for Fedora Core 1

