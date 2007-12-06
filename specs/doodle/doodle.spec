# $Id$
# Authority: dag
# Upstream: Christian Grothoff <christian@grothoff.org>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el3:%define _without_gamin 1}
%{?fc2:%define _without_gamin 1}
%{?fc1:%define _without_gamin 1}

Summary: Searches your hard drive for files using pattern matching on meta-data
Name: doodle
Version: 0.6.7
Release: 1
License: GPL
Group: Applications/File
URL: http://gnunet.org/doodle/

Source: http://gnunet.org/doodle/download/doodle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libextractor-devel, gcc-c++, gettext
%{?_without_gamin:BuildRequires: fam-devel}
%{!?_without_gamin:BuildRequires: gamin-devel}

%description
Doodle is a tool that searches your hard drive for files using pattern
matching on meta-data. It extracts meta-data using libextractor and
builds a suffix tree to index the files. The index can then be searched
rapidly. It is similar to locate, but can take advantage of information
such as ID3 tags.

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
    --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/doodle.1*
%doc %{_mandir}/man1/doodled.1*
%{_bindir}/doodle
%{_bindir}/doodled
%{_libdir}/libdoodle.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/libdoodle.3*
%{_includedir}/doodle.h
#%{_libdir}/libdoodle.a
%{_libdir}/libdoodle.so
%{_libdir}/pkgconfig/doodle.pc
%exclude %{_libdir}/libdoodle.la

%changelog
* Thu Dec 06 2007 Dag Wieers <dag@wieers.com> - 0.6.7-1
- Updated to release 0.6.7.

* Sun Jan 07 2007 Dries Verachtert <dries@ulyssis.org> - 0.6.6-1
- Updated to release 0.6.6.

* Fri May 05 2006 Dag Wieers <dag@wieers.com> - 0.6.5-1
- Updated to release 0.6.5.

* Thu Dec 08 2005 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Updated to release 0.6.4.

* Sun Aug 07 2005 Dag Wieers <dag@wieers.com> - 0.6.3-1
- Updated to release 0.6.3.

* Thu Jan 06 2005 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Sun Oct 10 2004 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Sat Jul 24 2004 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Initial package. (using DAR)
