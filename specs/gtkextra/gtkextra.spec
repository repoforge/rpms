# $Id$

# Authority: dries
# Screenshot: http://scigraphica.sourceforge.net/images/gradient.jpg
# ScreenshotURL: http://scigraphica.sourceforge.net/screenshots.html

Summary: Useful set of widgets for GTK+
Name: gtkextra
Version: 0.99.17
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://gtkextra.sourceforge.net/

Source: http://gtkextra.sourceforge.net/src/gtk+extra-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake, autoconf, gtk+-devel, glib-devel

%description
GtkExtra is a useful set of widgets for creating GUI's for the Xwindows
system using GTK+. You can use it complementary to GTK+ and it is written in
C. It is also Free Software and released under the LGPL license. 

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n gtk+extra-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/gtkextra-config
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gtkextra
%{_datadir}/aclocal/gtkextra.m4
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Mon Jan 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.99.17-1
- Initial package.
