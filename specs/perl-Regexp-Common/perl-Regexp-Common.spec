# $Id$
# Authority: dries
# Upstream: Abigail <$cpan$$abigail,nl>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Regexp-Common

Summary: Provide commonly requested regular expressions
Name: perl-Regexp-Common
Version: 2.120
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Regexp-Common/

Source: http://search.cpan.org/CPAN/authors/id/A/AB/ABIGAIL/Regexp-Common-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Provide commonly requested regular expressions.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Regexp/Common.pm
%{perl_vendorlib}/Regexp/Common

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.120-1
- Initial package.
