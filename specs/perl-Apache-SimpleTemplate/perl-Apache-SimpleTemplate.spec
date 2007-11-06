# $Id$
# Authority: dries
# Upstream: Peter Forty <cpan$peter,nyc,ny,us>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-SimpleTemplate

Summary: Simple templates
Name: perl-Apache-SimpleTemplate
Version: 0.05
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-SimpleTemplate/

Source: http://search.cpan.org/CPAN/authors/id/F/FO/FORTY/Apache-SimpleTemplate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Apache::SimpleTemplate is *another* Template-with-embedded-Perl package
for mod_perl. It allows you to embed blocks of Perl code into text
documents, such as HTML files, and have this code executed upon HTTP
request. It should take moments to set-up and learn; very little knowledge
of mod_perl is necessary, though some knowledge of Apache and perl is
assumed.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Apache/SimpleTemplate.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
