# $Id$
# Authority: dries
# Upstream: Sam Kington <sam$illuminated,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Silly-StringMaths

Summary: Perl extension for doing maths with strings
Name: perl-Silly-StringMaths
Version: 0.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Silly-StringMaths/

Source: http://search.cpan.org/CPAN/authors/id/S/SK/SKINGTON/Silly-StringMaths-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Silly::StringMaths provides support for basic integer mathematics, using
strings rather than numbers. Upper-case letters are positive,
lower-case letters are negative, so ABCDEF would be 6 (but
WOMBAT would also be 6).

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
%{perl_vendorlib}/Silly/StringMaths.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Initial package.
