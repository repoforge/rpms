# $Id$
# Authority: dries
# Upstream: Brad Fitzpatrick <brad$danga,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Set-ConsistentHash

Summary: Library for doing consistent hashing
Name: perl-Set-ConsistentHash
Version: 0.91
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-ConsistentHash/

Source: http://search.cpan.org//CPAN/authors/id/B/BR/BRADFITZ/Set-ConsistentHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Library for doing consistent hashing.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES
%doc %{_mandir}/man3/Set::ConsistentHash*
%{perl_vendorlib}/Set/ConsistentHash.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.91-1
- Initial package.
