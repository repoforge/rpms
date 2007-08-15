# $Id$
# Authority: dries
# Upstream: Daniel Sirait <dns$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Language-Indonesia

Summary: Write Perl program in Bahasa Indonesia
Name: perl-Language-Indonesia
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Language-Indonesia/

Source: http://search.cpan.org//CPAN/authors/id/D/DN/DNS/Language-Indonesia-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Write Perl program in Bahasa Indonesia.

%prep
%setup -n %{real_name}

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
%doc Changes readme
%doc %{_mandir}/man3/Language::Indonesia*
%{perl_vendorlib}/Language/Indonesia.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
