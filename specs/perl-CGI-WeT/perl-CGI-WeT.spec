# $Id$
# Authority: dries
# Upstream: James G Smith <cpan$jamesmith,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-WeT

Summary: Suite of modules to themeify a website
Name: perl-CGI-WeT
Version: 0.71
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-WeT/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-WeT-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
CGI::WeT is a package to help build a website with the ability to offer
looks for the same content.  CGI::WeT prefers Apache with mod_perl but can
be made to work without mod_perl with a little more effort.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/CGI/WeT.pm
%{perl_vendorlib}/CGI/WeT/*

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.71-1
- Initial package.
