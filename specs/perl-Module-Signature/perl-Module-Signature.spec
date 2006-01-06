# $Id$
# Authority: dries
# Upstream: &#9786;&#21776;&#40179;&#9787; <autrijus$autrijus,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Signature

Summary: Check and create SIGNATURE files for CPAN distributions
Name: perl-Module-Signature
Version: 0.50
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Signature/

Source: http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/Module-Signature-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, gnupg, perl-ExtUtils-AutoInstall, perl-PAR-Dist

%description
A module to check and create SIGNATURE files for CPAN distributions.

%prep
%setup -n %{real_name}-%{version}

%build
echo n | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/cpansign*
%{_bindir}/cpansign
%{perl_vendorlib}/Module/Signature.pm

%changelog
* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Initial package.
