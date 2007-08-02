# $Id$
# Authority: dries
# Upstream: Christian Renz <crenz$web42,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Find

Summary: Perl module to find and use installed modules in a (sub)category
Name: perl-Module-Find
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Find/

Source: http://ftp.cpan.org/pub/CPAN/modules/by-module/Module/Module-Find-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Module::Find lets you and use modules in categoris. This can be very useful
for auto-detecting driver or plug-in modules. You can differentiate between
looking in the category itself or in all subcategories.

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
%doc %{_mandir}/man3/Module::Find*
%dir %{perl_vendorlib}/Module
%{perl_vendorlib}/Module/Find.pm

%changelog
* Fri Aug 11 2006 Al Pacifico <adpacifico@users.sourceforge.net> - 0.05-1
- Initial packaging.
