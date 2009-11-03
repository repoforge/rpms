# $Id$
# Authority: dag
# Upstream: Claus Schotten <schotten$gmx,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-PrettyPrinter

Summary: Generate nice HTML files from HTML syntax trees
Name: perl-HTML-PrettyPrinter
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-PrettyPrinter/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-PrettyPrinter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Generate nice HTML files from HTML syntax trees.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/HTML::PrettyPrinter.3pm*
%dir %{perl_vendorlib}/HTML/
#%{perl_vendorlib}/HTML/PrettyPrinter/
%{perl_vendorlib}/HTML/PrettyPrinter.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
