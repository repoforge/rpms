# $Id$
# Authority: dag

Summary: Utility for converting bitmaps to vector graphics
Name: autotrace
Version: 0.31.1
Release: 2.2%{?dist}
License: GPL and LGPL
Group: Applications/Multimedia
URL: http://autotrace.sourceforge.net/

Source: http://dl.sf.net/autotrace/autotrace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
AutoTrace is a program for converting bitmaps to vector graphics. The
aim of the AutoTrace project is the development of a freely-available
application similar to CorelTrace or Adobe Streamline. In some
aspects it is already better. Originally being created as a plugin
for the GIMP, AutoTrace is now a standalone program and can be
compiled on any UNIX platform using GCC.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}.

%prep
%setup

%build
%configure #--without-magick --without-pstoedit
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/libautotrace.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* FAQ NEWS README* TODO
%doc %{_mandir}/man1/*
%{_bindir}/autotrace
%{_libdir}/libautotrace.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/autotrace-config
%{_libdir}/libautotrace.a
%{_libdir}/libautotrace.so
%{_includedir}/autotrace/
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.31.1-2.2
- Rebuild for Fedora Core 5.

* Mon Nov 25 2002  Dag Wieers <dag@wieers.com> - 0.31.1-0
- Updated to release 0.31.1.

* Mon Apr 30 2001 Dag Wieers <dag@wieers.com>
- Initial package.
