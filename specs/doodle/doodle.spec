# $Id$
# Authority: dag

Summary: Searches your hard drive for files using pattern matching on meta-data
Name: doodle
Version: 0.5.0
Release: 1
License: GPL
Group: Applications/File
URL: http://www.ovmj.org/doodle/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.ovmj.org/doodle/download/doodle-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libextractor-devel

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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/doodle.1*
%{_bindir}/doodle
%{_libdir}/libdoodle.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/libdoodle.3*
%{_includedir}/doodle.h
%{_libdir}/libdoodle.a
%exclude %{_libdir}/libdoodle.la

%changelog
* Sun Oct 10 2004 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Sat Jul 24 2004 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Initial package. (using DAR)
