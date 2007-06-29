# $Id: $
# Authority: ae
# Upstream: Damian Conway <damian$conway,org>

# package included in extras beginning with fc5
# ExclusiveDist: fc1 fc2 fc3 fc4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Std

Summary: Implementation of a "Std" class
Name: perl-Class-Std
Version: 0.0.8
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Std/

Source: http://www.cpan.org/modules/by-module/Class/Class-Std-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module provides tools that help to implement the 
"inside out object" class structure in a convenient and standard way.

Portions of the following code and documentation from 
"Perl Best Practices" copyright (c) 2005 by O'Reilly Media, Inc. 
and reprinted with permission.

%prep
%setup -n %{real_name}-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Std.pm

%changelog
* Fri Jun 29 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> 0.0.8-1
- Initial package.
