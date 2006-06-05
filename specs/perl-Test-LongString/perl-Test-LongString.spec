# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-LongString

Summary: Tests strings for equality, with more helpful failures
Name: perl-Test-LongString
Version: 0.09
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-LongString/

Source: http://www.cpan.org/modules/by-module/Test/Test-LongString-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

Requires: perl

%description
This module provides some drop-in replacements for the string
comparison functions of Test::More, but which are more suitable
when you test against long strings.  If you've ever had to search
for text in a multi-line string like an HTML document, or find
specific items in binary data, this is the module for you.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/LongString.pm

%changelog
* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
