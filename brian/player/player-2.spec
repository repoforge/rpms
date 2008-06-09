%define pythonver %(%{__python} -c 'import sys; print sys.version[:3]' || echo 2.4)
%define pythondir %(%{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages"][0]')

Summary: robotics protocols
Name: player
Version: 2.1.0rc2
Release: 2.bs%{?dist}
License: GPL
Group: Development/Libraries
URL: http://playerstage.sf.net/
Packager: Brian Schueler
Obsoletes: player < %{version}
Provides: player = %{version}-%{release}
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libtool-ltdl-devel gsl opencv

%description
Player robot protocols

%prep
%setup -q 

%build
#ln -b -s /usr/lib/libltdl.so.3 /usr/lib/libltdl.so
mkdir -p /usr/X11R6/lib/X11
./bootstrap || echo no bootstrap... continuing
%configure 

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}
LIBDIR="`echo %{buildroot}%{_libdir} | sed \"s/\\\//\\\\\\\\\//g\"`"
DESTLIBDIR="`echo %{_libdir} | sed \"s/\\\//\\\\\\\\\//g\"`"
%makeinstall
mv %{buildroot}%{_includedir}/player-2.1/* %{buildroot}%{_includedir}
rm -fr %{buildroot}%{_includedir}/player-2.1
TMPFILE=%{buildroot}/tmp-`basename $0`-$$
pushd %{buildroot}%{_libdir}
ls *.la | while read MYFILE; do
  cp $MYFILE $TMPFILE
  echo processing: $MYFILE
  cat $TMPFILE | sed "s/${LIBDIR}/${DESTLIBDIR}/g" > $MYFILE
done
popd
rm ${TMPFILE}
mkdir -p %{buildroot}/usr/X11R6/lib/X11
ln -b -s /usr/share/X11/rgb.txt %{buildroot}/usr/X11R6/lib/X11/rgb.txt

# make prefix=%{buildroot}/usr install
# DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/libplayercore.so
%{_libdir}/libplayercore.so.2*
%{_libdir}/libplayerc.so
%{_libdir}/libplayerc++.so
%{_libdir}/libplayerc.so.2*
%{_libdir}/libplayerc++.so.2*
%{_libdir}/libplayerdrivers.so
%{_libdir}/libplayerdrivers.so.2*
%{_libdir}/libplayererror.so
%{_libdir}/libplayererror.so.2*
%{_libdir}/libplayerjpeg.so
%{_libdir}/libplayerjpeg.so.2*
%{_libdir}/libplayertcp.so
%{_libdir}/libplayertcp.so.2*
%{_libdir}/libplayerxdr.so
%{_libdir}/libplayerxdr.so.2*
%{_libdir}/python%{pythonver}/site-packages/playerc.py
%{_libdir}/python%{pythonver}/site-packages/playerc.pyc
%{_libdir}/python%{pythonver}/site-packages/playerc.pyo
%{_libdir}/python%{pythonver}/site-packages/_playerc.so
%{_includedir}/
%{_datadir}/player/
%{_libdir}
%{_libdir}/libplayerc.a
%{_libdir}/libplayerc++.a
%{_libdir}/libplayerc.la
%{_libdir}/libplayerc++.la
%{_libdir}/libplayercore.a
%{_libdir}/libplayercore.la
%{_libdir}/libplayerdrivers.a
%{_libdir}/libplayerdrivers.la
%{_libdir}/libplayererror.a
%{_libdir}/libplayererror.la
%{_libdir}/libplayerjpeg.a
%{_libdir}/libplayerjpeg.la
%{_libdir}/libplayertcp.a
%{_libdir}/libplayertcp.la
%{_libdir}/libplayerxdr.a
%{_libdir}/libplayerxdr.la
%{_libdir}/pkgconfig/playercore.pc
%{_libdir}/pkgconfig/playerc.pc
%{_libdir}/pkgconfig/playerc++.pc
%{_libdir}/pkgconfig/playerdrivers.pc
%{_libdir}/pkgconfig/playererror.pc
%{_libdir}/pkgconfig/playertcp.pc
%{_libdir}/pkgconfig/playerxdr.pc
%{_bindir}
%{_bindir}/player
%{_bindir}/playercam
%{_bindir}/playerjoy
%{_bindir}/playernav
%{_bindir}/playerprint
%{_bindir}/playerv
%{_bindir}/playervcr
%{_bindir}/playerwritemap
%{_bindir}/playerxdrgen.py
%{_bindir}/playerxdrgen.pyc
%{_bindir}/playerxdrgen.pyo
/usr/X11R6/lib/X11/rgb.txt

%changelog
* Tue May 13 2008 Brian Schueler <brian.schueler@gmx.de> - 2.1.0rc2.2
- Libdir/Plugin fixes

* Mon May 15 2006 Douglas S. Blank <dblank@brynmawr.edu> - 2-1
- Initial build.

