%define pythonver %(%{__python} -c 'import sys; print sys.version[:3]' || echo 2.4)
%define pythondir %(%{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages"][0]')

Summary: 2d robotics simulator
Name: stage
Version: 2.1.0rc2
Release: 2.bs%{?dist}
License: GPL
Group: Development/Libraries
URL: http://playerstage.sf.net/
Packager: Brian Schueler
Obsoletes: stage < %{version}
Provides: stage = %{version}-%{release}
Requires: player
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Stage robot simulator

%prep
%setup -q 
./bootstrap || echo no boostrap... continuing

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}
LIBDIR="`echo %{buildroot}%{_libdir} | sed \"s/\\\//\\\\\\\\\//g\"`"
DESTLIBDIR="`echo %{_libdir} | sed \"s/\\\//\\\\\\\\\//g\"`"
%makeinstall
mv %{buildroot}%{_includedir}/stage-2.1/* %{buildroot}%{_includedir}
rm -fr %{buildroot}%{_includedir}/stage-2.1
TMPFILE=%{buildroot}/tmp-`basename $0`-$$
pushd %{buildroot}%{_libdir}
ls *.la | while read MYFILE; do
  cp $MYFILE $TMPFILE
  cat $TMPFILE | sed "s/${LIBDIR}/${DESTLIBDIR}/g" > $MYFILE
done
popd
rm ${TMPFILE}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/audio
%{_bindir}/ptest
%{_bindir}/stest
%{_includedir}/stage.h
%{_libdir}/libstage.a
%{_libdir}/libstage.la
%{_libdir}/libstage.so
%{_libdir}/libstage.so.2*
%{_libdir}/libstageplugin.a
%{_libdir}/libstageplugin.la
%{_libdir}/libstageplugin.so
%{_libdir}/libstageplugin.so.1*
%{_libdir}/pkgconfig/stage.pc
%{_datadir}/stage/worlds/

%changelog
* Tue May 13 2008 Brian Schueler <brian.schueler@gmx.de> - 2.1.0rc2.2
- Libdir/Plugin fixes

