# Authority: freshrpms
Summary: A C++ interface for GNOME.
Name: gnomemm
Version: 1.2.3
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://download.sourceforge.net/gtkmm/%{name}-%{version}.tar.bz2
Patch: gnomemm-1.2.3-rh80.patch
Buildroot: %{_tmppath}/root)%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk+-devel, gnome-libs-devel, gtkmm-devel, libsigc++-devel

%description
This package provides a C++ interface for GnomeUI.  It is a subpackage of
the Gtk-- project.  The interface provides a convenient interface for C++
programmers to create Gnome GUIs with GTK+'s flexible object-oriented 
framework.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
#{?rh80:%{__perl} -pi.orig -e 's|(type_correctcallback) cb);$|cb);$|' src/procbar.gen_h}

%build
%configure \
	--enable-static \
	--enable-shared \
	--enable-docs
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up examples
%{__rm} -f examples/Makefile* examples/examples.conf.in

# strip down the docs 
find docs/ \
\( 	-name 'Makefile*' -or	\
	-name '*.m4' -or	\
	-name 'html' -or	\
	-name 'header' -or 	\
	-name '*.h' 		\
\)	-exec rm -rf {} \;

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc examples/ docs/
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.sh
%{_libdir}/*.so
%{_datadir}/aclocal/gnome--.m4
#exclude %{_libdir}/*.la

%changelog
* Sat Oct 25 2003 Dag Wieers <dag@wieers.com> - 1.2.3
- Updated to release 1.2.3.
