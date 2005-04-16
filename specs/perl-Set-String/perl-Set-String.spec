# $Id$
# Authority: dries
# Upstream: Daniel Berger <djberg96$hotmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Set-String

Summary: Strings as objects with lots of handy methods
Name: perl-Set-String
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-String/

Source: http://search.cpan.org/CPAN/authors/id/D/DJ/DJBERG/Set-String-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Set::String allows you to create strings as objects and use OO-style
methods on them. Many convenient methods are provided here that appear
in the FAQ's, the Perl Cookbook or posts from comp.lang.perl.misc. In
addition, there are Set methods with corresponding (overloaded)
operators for the purpose of Set comparison, i.e. +, ==, etc.

The purpose is to provide built-in methods for operations that people
are always asking how to do, and which already exist in languages like
Ruby. This should (hopefully) improve code readability and/or
maintainability. The other advantage to this module is method-chaining
by which any number of methods may be called on a single object in a
single statement.
	
%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Set/String.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
