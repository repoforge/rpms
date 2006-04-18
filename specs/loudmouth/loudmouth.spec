# $Id$
# Authority: dag

Summary: Jabber client library.
Name: loudmouth
Version: 0.16
Release: 1.2
License: LGPL
Group: System Environment/Libraries
URL: http://projects.imendio.com/loudmouth/

Source: http://ftp.imendio.com/pub/imendio/loudmouth/src/loudmouth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.0.0
BuildRequires: gtk-doc >= 0.10, gcc-c++
#BuildRequires: gnutls-devel >= 1.0

%description
Loudmouth is a lightweight and easy-to-use C library for programming with
the Jabber protocol. It's designed to be easy to get started with and yet
extensible to let you do anything the Jabber protocol allows.

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

%build
%configure \
	--enable-gtk-doc \
	--with-ssl="yes"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/loudmouth/
%{_libdir}/*.so
%{_libdir}/.a
%{_libdir}/pkgconfig/*.
%{_includedir}/loudmouth-1.0/
%exclude %{_libdir}/.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1.2
- Rebuild for Fedora Core 5.

* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 0.15.1-1
- Initial packahe. (using DAR)
