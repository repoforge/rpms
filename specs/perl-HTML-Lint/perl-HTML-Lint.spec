# $Id$
# Authority: dag
# Upstream: Andy Lester <andy$petdance,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Lint

Summary: Perl module to check for HTML errors in a string or file
Name: perl-HTML-Lint
Version: 2.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Lint/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Lint-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-HTML-Lint is a Perl module to check for HTML errors in a string or file.

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
%doc %{_mandir}/man3/HTML::Lint.3pm*
%doc %{_mandir}/man3/HTML::Lint::Error.3pm*
%doc %{_mandir}/man3/HTML::Lint::HTML4.3pm*
%doc %{_mandir}/man3/Test::HTML::Lint.3pm*
%{_bindir}/weblint
%dir %{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTML/Lint/
%{perl_vendorlib}/HTML/Lint.pm
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/HTML/
%{perl_vendorlib}/Test/HTML/Lint.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 2.06-1
- Updated to version 2.06.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 2.04-1
- Updated to release 2.04.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 2.02-1
- Initial package. (using DAR)
