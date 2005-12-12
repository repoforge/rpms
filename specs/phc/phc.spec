# $Id$
# Authority: dries

Summary: PHP compiler
Name: phc
Version: 0.1.3
Release: 1
License: GPL
Group: Development/Languages
URL: http://www.phpcompiler.org/

Source: http://www.phpcompiler.org/src/phc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, bison, gcc-c++

%description
phc is a compiler for PHP that will translate PHP code directly into Linux 
assembly code. It can be used as a (C++) framework for developing 
refactoring tools, aspect weavers, script obfuscators, and any other tools 
that operate on PHP scripts.

%prep
%setup

%build
%{__make} %{?_smp_mflags} -C src

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/phc %{buildroot}%{_bindir}/phc

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%{_bindir}/phc

%changelog
* Mon Dec 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.3-1
- Initial package.
