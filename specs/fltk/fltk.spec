# $Id$

# Authority: dries
# Screenshot: http://www.fltk.org/images/fluid.gif

# NeedsCleanup

Summary: a cross-platform C++ GUI toolkit
Summary(nl): een cross-platform C++ GUI toolkit
Name: fltk
Version: 1.1.4
Release: 1.dries
License: FLTK
Group: System Environment/Libraries
URL: http://www.fltk.org/

Source: http://dl.sf.net/fltk/fltk-%{version}-source.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, gcc-c++, libjpeg-devel, zlib-devel, libpng-devel, XFree86-devel
Requires: libjpeg, zlib, libpng

%description
FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit for
UNIX/Linux (X11), Microsoft Windows and MacOS X. FLTK provides modern GUI
functionality and supports 3D graphics via OpenGL and its built-in GLUT 
emulation.

%description -l nl
FLTK (uitgesproken als "fulltick") is een cross-platform C++ GUI toolkit
voor UNIX/Linux (X11), Microsoft Windows en MacOS X. FLTK voorziet moderne
GUI functionaliteit zonder en ondersteunt 3D graphics via OpenGL en de
ingebouwde GLUT emulatie.

%prep
%setup

%build
%configure \
	--enable-shared="yes"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export DESTDIR=$RPM_BUILD_ROOT
# doesn't use something like DESTDIR :(
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/include/FL
sed -i "s/\/usr\/bin/${RPM_BUILD_ROOT//\//\\/}\/usr\/bin/g" makeinclude
sed -i "s/\/usr\/include/${RPM_BUILD_ROOT//\//\\/}\/usr\/include/g" makeinclude
sed -i "s/\/usr\/lib/${RPM_BUILD_ROOT//\//\\/}\/usr\/lib/g" makeinclude
sed -i "s/\/usr\/share/${RPM_BUILD_ROOT//\//\\/}\/usr\/share/g" makeinclude
make install
# the make install puts a lot of docs in /usr/share/doc which will be
# overwritten by %doc
mv $RPM_BUILD_ROOT/usr/share/doc .

%files
%defattr(-,root,root)
%doc README doc CHANGES COPYING ANNOUNCEMENT 
/usr/bin/fltk-config
/usr/bin/fluid
/usr/include/FL
/usr/lib/libfltk*
/usr/share/man/cat1/fltk-config.1
/usr/share/man/cat1/fluid.1
/usr/share/man/cat3/fltk.3
/usr/share/man/man1/fltk-config.1.gz
/usr/share/man/man1/fluid.1.gz
/usr/share/man/man3/fltk.3.gz

%changelog
* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 1.1.4-1.dries
- first packaging for Fedora Core 1
