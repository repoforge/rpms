# $Id$

# Authority: dries
# Upstream: Brian Ingerson <ingy$cpan,org>

%define real_name YAML
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Machine parseable data serialization format
Name: perl-YAML
Version: 0.36
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML/

Source: http://search.cpan.org/CPAN/authors/id/I/IN/INGY/YAML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
YAML is an abbreviation of YAML Ain't Markup Language. It's a straightforward 
machine-parseable data serialization format.

%prep
%setup -n %{real_name}-%{version}

%build
echo y | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/*
%{perl_vendorlib}/YAML.*
%{perl_vendorlib}/YAML/*

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Updated to release 0.36.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Initial package.
