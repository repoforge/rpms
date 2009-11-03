# $Id$
# Authority: dag
# Upstream: Curtis "Ovid" Poe <ovid$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-TokeParser-Simple

Summary: Easy to use C<HTML::TokeParser> interface
Name: perl-HTML-TokeParser-Simple
Version: 3.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-TokeParser-Simple/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-TokeParser-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Easy to use C<HTML::TokeParser> interface.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/HTML::TokeParser::Simple.3pm*
%doc %{_mandir}/man3/HTML::TokeParser::Simple::*.3pm*
%dir %{perl_vendorlib}/HTML/
%dir %{perl_vendorlib}/HTML/TokeParser/
%{perl_vendorlib}/HTML/TokeParser/Simple/
%{perl_vendorlib}/HTML/TokeParser/Simple.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 3.15-1
- Initial package. (using DAR)
