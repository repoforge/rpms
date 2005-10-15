# $Id: $
# Authority: dries

Summary: Extension for reading and writing YAML
Name: syck
Version: 0.55
Release: 1
License: GPL
Group: Development/Libraries
URL: http://www.whytheluckystiff.net/syck/

Source: http://rubyforge.org/frs/download.php/3136/syck-%{version}.tar.gz
#Source: http://rubyforge.org/frs/download.php/3717/syck-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: byacc, flex, bison

%description
Syck is an extension for reading and writing YAML swiftly in popular
scripting languages. As Syck loads the YAML, it stores the data directly in
your language's symbol table.

%package devel
Summary: Extension for reading and writing YAML
Group: Development/Libraries
Obsoletes: syck <= %{version}

%description devel
Syck is an extension for reading and writing YAML swiftly in popular
scripting languages. As Syck loads the YAML, it stores the data directly in
your language's symbol table.

%prep
%setup

%build
export CFLAGS="%{optflags} -fPIC"
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

%files devel
%defattr(-, root, root, 0755)
%doc COPYING README
%{_includedir}/syck.h
%{_includedir}/syck_st.h
%{_libdir}/libsyck.a

%changelog
* Thu Oct 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.55-1
- Updated to release 0.55.

* Sat Apr 02 2005 Dag Wieers <dag@wieers.com> - 0.51-2
- Renamed package syck to syck-devel.
- Added -fPIC to the compile options for x86_64.

* Mon Mar 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Update to version 0.51.

* Tue Feb 08 2005 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Update to version 0.50.

* Mon Sep 13 2004 Dries Verachtert <dries@ulyssis.org> - 0.45-1
- Update to version 0.45.

* Sat Jul 31 2004 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Initial package.
