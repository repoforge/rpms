# $Id$
# Authority: dries

Summary: PHP compiler
Name: phc
Version: 0.1.7
Release: 1%{?dist}
# versions below 0.1.5.1 were GPL
License: BSD
Group: Development/Languages
URL: http://www.phpcompiler.org/

Source: http://www.phpcompiler.org/src/archive/phc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, bison, gcc-c++

%description
phc is a compiler for PHP that will translate PHP code directly into Linux
assembly code. It can be used as a (C++) framework for developing
refactoring tools, aspect weavers, script obfuscators, and any other tools
that operate on PHP scripts.

%prep
%setup
%configure

%build
%{__make} %{?_smp_mflags}
# -C src

%install
%{__rm} -rf %{buildroot}
%makeinstall
#{__install} -Dp -m0755 src/phc %{buildroot}%{_bindir}/phc

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%{_bindir}/phc
%{_bindir}/phc_compile_plugin
%{_includedir}/phc/
%{_datadir}/phc/

%changelog
* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.7-1
- Updated to release 0.1.7.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.5.1-1.2
- Rebuild for Fedora Core 5.

* Sat Jan 28 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.5.1-1
- Updated to release 0.1.5.1.

* Fri Jan 27 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.5-1
- Updated to release 0.1.5.

* Mon Jan 09 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.4-1
- Updated to release 0.1.4.

* Mon Dec 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.3-1
- Initial package.
