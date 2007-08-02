# $Id$
# Authority: dries
# Upstream: Salvador Fandi&#241;o Garc&#237;a <salva$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Properties

Summary: Read and write property files
Name: perl-Config-Properties
Version: 0.65
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Properties/

Source: http://search.cpan.org//CPAN/authors/id/S/SA/SALVA/Config-Properties-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Read and write property files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Config::Properties*
%{perl_vendorlib}/Config/Properties.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.65-1
- Initial package.
